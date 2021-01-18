# shortyy

<img src="/assets/logo.png" width=10% height=10%>

[shortyy - A Brand URL Shortener Made Using Flask & PostgreSQL](https://shortyy.ml/)



## Features
- Open Source
- Free
- Alternative To Paid URL Shorteners
- 24/7 Runtime
- Secure
- Made In Python (Flask)
- Database Used - PostgreSQL
- A Dashboard



## Usage
- Clone The Repository On Your PC.

- Open PGAdmin4 (GUI) or PSQL (Shell) and create a new database and clone the database using Restore option, i.e, import the file shortyy (included in repository), this will create just the required table and schema inside the database without any data.

- Now Open `config.py`, change your admin username and password. This will allow you to get access to dashboard which you can use to manage your URLs. 

- Most Importantly in `config.py` add your Database URI there in the format `db_engine://db_username:db_password@db_host:db_port/db_name`, here we are using PostgreSQL so you can do something like this, taking these as db parameters - `db_user - postgres`, `db_password - test123`, `db_host - localhost`, `db_port - 5432`, `db_name - urlshortener`:
     **postgres://postgres:test123@localhost:5432/urlshortener**
     
- Install Requirements: Open your terminal and enter: `pip install -r requirements.txt`

- Host The Flask App: (Debug Environment - Run `python app.py`) (Production Environment - WSGI Script [Surf The Web For Tutorials]).



## Contributing
- Contributions are accepted but follow the common ethics and principles while contributing. Contributions must not contain spams, malicious contents, NSFW things, etc.



## Contributors - Awesome Contributors Of This Project (Check Them Out)
- Rudransh Joshi - [FireHead90544](https://github.com/FireHead90544) {Developer}
- Knoxo - [Knoxo](https://github.com/Knoxo) {Contributor}


## LICENSE
- This project and repository has been licensed under **GNU General Public License v3.0**, LICENSE can be found **[here](https://github.com/FireHead90544/shortyy/blob/main/LICENSE)** + You can use this anywhere but you must provide its source and give credits to this repository.



## Future Plans
- We are planning to add an API related system which you can use to add or delete links to the database using GET/POST/DELETE etc. requests, so if you want to contribute, it will be highly appreciated.



## Special Thanks To [Cyber Efficient](https://www.cyberefficient.io/) For Supporting This Project Which Made It Possibe To Host It.



# THANK YOU
### ~ Rudransh Joshi
