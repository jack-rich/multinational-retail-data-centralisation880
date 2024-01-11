import csv
import requests
import boto3
from botocore.exceptions import NoCredentialsError

class DataExtractor:
    def __init__(self):
        pass

    def extract_data_from_csv(self, file_path):
        """
        Extract data from a CSV file.

        Parameters:
        - file_path (str): Path to the CSV file.

        Returns:
        - list: List of dictionaries representing the extracted data.
        """
        data = []
        try:
            with open(file_path, 'r') as csvfile:
                csv_reader = csv.DictReader(csvfile)
                for row in csv_reader:
                    data.append(row)
        except FileNotFoundError:
            print(f"Error: CSV file '{file_path}' not found.")
        except Exception as e:
            print(f"Error extracting data from CSV: {str(e)}")
        return data

    def extract_data_from_api(self, api_url):
        """
        Extract data from an API.

        Parameters:
        - api_url (str): URL of the API.

        Returns:
        - list: List of dictionaries representing the extracted data.
        """
        data = []
        try:
            response = requests.get(api_url)
            response.raise_for_status()
            data = response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error extracting data from API: {str(e)}")
        return data

    def extract_data_from_s3(self, bucket_name, object_key):
        """
        Extract data from an S3 bucket.

        Parameters:
        - bucket_name (str): Name of the S3 bucket.
        - object_key (str): Key of the object within the bucket.

        Returns:
        - str: Content of the object in the S3 bucket.
        """
        s3 = boto3.client('s3')
        data = ""
        try:
            response = s3.get_object(Bucket=bucket_name, Key=object_key)
            data = response['Body'].read().decode('utf-8')
        except NoCredentialsError:
            print("Error: AWS credentials not available.")
        except Exception as e:
            print(f"Error extracting data from S3: {str(e)}")
        return data