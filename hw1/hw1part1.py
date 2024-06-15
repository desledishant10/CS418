import pandas as pd
import numpy as np

# Question 1.1

def extract_hour(time):
    """
    Extracts hour information from military time.
    
    Args: 
        time (float64): array of time given in military format.  
          Takes on values in 0.0-2359.0 due to float64 representation.
    
    Returns:
        array (float64): array of input dimension with hour information.  
          Should only take on integer values in 0-23
    """
    # Extract the hour by integer division
    hours = time // 100
    # Use Series.where to filter out invalid hours (less than 0 or greater than 23)
    valid_hours = pd.Series(hours).where((hours >= 0) & (hours < 24), np.nan)
    return valid_hours
    
def extract_mins(time):
    """
    Extracts minute information from military time
    
    Args: 
        time (float64): array of time given in military format.  
          Takes on values in 0.0-2359.0 due to float64 representation.
    
    Returns:
        array (float64): array of input dimension with hour information.  
          Should only take on integer values in 0-59
    """
    # Extract minutes by taking the remainder of division by 100
    minutes = time % 100
    # Use Series.where to filter out invalid minutes (less than 0 or greater than 59)
    valid_minutes = pd.Series(minutes).where((minutes >= 0) & (minutes < 60), np.nan)
    return valid_minutes

# Question 1.2

def convert_to_minofday(time):
    """
    Converts military time to minute of day
    
    Args:
        time (float64): array of time given in military format.  
          Takes on values in 0.0-2359.0 due to float64 representation.
    
    Returns:
        array (float64): array of input dimension with minute of day
    
    Example: 1:03pm is converted to 783.0
    >>> convert_to_minofday(1303.0)
    783.0
    """
    # Extract hour and convert to minutes
    hours_in_min = (time // 100) * 60
    # Extract minutes
    minutes = time % 100
    # Combine to get minute of day
    min_of_day = hours_in_min + minutes
    # Validate time and replace invalid values with NaN
    valid_min_of_day = pd.Series(min_of_day).where((min_of_day >= 0) & (min_of_day <= 1440), np.nan)
    return valid_min_of_day
    
    
def calc_time_diff(x, y):
    """
    Calculates delay times y - x
    
    Args:
        x (float64): array of scheduled time given in military format.  
          Takes on values in 0.0-2359.0 due to float64 representation.
        y (float64): array of same dimensions giving actual time
    
    Returns:
        array (float64): array of input dimension with delay time
    """
    
    scheduled = convert_to_minofday(x)
    actual = convert_to_minofday(y)
    
    # Calculate delay by subtracting scheduled from actual
    delay = actual - scheduled
    return delay