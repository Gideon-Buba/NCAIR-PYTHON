def calculate_bmi(weight_kg, height_m):
    """
    Calculate Body Mass Index (BMI) using weight in kilograms and height in meters.

    Args:
        weight_kg (float): Weight in kilograms.
        height_m (float): Height in meters.

    Returns:
        float: Calculated BMI.
    """
    bmi = weight_kg / (height_m ** 2)
    return bmi

# Example usage:
weight = 70  # in kilograms
height = 1.75  # in meters
bmi = calculate_bmi(weight, height)
print("BMI:", bmi)