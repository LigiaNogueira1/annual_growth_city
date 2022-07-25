city_a = 80000
city_b = 200000
annual_growth_a = 0.03
annual_growth_b = 0.015

year = 0

while city_a < city_b:
	city_a=city_a+(city_a*annual_growth_a)
	city_b=city_b+(city_b*annual_growth_b)
	year=year+1

if city_a > city_b:
    print("The number of years for city A exceed city B will be" ,year, "years.")