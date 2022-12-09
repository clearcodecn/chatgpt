from chatgpt.main import Chatbot
from flask import Flask
from flask import request, jsonify


config = {
    "email": "735416909@qq.com",
    "password": "735416909@qq.com",
#    "proxy": "http://127.0.0.1:1081",
    'session_token':'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..nNeQV6slXVSrcIpr.z5S7vab559sM9XWkqu0EQCY65nQ00iW6MTEZ_Q4kj3pIOx5mRYhLWTrPvOJOHswB6G0BPMesMGq28xjZ1wai3nOYg7q6FYiGX0pQCxVrPZV1skiCanGwZpiV_7cE-d2BwrDjz9HW431hEUXS5yHUPG_NHW2kwizuzGAN0bSNRYjAlZ7mOLyDlWmeXjMOgrvfa27XbhEkU2UyPF56C1BS6W6fyJQeAgzdYxBnE24Mngsc-un3imETktrOWgyYHxjihADUJ_Et9lLhOg1kBzMDIsnV5AugO1oSaEjBjV2LCgTEcQ9MEhKxQwCORx2P38itqbuGTl-ND4e-NQSboNyXbMGSlGh1VmFKZ9rot0Xd9TqgzeCI6VUZgDFqTwdosdKmBZAX-eoElxbEEnbzBrurOiXJJ_JssFzC9BnT5jckr4A71PMVW0z9jOQT848_sI42dS4CipcnHylfm_tL0BLt1gLYexOMtKU3p1rBR39yL5F5yqchpzlQsTl8gAgkTf7BWKFwoPLpXG62-FxfsOfclW1bRdpxCGLzgkQtnk7rF6xuz2p-ChXO-3FjcEl60fMxRrvj36DVNElbJh2dHBQbBeLWEY0VJWwQWKPQlbSz1uqDdJiMTmicuNcSA1jYsnb688HaQhvveBEuHjbKbXzJl8Cd7QT9xxty-Bhs6iveEArmiIIYOnrMP5FWhhC40ZFAMHWgyMsdgBvn6JRirXcZpP7_RIAYB07V0xxwID73l7nWqTXVi3ikTB8k__Zj6Z85U1PlOqpJdmGwKuI9iPP28tpt6PJaPOzOTvIq9j4_3lYsX5PsiDpvxTPho3v57b-4NHIOeyvhz0ktLbpoPGog2HVzZq7ftoqUzpHsa-JGWF_y1Abj15Ar8yvyYBRTd1w5sFi-wp-pWOxpUwimg4ahOEOysEPLqTPEOfcR0BfZPHKaJAAupuStMndo48TQf0M_zwImIKbq7-XqvRQWC1nA96iERgXiqQ4m3ygx6n_hOTDBVn4A34cveh-L-t7zb8FwL13rpy5jboWbuslc5xtOkkXkyrsHyeZJlTayAYJo9-ftcI4sXbUL79s_PTdekdHZAiLVY5T2mbnfGx6BOay0PyOD03KMw0eEbsJ9SKgjkNuTlj82TPj2WGzTdxHCJRgr0y4bvwuj1b0S5ck0G2BiwH0VJ4PFRDVx_kP3zSP-xfHd-fPJirm5gQ-b-wmi4KbqFEiP8fGJLk6WJW9jN3-Txxigc-226mFvP3ACQrXV_p9NyyuvTh-7P88hI9BlgqNneUO3BsHJAAXDDAi9wmYxOopMAMeByKnQHBIN-3Sp7sua2Ahr17nZqVI3z1wKqkP62XWHDcoZdtLn5aeNHMeQ0wcv6gaWgOaENXofKvJicYmh8sLnZsHm0uIdNlgfny1Bzyy-6yCQg3SdVju28GlVrjBJCabnDRd26fwopKnnyX_9l6An4RyXNO5HNWhgegvDYVnwEOorMi4k2hjOGhEjFsbfZYl0MBprYNWFDDQj0pQ6vuf0Sem8ojPFDlcy7kC7sxF4m_MbhsAoEYaOE_0E51hxoS2WcTY9uN4P7ok8boufiJ-HFea0Czp9UhODRj6xXlyhgPhfm96k8uHodIn2Fcdw7NEBwVGbGxeCJ4I-hyapvSBlH-XHLHspdHDzcJ9j7p5253M9ida1KrERt0F5x84_rv7nH4mHDbt564yNpxd-Br29m0sO_bLDwka9BzrlzSpFizxXEy2zWB7VEPP246dt41UA24F4ocqQ_ND91hVWmJmHggu-SvLI_gLrH_Gasqm9-K4DNC6w5wp1pAFqRJTplq5qDu1KIgKzwwBn31WO63OKqT-P9UcHTCeu4ujuYMPFeqIUsZcPjUSztxgwLS9zaqlYMa_KSD9FuJ-TSiVgdvLIvXzvjMPK8n0hOZByexF57MpoiPOdp1kV1o63fv3B1tjDsBQivBZFf64u0Kx3BoMWqELQe6GklGKnahAYk3qhNBnijjzNs4xuOwQqLqCNU6TTgAiSiBkXcBQAZlnVQzxs3A74uzk3AS2PrXFA-biVea9zIES5LFZbWHUOdNesYADpaN5AbxqRCflWf1EmAA_RDCfZv4urqBrktdJcZk5ETSjF5tdWK4A4_qV3lJNBvIumDOkzKvC5XCIxoLJzi3ypI5oHkfmTsxeY4uVWxQmuTeSfYdnXTCQduee8wFLLAbLZ7lmPFked6bOsQukeYmnoHQICMmJSEdROOMQupE0dEP6HUkbYCeRDgcpS1RaWRyW3VP3adETsmcfIIYjokPNZtsrFuZDmDvnPjd95f5RIUK_q5SWdfFtecMCAKtSkVL7Z.aoxZOAnA8g2fl8odYYKbgw',
}
chatbot = Chatbot(config, conversation_id=None)

def getMessage(q = '') :
    print('q = ', q)
    resp = chatbot.get_chat_response(q, output='text')
    print('a = ', resp['message'])
    return resp['message'] 



app = Flask(__name__)

@app.route("/api", methods=['POST'])
def hello_world():
    q = request.json['q']
    msg = getMessage(q = q)
    if '抱歉' in msg :
        msg = ''
    return jsonify(code=200, status=0, message='ok', data={
        'a': msg, 
        'q': q, 
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0')
