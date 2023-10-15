import linkedin_connector_functions as lcf

lcf.connector_pipe_line(
    login_link="https://www.linkedin.com/comm/checkpoint/lg/otp-submit/flagship?sig=05tbiKv7sMGGY1&submissionId=AgENaUfwq1xLAgAAAYszcIMGHKjQTCvRl-GzBZpyD9kEVQsaqIHDZWaHw2bF9vNlCZkU2ux2Ocdgw_LAzp3SxwaGJVWSHIrTk05e7g&loginToken=AQHIIr_K6lPodgAAAYszcIOnr2iaLGORloZm71SH2ZGRVDlYXqooHjytEABe_UbHOvHD4K-nK8ossHS_UL0Vd5NAm00KCW0wHQbxJ60MaRUM4A_XxyI&session_redirect=%2Ffeed%2F%3FparentPageKey%3Dd_request-otp-generation&fromSignIn=true&midToken=AQEAqebx11W4jw&midSig=2gb2R-m7EMGGY1&trk=eml-email_security_one_time_sign_in_link_checkpoint-null-1-null&trkEmail=eml-email_security_one_time_sign_in_link_checkpoint-null-1-null-null-c6ljey%7Elnrhb0e5%7E9m-null-neptune%2Fcheckpoint%7Eotp%7Esubmit%7Eflagship&lipi=urn%3Ali%3Apage%3Aemail_email_security_one_time_sign_in_link_checkpoint%3BK%2FljdyiISAe47dB3fLih%2FA%3D%3D",
    search_link="https://www.linkedin.com/search/results/people/?geoUrn=%5B%22101282230%22%5D&keywords=data%20scientist&origin=FACETED_SEARCH&searchId=498aa9be-2ccb-4a87-a5ac-8d1ce11f8b42&sid=klL", 
    PATH='chromedriver.exe', 
    message='chatgpt', 
    my_informations="\n- Working as Data Scientist\n- Doing masters at Big Data\n- Doing traineeship at BME\n- My name: Talha",
    openai_key="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",
    limit=100,
    headless=False)