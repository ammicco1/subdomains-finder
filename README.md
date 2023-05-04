# Simple python script to check if a list of subdomains is up or down

The script check if a list of subdomains exist using PING, in particular: 
``` python
    subprocess.run(["ping", "-c", "1", hostname])
```

So it exec a single ping, if it recive a response, the domain is up.

To run the script use: 
``` bash
    python3 main.py -f subdomain-list-filename.txt main-domain

    # an example 
    
    $ cat subdomains.txt
    www
    mail
    ftp
    localhost
    webmail
    smtp
    pop
    ns1

    $ python3 main.py -f subdomains.txt archlinux.org
    www.archlinux.org is up
    mail.archlinux.org is up
    ftp.archlinux.org is down
    localhost.archlinux.org is down
    webmail.archlinux.org is down
    smtp.archlinux.org is down
    pop.archlinux.org is down
    ns1.archlinux.org is down
```

you can redirect the output to a file with the ```-o``` option and select only the first "n" subdomains of a file with the ```-n``` option.