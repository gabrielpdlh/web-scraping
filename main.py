import os
import requests
import zipfile
from bs4 import BeautifulSoup

def download_pdf(url, download_folder):
    filename = os.path.join(download_folder, url.split("/")[-1])
    
    try:
        response = requests.get(url, stream=True, timeout=10)
        response.raise_for_status()
        
        with open(filename, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
                
        print(f"Downloaded: {filename}")
        return filename
        
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return None

def find_pdf_links(soup):
    pdf_links = []
    ol = soup.find("ol")
    
    if ol:
        for li in ol.find_all("li"):
            pdf_link = li.find("a", href=lambda href: href and href.endswith(".pdf"))
            if pdf_link:
                pdf_links.append(pdf_link["href"])
    
    return pdf_links

def main():
    page_url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    download_dir = "downloads"
    zip_filename = "attachments.zip"
    
    os.makedirs(download_dir, exist_ok=True)
    
    response = requests.get(page_url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    pdf_links = find_pdf_links(soup)
    
    downloaded_files = []
    for link in pdf_links:
        file_path = download_pdf(link, download_dir)
        if file_path:
            downloaded_files.append(file_path)
    
    zip_path = os.path.join(download_dir, zip_filename)
    with zipfile.ZipFile(zip_path, "w") as zipf:
        for file in downloaded_files:
            zipf.write(file, os.path.basename(file))
            print(f"Added to ZIP: {file}")
    
    print(f"\nAll PDFs have been compressed into: {zip_path}")

if __name__ == "__main__":
    main()