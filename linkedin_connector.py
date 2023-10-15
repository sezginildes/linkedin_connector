import linkedin_connector_functions as lcf

lcf.connector_pipe_line(
    login_link="https://www.linkedin.com/comm/checkpoint/lg/otp-submit/flagship?sig=3vWfZeKsGyGGY1&submissionId=AgGYbBQwWeppCAAAAYsz2GFRkFvbR-2O2f3fLAxCxy1bW5hVNP-IEnt207DRUob4j_Tj6GY8AffLG4LKrFo5ZOWgkJUkoAovoyzo6A&loginToken=AQEQF9YuL3auKgAAAYsz2GHPlfWAAeMIDwW8E5CRJyyiPnvxcLvr6G10IUxHv36S1L-zrfwLJTSrkawNc7ZX7ZthJ9KZlGwHqnqABHA9ilehYflZXiI&session_redirect=%2Ffeed%2F%3FparentPageKey%3Dd_request-otp-generation&fromSignIn=true&midToken=AQEVPyWhQYLNGA&midSig=1vkLg3lSGyGGY1&trk=eml-email_security_one_time_sign_in_link_checkpoint-null-1-null&trkEmail=eml-email_security_one_time_sign_in_link_checkpoint-null-1-null-null-jvv8sn%7Elnrlcwro%7Ewu-null-neptune%2Fcheckpoint%7Eotp%7Esubmit%7Eflagship&lipi=urn%3Ali%3Apage%3Aemail_email_security_one_time_sign_in_link_checkpoint%3BUHFnwe4dSnifTolXMNSuBA%3D%3D",
    search_link="https://www.linkedin.com/search/results/people/?heroEntityKey=urn%3Ali%3Aorganization%3A17980339&keywords=i̇bn%20haldun%20üniversitesi&origin=SWITCH_SEARCH_VERTICAL&position=0&searchId=cb1d843f-6679-465a-aff5-10d4a042212d&sid=CiK", 
    PATH='chromedriver.exe', 
    message='chatgpt', 
    my_informations="None",
    openai_key="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",
    limit=100,
    headless=False)