class SmartHomeDevice:
    def __init__(self, device_name, device_type, location, is_on=False, battery_level=100):
        self.device_name = device_name
        self.device_type = device_type
        self.location = location
        self.is_on = is_on
        self._battery_level = battery_level  # encapsulated attribute
    
    def toggle_power(self):
        self.is_on = not self.is_on
        status = "on" if self.is_on else "off"
        return f"{self.device_name} is now {status} 🔌"
    
    def check_battery(self):
        return f"{self.device_name} battery level: {self._battery_level}%"
    
    def _drain_battery(self, amount):
        
        self._battery_level = max(0, self._battery_level - amount)
    
    def recharge(self):
        self._battery_level = 100
        return f"{self.device_name} is fully charged! ⚡"
    
    def get_status(self):
        status = "On" if self.is_on else "Off"
        return f"{self.device_name} ({self.device_type}) in {self.location}: {status} | Battery: {self._battery_level}%"
    
    def __str__(self):
        return f"{self.device_name} - {self.device_type} in {self.location}"

# Inheritance layer - Specialized smart devices
class SmartLight(SmartHomeDevice):
    def __init__(self, device_name, location, brightness=50, color="white", is_on=False, battery_level=100):
        super().__init__(device_name, "Smart Light", location, is_on, battery_level)
        self.brightness = brightness  # 0-100%
        self.color = color
    
    def set_brightness(self, level):
        if 0 <= level <= 100:
            self.brightness = level
            if self.is_on and level > 0:
                self._drain_battery(1)  # Using parent's protected method
            return f"{self.device_name} brightness set to {level}%"
        return "Brightness must be between 0-100%"
    
    def change_color(self, new_color):
        self.color = new_color
        if self.is_on:
            self._drain_battery(2)
        return f"{self.device_name} color changed to {new_color} 🌈"
    
    def get_status(self):
        base_status = super().get_status()
        return f"{base_status} | Brightness: {self.brightness}% | Color: {self.color}"

class SmartThermostat(SmartHomeDevice):
    def __init__(self, device_name, location, temperature=72, mode="cool", is_on=False, battery_level=100):
        super().__init__(device_name, "Smart Thermostat", location, is_on, battery_level)
        self.temperature = temperature  # Fahrenheit
        self.mode = mode  # heat, cool, auto
    
    def set_temperature(self, new_temp):
        self.temperature = new_temp
        if self.is_on:
            self._drain_battery(3)
        return f"{self.device_name} set to {new_temp}°F"
    
    def set_mode(self, new_mode):
        if new_mode in ["heat", "cool", "auto"]:
            self.mode = new_mode
            if self.is_on:
                self._drain_battery(2)
            return f"{self.device_name} mode set to {new_mode}"
        return "Mode must be 'heat', 'cool', or 'auto'"
    
    def get_status(self):
        base_status = super().get_status()
        return f"{base_status} | Temp: {self.temperature}°F | Mode: {self.mode}"


if __name__ == "__main__":
    print("=== SMART HOME DEVICE  ===\n")
    
    # Create smart devices
    kitchen_light = SmartLight("Kitchen Main Light", "Kitchen", brightness=75, color="warm white")
    living_thermostat = SmartThermostat("Living Room AC", "Living Room", temperature=68, mode="cool")
    
    # functionality
    print(kitchen_light.toggle_power())
    print(kitchen_light.set_brightness(80))
    print(kitchen_light.change_color("soft yellow"))
    print(kitchen_light.check_battery())
    print()
    
    print(living_thermostat.toggle_power())
    print(living_thermostat.set_temperature(70))
    print(living_thermostat.set_mode("auto"))
    print(living_thermostat.check_battery())
    print()
    
    # Show polymorphism with get_status method
    devices = [kitchen_light, living_thermostat]
    for device in devices:
        print(device.get_status())
    
    print("\nAfter some battery usage:")
    kitchen_light._drain_battery(15)  # Simulate battery drain
    print(kitchen_light.check_battery())
    print(kitchen_light.recharge())