import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import os

# Data dictionary to store extracted information
d = {'username': [], 'bio': [], 'location': [], 'website': [], 'following': [], 'followers': []}

# Ensure the data directory exists
data_dir = "data"
if not os.path.exists(data_dir):
    print(f"The directory {data_dir} does not exist!")
else:
    for file in os.listdir(data_dir):
        file_path = os.path.join(data_dir, file)

        # Ensure you're only reading HTML files (optional)
        if file.endswith(".html"):
            try:
                # Open the file with proper encoding to avoid UnicodeDecodeError
                with open(file_path, 'r', encoding='utf-8') as f:
                    html_doc = f.read()

                # Parse the HTML content with BeautifulSoup
                soup = BeautifulSoup(html_doc, 'html.parser')

                # Extracting the username
                username = soup.find('div', class_='css-175oi2r r-1awozwy r-18u37iz r-1wbh5a2')
                if username:
                    username = username.get_text()
                else:
                    print(f"Missing username in {file}")
                    username = np.nan  # Assigning NaN value using numpy

                # Extracting the bio
                bio = soup.find("div", class_="css-175oi2r r-1adg3ll r-6gpygo")
                if bio:
                    bio = bio.get_text()
                else:
                    print(f"Missing bio in {file}")
                    bio = np.nan

                # Extracting the location
                location = soup.find('span', {'data-testid': 'UserLocation'})
                if location:
                    location = location.get_text()
                else:
                    print(f"Missing location in {file}")
                    location = np.nan

                # Extracting the website
                website = soup.find('a', {'data-testid': 'UserUrl'})
                if website and website.get('href'):
                    website = website['href']
                else:
                    print(f"Missing website in {file}")
                    website = np.nan

                # Extracting the following count
                following = soup.find('span',
                                      class_='css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3 r-1b43r93 r-1cwl3u0 r-b88u0q')
                if following:
                    following = following.get_text().strip()
                else:
                    print(f"Missing following count in {file}")
                    following = np.nan

                # Extracting the followers count
                followers = soup.find_all('span',
                                          class_='css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3 r-1b43r93 r-1cwl3u0 r-b88u0q')[
                    1]
                if followers:
                    followers = followers.get_text().strip()
                else:
                    print(f"Missing followers count in {file}")
                    followers = np.nan

                # Append data to the dictionary
                d['username'].append(username)
                d['bio'].append(bio)
                d['location'].append(location)
                d['website'].append(website)
                d['following'].append(following)
                d['followers'].append(followers)

            except Exception as e:
                print(f"Error reading {file_path}: {e}")

# Convert the data dictionary to a DataFrame
df = pd.DataFrame(data=d)

# Check for missing values in the DataFrame
missing_values = df.isnull().sum()
print("Missing values in the dataset:")
print(missing_values)

# Save the DataFrame to a CSV file
df.to_csv('twitter_data2.csv', index=False)
