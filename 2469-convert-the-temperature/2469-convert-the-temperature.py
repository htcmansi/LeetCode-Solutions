class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin=float(celsius + 273.15)
        farenite=float(celsius * 9/5)+32
        return [kelvin,farenite]
        
        
        