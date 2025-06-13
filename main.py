from instagrapi import Client
from instagrapi.exceptions import LoginRequired, ClientError
import time
import random
import logging
import os
import sys

print("Welcome to the Unfollower Bot")
# Configure logging to both console and file
def setup_logger():
    logger = logging.getLogger('insta_unfollow')
    logger.setLevel(logging.INFO)
    
    # Create handlers
    console_handler = logging.StreamHandler(sys.stdout)
    file_handler = logging.FileHandler('unfollow_log.txt', mode='a')
    
    # Create formatters and add to handlers
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    
    # Add handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    return logger

logger = setup_logger()

# Safety constants
MAX_RETRIES = 3
BASE_DELAY = 300  # 5 minutes base delay for rate limits
DAILY_LIMIT = 100  # Instagram's approximate daily action limit

def login_user(username, password, api_delay_range, force_logout=False):
    """Log in to Instagram with session management and 2FA handling"""
    session_file = f"{username}_session.json"
    
    cl = Client()
    cl.delay_range = api_delay_range
    
    if os.path.exists(session_file) and not force_logout:
        try:
            logger.info("Loading existing session...")
            cl.load_settings(session_file)
            cl.login(username, password)
            logger.info("Successfully logged in using existing session")
            return cl
        except LoginRequired:
            logger.warning("Session expired - relogging in")
            os.remove(session_file)
    
    # New login or forced logout
    if force_logout and os.path.exists(session_file):
        try:
            logger.info("Attempting to logout from existing session...")
            cl.load_settings(session_file)
            cl.logout()
            logger.info("Successfully logged out from existing session")
            os.remove(session_file)
        except Exception as e:
            logger.error(f"Error during logout: {e}")
    
    try:
        logger.info("Attempting new login...")
        cl.login(username, password)
    except LoginRequired as e:
        if "two_factor" in str(e).lower():
            logger.info("2FA code required")
            code = input("Enter 2FA code: ")
            cl.two_factor_login(code)
        else:
            logger.error("Login failed")
            raise
    
    cl.dump_settings(session_file)
    logger.info("Successfully logged in and saved session")
    return cl

def unfollow_non_followers(username, password, max_unfollow, api_delay_range, action_delay_range, force_logout=False):
    try:
        cl = login_user(username, password, api_delay_range, force_logout)
        
        # Safety check
        if max_unfollow > DAILY_LIMIT:
            logger.warning(f"⚠️ Warning: Instagram's daily limit is ~{DAILY_LIMIT} actions!")
            confirm = input(f"Continue with {max_unfollow} unfollows? (y/n): ")
            if confirm.lower() != 'y':
                logger.info("Unfollow operation aborted by user")
                return

        user_id = cl.user_id
        logger.info("Fetching following list...")
        following = cl.user_following(user_id)
        logger.info(f"Found {len(following)} accounts you follow")
        
        logger.info("Fetching followers list...")
        followers = cl.user_followers(user_id)
        logger.info(f"Found {len(followers)} accounts following you")

        # Calculate non-followers and randomize order
        non_followers = list(set(following.keys()) - set(followers.keys()))
        random.shuffle(non_followers)
        
        limit = min(max_unfollow, len(non_followers))
        non_followers = non_followers[:limit]
        
        logger.info(f"Preparing to unfollow {len(non_followers)}/{max_unfollow} non-followers")
        logger.info(f"⚙️ Settings: API delays {api_delay_range}s | Action delays {action_delay_range}s")

        retry_count = 0
        for count, user_id in enumerate(non_followers, 1):
            user = following[user_id]
            try:
                while retry_count < MAX_RETRIES:
                    try:
                        logger.info(f"Attempting to unfollow {user.username}...")
                        cl.user_unfollow(user_id)
                        logger.info(f"[{count}/{limit}] Successfully unfollowed {user.username}")
                        retry_count = 0  # Reset retry counter
                        
                        # Progressive delay increase
                        action_delay = random.uniform(*action_delay_range) * (1 + (count/100))
                        logger.debug(f"Sleeping for {action_delay:.2f} seconds")
                        time.sleep(action_delay)
                        
                        # Random long pause every 10-30 actions
                        if count % random.randint(10, 30) == 0:
                            long_pause = random.uniform(120, 300)
                            logger.info(f"⏸ Taking safety pause: {long_pause/60:.1f} minutes")
                            time.sleep(long_pause)
                        
                        break
                        
                    except ClientError as e:
                        if "wait a few minutes" in str(e).lower():
                            wait_time = BASE_DELAY * (2 ** retry_count)
                            logger.warning(f"⏳ Rate limited! Waiting {wait_time/60:.1f} minutes (retry {retry_count+1}/{MAX_RETRIES})")
                            time.sleep(wait_time)
                            retry_count += 1
                        else:
                            logger.error(f"Unfollow error: {e}")
                            raise
                
                if retry_count >= MAX_RETRIES:
                    logger.error("❌ Max retries exceeded. Stopping for safety.")
                    break

            except Exception as e:
                logger.error(f"Failed to unfollow {user.username}: {str(e)}")
                time.sleep(60)

        logger.info(f"✅ Unfollow process completed. {limit} accounts unfollowed.")

    except Exception as e:
        logger.error(f"❌ Critical error occurred: {e}")
    finally:
        try:
            if 'cl' in locals():
                logger.info("Logging out...")
                cl.logout()
        except Exception as e:
            logger.error(f"Error during logout: {e}")

