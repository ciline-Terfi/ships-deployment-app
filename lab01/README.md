DATASET resource / kaggle ( ship_fuel_efficiency.csv )
1.Type of dataset:
	This is a structured, tabular dataset ( organized in rows and columns ) . 
		rows -> represent a single trip 
		columns -> technical, environmental, or logistical feature of that journey.
	it's a midium sized dataset
2. Type of Data Contained:
  1/Quantitative:
	Column                     Type                             Description
	Distance                Continuous                 The total distance traveled in nautical miles.
	Fuel Consumption        Continuous                 Amount of fuel burned (mass/volume).
	CO2 Emissions           Continuous                 Total carbon footprint of the trip.
	Engine Efficiency       Continuous                 Performance percentage of the ship's engine. 
  2/Qualitative:
	Ship ID                  Nominal                   Unique name or ID of the vessel.
	Ship Type                Nominal                   Type of ship (Tanker, Cargo, Container)
	Route I                  Nominal                   Origin-Destination pair (e.g., Lagos-Warri).
	Month                    Ordinal                   Time of the year (January to December)and have a logical order .
	Fuel Type                Nominal                   Energy source (HFO, diesel).
	Weather Conditions       Nominal                   Environmental state (Calm < Moderate < Stormy).
3. Appropriate Mathematical Operations & Statistical Methods:
	Mean, Median, Mode: To find the average engine efficiency and typical fuel consumption per ship type.

	Standard Deviation: To measure the volatility of fuel usage—how much does it vary between a calm trip and a stormy one

	Min/Max: Identifying the longest distance trips and the lowest efficiency "risk" points.
4.explanation of the content; 
	it is a mix between lab 0 that request a first manipulation of a choosen dataset and the lab1 that asks for a descriptive statistics 
