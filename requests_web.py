import requests
 
def cria_lista_links(content):
    links = []
    for line in content.split(bytes('</p>', 'UTF-8')):
        index = line.find(bytes('class="title ', 'UTF-8'))
        if index != -1:
            href_start = line.find(bytes('href="', 'UTF-8'), index) + 6
            href_end = line.find(bytes('"', 'UTF-8'), href_start)
            links.append(line[href_start:href_end])
    return links
 
r = requests.get("http://www.reddit.com/r/programming")
print('\n'.join(str(cria_lista_links(r.content))))