def get_float_input(prompt, default):
    """Helper function to get numeric input with default value"""
    while True:
        try:
            value = input(f"{prompt} (default {default}): ")
            return float(value) if value.strip() else default
        except ValueError:
            print("Please enter a valid number")

def main_menu():
    print("\n" + "="*40)
    print(" INSTAGRAM UNFOLLOW BOT ".center(40, "⚡"))
    print("="*40)
    print("1. Run unfollow bot")
    print("2. Logout from existing session")
    print("3. Exit")
    return input("Select an option (1-3): ")

if __name__ == "__main__":
    USERNAME = "add your username here" #👈👈👈👈👈👈👈👈
    PASSWORD = "add your password here" #👈👈👈👈👈👈👈👈
    
    while True:
        choice = main_menu()
        
        if choice == "1":
            try:
                max_unfollow = int(input("\nHow many people do you want to unfollow? "))
                if max_unfollow <= 0:
                    print("Please enter a positive number.")
                    continue
                
                print("\nConfigure delays (in seconds):")
                api_min = get_float_input("  Minimum delay between API requests", 2)
                api_max = get_float_input("  Maximum delay between API requests", 3)
                action_min = get_float_input("  Minimum delay between unfollow actions", 5)
                action_max = get_float_input("  Maximum delay between unfollow actions", 15)
                
                # Validate ranges
                api_delay_range = [min(api_min, api_max), max(api_min, api_max)]
                action_delay_range = [min(action_min, action_max), max(action_min, action_max)]
                
                unfollow_non_followers(
                    USERNAME,
                    PASSWORD,
                    max_unfollow,
                    api_delay_range,
                    action_delay_range
                )
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
                
        elif choice == "2":
            confirm = input("\nAre you sure you want to logout? (y/n): ")
            if confirm.lower() == 'y':
                try:
                    cl = Client()
                    session_file = f"{USERNAME}_session.json"
                    if os.path.exists(session_file):
                        logger.info("Loading session for logout...")
                        cl.load_settings(session_file)
                        cl.logout()
                        os.remove(session_file)
                        logger.info("✅ Successfully logged out and removed session file")
                    else:
                        logger.info("ℹ️ No active session found")
                except Exception as e:
                    logger.error(f"❌ Error during logout: {e}")
            input("\nPress Enter to continue...")
            
        elif choice == "3":
            logger.info("Goodbye!")
            break
            
        else:
            print("\nInvalid choice. Please select 1-3")
