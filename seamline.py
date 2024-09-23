from paddleocr import PaddleOCR
import pandas as pd

entity_unit_map = {
    'width': [
        ['centimetre', 'centimetres', 'cm', 'cms'],
        ['foot', 'feet', 'ft'],
        ['inch', 'inches', 'in'],
        ['metre', 'meter', 'meters', 'm'],
        ['millimetre', 'millimeter', 'millimeters', 'mm'],
        ['yard', 'yards', 'yd', 'yds']
    ],
    'depth': [
        ['centimetre', 'centimetres', 'cm', 'cms'],
        ['foot', 'feet', 'ft'],
        ['inch', 'inches', 'in'],
        ['metre', 'meter', 'meters', 'm'],
        ['millimetre', 'millimeter', 'millimeters', 'mm'],
        ['yard', 'yards', 'yd', 'yds']
    ],
    'height': [
        ['centimetre', 'centimetres', 'cm', 'cms'],
        ['foot', 'feet', 'ft'],
        ['inch', 'inches', 'in'],
        ['metre', 'meter', 'meters', 'm'],
        ['millimetre', 'millimeter', 'millimeters', 'mm'],
        ['yard', 'yards', 'yd', 'yds']
    ],
    'item_weight': [
        ['gram', 'grams', 'g'],
        ['kilogram', 'kilograms', 'kg', 'kgs'],
        ['microgram', 'micrograms', 'μg', 'mcg'],
        ['milligram', 'milligrams', 'mg'],
        ['ounce', 'ounces', 'oz'],
        ['pound', 'pounds', 'lb', 'lbs'],
        ['ton', 'tons', 't']
    ],
    'maximum_weight_recommendation': [
        ['gram', 'grams', 'g'],
        ['kilogram', 'kilograms', 'kg', 'kgs'],
        ['microgram', 'micrograms', 'μg', 'mcg'],
        ['milligram', 'milligrams', 'mg'],
        ['ounce', 'ounces', 'oz'],
        ['pound', 'pounds', 'lb', 'lbs'],
        ['ton', 'tons', 't']
    ],
    'voltage': [
        ['kilovolt', 'kilovolts', 'kV'],
        ['millivolt', 'millivolts', 'mV'],
        ['volt', 'volts', 'V']
    ],
    'wattage': [
        ['kilowatt', 'kilowatts', 'kW'],
        ['watt', 'watts', 'W']
    ],
    'item_volume': [
        ['centilitre', 'centiliter', 'centiliters', 'cl'],
        ['cubic foot', 'cubic feet', 'cu ft', 'ft³'],
        ['cubic inch', 'cubic inches', 'cu in', 'in³'],
        ['cup', 'cups'],
        ['decilitre', 'deciliter', 'deciliters', 'dl'],
        ['fluid ounce', 'fluid ounces', 'fl oz'],
        ['gallon', 'gallons', 'gal'],
        ['imperial gallon', 'imperial gallons', 'imp gal'],
        ['litre', 'liter', 'liters', 'litres', 'L', 'l'],
        ['microlitre', 'microliter', 'microliters', 'microlitres', 'μL', 'mcL'],
        ['millilitre', 'milliliter', 'milliliters', 'millilitres', 'mL'],
        ['pint', 'pints', 'pt'],
        ['quart', 'quarts', 'qt']
    ]
}

csv_file_path = r'D:\Aikens\student_resource\dataset\sample_test.csv'
df = pd.read_csv(csv_file_path)

# Print the first 5 rows of the DataFrame
print(df.head())

# Initialize the PaddleOCR model with the angle classifier
ocr = PaddleOCR(use_angle_cls=True)

size = len(df)

image = df.iloc[0][1].split("/")[-1]
gid = df.iloc[0][2]
ent_name = df.iloc[0][3]

words =[]

for i in range(size):
    if i >0 and df.iloc[i][2]!=df.iloc[i-1][2]:
        words =
        
    image = df.iloc[i][1].split("/")[-1]
    gid = df.iloc[i][2]
    ent_name = df.iloc[i][3]
    print(f"{image}  {gid}  {ent_name}")
 

# ocr = PaddleOCR(use_angle_cls=True)

# result = ocr.ocr(r'D:\Aikens\student_resource\images\51r7U52rh7L.jpg')

# for line in result:
#     for word_info in line:
#         print("----------------------------------------------")
#         print(f"Text: {word_info[1][0]}")  # Detected text
#         print(f"Coordinates: {word_info[0]}")  # Bounding box coordinates
#         print(f"Accuracy: {word_info[1][1]:.2f}")  # Confidence score
