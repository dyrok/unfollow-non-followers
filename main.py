from instagrapi import Client
from instagrapi.exceptions import LoginRequired, ClientError
import time
import random
import logging
import os

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger()

def login_user(username, password, api_delay_range):
    """Log in to Instagram with session management and 2FA handling"""
    session_file = f"{username}_session.json"
    
    cl = Client()
    cl.delay_range = api_delay_range  # Set API request delays
    
    if os.path.exists(session_file):
        try:
            cl.load_settings(session_file)
            cl.login(username, password)
            logger.info("Logged in using existing session")
            return cl
        except LoginRequired:
            logger.warning("Session expired - relogging in")
            os.remove(session_file)
    
    # New login
    try:
        cl.login(username, password)
    except LoginRequired as e:
        if "two_factor" in str(e).lower():
            code = input("Enter 2FA code: ")
            cl.two_factor_login(code)
        else:
            raise
    
    cl.dump_settings(session_file)
    logger.info("Successfully logged in")
    return cl

def unfollow_non_followers(username, password, max_unfollow, api_delay_range, action_delay_range):
    cl = login_user(username, password, api_delay_range)
    
    try:
        user_id = cl.user_id
        logger.info("Fetching following list...")
        following = cl.user_following(user_id)
        logger.info("Fetching followers list...")
        followers = cl.user_followers(user_id)

        # Calculate non-followers and randomize order
        non_followers = list(set(following.keys()) - set(followers.keys()))
        random.shuffle(non_followers)
        
        limit = min(max_unfollow, len(non_followers))
        non_followers = non_followers[:limit]
        
        logger.info(f"Found {len(non_followers)}/{max_unfollow} non-followers to unfollow")

        # Unfollow process with custom delays
        for count, user_id in enumerate(non_followers, 1):
            user = following[user_id]
            try:
                cl.user_unfollow(user_id)
                logger.info(f"[{count}/{limit}] Unfollowed {user.username}")
                
                # Customizable action delay
                delay = random.uniform(*action_delay_range)
                logger.debug(f"Sleeping for {delay:.2f} seconds")
                time.sleep(delay)
                
            except ClientError as e:
                logger.error(f"Failed to unfollow {user.username}: {e}")
                time.sleep(60)

        logger.info(f"Unfollow process completed. {limit} accounts unfollowed.")

    except Exception as e:
        logger.error(f"An error occurred: {e}")
    finally:
        cl.logout()

def get_float_input(prompt, default):
    """Helper function to get numeric input with default value"""
    while True:
        try:
            value = input(f"{prompt} (default {default}): ")
            return float(value) if value.strip() else default
        except ValueError:
            print("Please enter a valid number")

if __name__ == "__main__":
    # Credentials ⚠️⚠️⚠️ REPLACE HERE ⚠️⚠️⚠️
    USERNAME = "your_instagram_username"
    PASSWORD = "your_instagram_password"
    
    try:
        # Get unfollow count
        max_unfollow = int(input("How many people do you want to unfollow? "))
        if max_unfollow <= 0:
            print("Please enter a positive number.")
            exit()
        
        # Get delay settings
        print("\nConfigure delays (in seconds):")
        api_min = get_float_input("  Minimum delay between API requests", 2)
        api_max = get_float_input("  Maximum delay between API requests", 3)
        action_min = get_float_input("  Minimum delay between unfollow actions", 2)
        action_max = get_float_input("  Maximum delay between unfollow actions", 3)
        
        # Validate ranges
        api_delay_range = [min(api_min, api_max), max(api_min, api_max)]
        action_delay_range = [min(action_min, action_max), max(action_min, action_max)]
        
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        exit()
    
    unfollow_non_followers(
        USERNAME,
        PASSWORD,
        max_unfollow,
        api_delay_range,
        action_delay_range
    )
