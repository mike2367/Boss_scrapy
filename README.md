# Boss_scrapy
Personal project of deploying an enterprice level web crawler using the scrapy frame.

## Target
The boss recruiting website, search for jobs in Shanghai, aquiring json API, job details are stored in mysql database through pipeline.</br></br>
original url: [https://www.zhipin.com/web/geek/job?city=101020100](https://www.zhipin.com/web/geek/job?city=101020100) </br></br>
<img src="https://github.com/user-attachments/assets/fb2c415a-bccd-40ce-80a4-05f78d03718a" width="310px" height="300px" class="alingright">
<img src="https://github.com/user-attachments/assets/8623b685-f8e9-42cb-b858-d3fdd7201b4b" width="310px" height="300px" class="alingright">


## Data segments
- job name </br>
- salary </br>
- required experience </br>
- required degree </br>
- brand name </br>
- area district </br>
- required skills </br>

## Running
### Run through the start.py in boss/other_src/start.py, which would start the crawler and check the current entries in the data base. </br>

## Content Including
- Scrapy frame </br>
- Pymysql </br>
- Mysql script </br>
- js reverse </br>

- ### Update: Due to the recent modification of zhipin.com, the original cookie generating js environment has lost efficacy, usage now requires manual input of personal __zp_token__, located in /boss/boss/middlewares.py. </br>
- ### Each __zp_token__ should provide 5 times of access. </br>
- ### Advices on the updated JS reverse are widely appreciated.
<img src="https://github.com/user-attachments/assets/4b1797e0-b0fa-4065-ab97-dfb0a579b53e"  width="500px" height="200px" class="center"> .
<img src="https://github.com/user-attachments/assets/afdf6490-4d9f-44c0-87ca-22d9414d8d16"  width="500px" height="200px" class="center"> .


