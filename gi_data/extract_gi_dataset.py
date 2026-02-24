from bs4 import BeautifulSoup
import os
import csv

with open("./gi_wiki_fandom.html") as fp:
    soup = BeautifulSoup(fp, features="html.parser")
    table = soup.find("table", {"class": "fandom-table article-table sortable alternating-colors-table"}).find("tbody")
    rows = table.find_all("tr")
    rows = rows[1:]  # Skip header row

    with open("gi_dataset.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)

        csv_header = ["Name", "Rarity", "Element", "Weapon", "Region", "Model"]
        writer.writerow(csv_header)

        for row in rows:
            cells = row.find_all("td")

            csv_row = []
            # Name
            if cells[1] is not None:
                csv_row.append(cells[1].find("a").text.strip())
            else:
                csv_row.append("None")

            # Rarity
            if cells[2] is not None and cells[2].find("span") is not None and cells[2].find("span").find("span") is not None:
                csv_row.append(cells[2].find("span").find("span").get("title", "").strip())
            else:
                csv_row.append("None")

            # Element
            if cells[3] is not None and cells[3].find("span") is not None and cells[3].find("span").find("a") is not None:
                csv_row.append(cells[3].find("span").find("a").get("title", "").strip())
            else:
                csv_row.append("None")

            # Weapon
            if cells[4] is not None and cells[4].find("span") is not None and cells[4].find("span").find("a") is not None:
                csv_row.append(cells[4].find("span").find("a").get("title", "").strip())
            else:
                csv_row.append("None")

            # Region
            if cells[5] is not None and cells[5].find("span") is not None and cells[5].find("span").find("a") is not None:
                csv_row.append(cells[5].find("span").find("a").get("title", "").strip())
            else:
                csv_row.append("None")

            # Model
            if cells[6] is not None and cells[6].find("a") is not None:
                csv_row.append(cells[6].find("a").text.strip())
            else:
                csv_row.append("None")

            writer.writerow(csv_row)

print("Finished extracting data.")