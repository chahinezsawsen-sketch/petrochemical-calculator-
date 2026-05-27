# main.py

def calculate_api_gravity(specific_gravity):
    """حساب درجة الكثافة المعهد الأمريكي للبترول (API Gravity)"""
    if specific_gravity <= 0:
        raise ValueError("Specific gravity must be greater than 0")
    api = (141.5 / specific_gravity) - 131.5
    return round(api, 2)

def calculate_flow_rate(velocity, diameter):
    """حساب معدل التدفق الحجمي في أنبوب دائري (Q = A * v)"""
    import math
    if velocity < 0 or diameter <= 0:
        raise ValueError("Velocity and diameter must be positive values")
    radius = diameter / 2
    area = math.pi * (radius ** 2)
    flow_rate = area * velocity
    return round(flow_rate, 4)

def estimate_z_factor(pressure, temperature):
    """حساب تقريبي جداً لمعامل انضغاطية الغاز بناءً على الضغط والحرارة"""
    if pressure < 0 or temperature <= 0:
        raise ValueError("Invalid physical properties")
    z = 1 - (0.0005 * pressure) / (temperature / 100)
    return round(max(0.3, min(z, 1.0)), 3)

def menu():
    print("\n" + "="*35)
    print("  Petrochemical Calculator v1.0  ")
    print("="*35)
    print("1. Calculate API Gravity")
    print("2. Calculate Pipe Flow Rate")
    print("3. Estimate Gas Z-Factor")
    print("4. Exit")
    print("="*35)

if __name__ == "__main__":
    while True:
        menu()
        choice = input("Enter your choice (1-4): ")
        
        try:
            if choice == '1':
                sg = float(input("Enter Specific Gravity (e.g., 0.85): "))
                api = calculate_api_gravity(sg)
                print(f"Result: API Gravity = {api} API")
            elif choice == '2':
                v = float(input("Enter Velocity (m/s): "))
                d = float(input("Enter Pipe Diameter (m): "))
                q = calculate_flow_rate(v, d)
                print(f"Result: Flow Rate = {q} m3/s")
            elif choice == '3':
                p = float(input("Enter Pressure (bar): "))
                t = float(input("Enter Temperature (Kelvin): "))
                z = estimate_z_factor(p, t)
                print(f"Result: Estimated Z-Factor = {z}")
            elif choice == '4':
                print("Thank you for using Petrochemical Calculator. Goodbye!")
                break
            else:
                print("Invalid choice! Please select between 1 and 4.")
        except ValueError as e:
            print(f"Error: {e}. Please enter valid numbers.")
