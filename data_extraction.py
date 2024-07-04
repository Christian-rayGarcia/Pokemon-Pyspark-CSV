import requests
import csv


class DataExtraction:
	def __init__(self, base_url, endpoint, data_processor, output_file):
		self.base_url = base_url
		self.endpoint = endpoint
		self.data_processor = data_processor
		self.output_file = output_file

	def get_data(self):
		# Get the total count of items
		with requests.Session() as session:
			response = session.get(f"{self.base_url}{self.endpoint}")
			response.raise_for_status()
			total_items = response.json()['count']

			# list to hold data
			data = []

			for i in range(1, total_items + 1):
				try:
					response = session.get(f"{self.base_url}{self.endpoint}/{i}")
					response.raise_for_status()
					item_data = response.json()
					processed_data = self.data_processor(item_data)
					data.append(processed_data)
				except requests.RequestException:
					break
			print("Extraction complete.")

		self.write_to_csv(data)

	def write_to_csv(self, data):
		with open(self.output_file, "w", newline='') as file:
			writer = csv.writer(file)
			writer.writerow(data[0].keys())  # Write header
			for row in data:
				writer.writerow(row.values())