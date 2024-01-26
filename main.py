import finnhub
import app_config
import app_email

# Setup client
finnhub_client = finnhub.Client(api_key=app_config.FINN_KEY)
data = '' 

for s in app_config.SYMBOLS:
    try:
        data = finnhub_client.quote(s['sym'])
        if (data['c'] >= s['max']):
            # print('above max')
            msg = f"{s['sym']} at {data['c']} max of {s['max']}"
            if(app_config.ENV == 'PROD'):
                app_email.email(msg)
        if (data['c'] <= s['min']):
            #print('below min')
            msg = f"{s['sym']} at {data['c']} min of {s['min']}"
            if(app_config.ENV == 'PROD'):
                app_email.email(msg)
        # print(data['c'])
    except Exception as e:
        print("Error:", e)

exit()

