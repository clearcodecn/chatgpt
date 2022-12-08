from chatgpt.main import Chatbot
from flask import Flask
from flask import request, jsonify


config = {
    "email": "735416909@qq.com",
    "password": "735416909@qq.com",
    "proxy": "http://127.0.0.1:1081",
    'session_token':'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..jZy5YipXX01Bs9-V.Byx-dpPcBRrlYRrhIN_svNnPEbQoNiQxbDmF-vpnzeWLocymuB11DX6uwkn_jsheVHUQtdefV8lrG7PvF4c4hW_h6C_mbnihOHE3my9eh81fiyEsT8u07EozwEFw33lJbM0m9dqDYsatFOo3x73ku5P7uyHZ4c9EtrXwDsHICDV33j1Nz5ya94sJ5lVe7OSUIVt1RiUYo8Gr2DRBPywy6hwnfZkepefjK-1RT-cAHCrQmnZMDoy8OwANh1ilsbAbT8fwkP4i6-NbxB5hRVtss1MfjNjbpbOLdAAEM7EOSSueP38PkVYGKobMQ1vhro6XZKAjPjfrPqJBxabXdw1Z0louc4tclte_j4fgktH0TCwhOH_BlFU01knbV2V8Laeq6vFLb1X16i0zKfmcHE4Vs0mBHiPkKTlubJiQY1oYVOwiqGSYZchZYWEw_GscJa7SqT12B-AShe-10LSjnrczjQJpxKF8FrH0aNObTwST80DxrL6ZChNljn0PLHCWU0O-_fDJEfsqXOhfORLxwXhMhrWaCRspigGGhPh5K_aocaLTvoNxlTz_G9eQVMODKbvYxHKkaD7u_HrvOvv94hEoCN5PayrhKJiYI6BPkB041j4pdb2FMXpbSNxBdJcgztmWYZyE0OWXUq5uodvY3sfIV0dh1DsGfF-0BsWyt_cZc64DLCCYCRPCQnpBW2bRUfEfmuJp_l0pnko_kQazhCTvsEXPJg0QoTmzEl-JuVMQzcbjfQy2Aa4sKZlA83G_1DKh3b-sCLGUmiRSkiZvD272HFW5DGZ28ErN9qiDmG2cV5hbysM6HnoeMWM7lVRLVUuzvI5Ps7hlAeQLrZ4tB7ykW_2bTOwLukpAromiwHFdSKleEwc4EFrN3xe4me8zihpnHD6qvJjR9F8xKG0D387qAOOk1ovifYWwt7q53QfO-U1IU2YtDAkFc_yZiuGqUCuXC2sDC0ZfpdjS_BQBBgZBrscGeODJp1s6vC3ImGM-7UTIT5zUC2mzx2pAovPqM7N3cHOdYJ04fH612CrFc45oMtDkEdkwPSQl-9ZSavga7miousiS31AlKr8NVJvKBHNys8z4RVuL_deSzKomg-_az-gQO7V3vx02qY0AVJ5tpXihNgq77qZZo1lZMWZewc7s_LMI87amoJtLLE6VSIB637Tfs1SZXmGHnHqY_VwOf24pc7EBkzB48n7VSqSnSVG0h_k6_0P9zwjYrVzq-fX6ylK8hFZdeYMJ6-vkhMRqAclh2eMHQ0zt2Z9N-2bRQLvnAjs4cU1C5rR5ImeR1uPkOUkCMtdcPshcrQBfZJmb596nLj7B9uoq-9lfTgvrul7MR0OgaXa903zcw_rBs2Z2xe712umMAQyqy2XGkFtXHKh3OLTnfVSD_6wR5KXKJ2JxpJaEP-aoSWzH4GmLkF5J7g-Fx6-hlAwshHMnnPinX00PUZXEf21cCyUkGXJ4NXuGcYRm6zwaIq2muU9GPBkP_KS5MMf7I95iQjBYlSBLgvSFBvqxtCc53Q3D_km8vp-JWd_5AXQtLt1kVGWpdDYGos1JqOP5ubiMqEymJ4KX83-X3xsJ7hUKcH0SKVcbt78HgS05bKd4m30Sk1sgpKGWTnD-AapMd3AoOftAsUgxpzgScCbG5VzELcwKW-GPIGWmuyEUS4nwVXu09omKgdUbk3-Uxo536-mQKDixzjDEzalSLlIq-Rfh1m7fA5YWmc9avcACAExDdVf5om6bYTH5JpJpKGg67945OnBZ8vJ9lrLnghjIQcm_AVRxiWkY0nkc6lD_wzTzV8yath6ynq8n_EcWJdukkg5hXuuaibZJaTuvwQty9lIyQbzRzuMXMwr7zywCzpxlF-HNW7y7ff98GiNgl5BFGg0fvwgi2946dI46q1tO3tshRmI-Xzbn2kCYvJB8ZJaV42oX9--v734GswHzPmqbvtsE15YlD4JIl1pTIpN4x3jRfIvHo-UuCEkC9FyRF3eQlKnUdcWG7iNDRnmnaq7CFT3qivPUECxCZRwaOVfe-9uRr8XDbMO_OcE3hT1VUNle-JlIJB2WhQRYyUcyHw5pTpFAXe57zIlKqjBlVXzYi4nshJQoDHKLNGuN45Cky2H1M4OI6xSbZUT8mvdliQZKlNxBmjjAh5QIFwE29W0yvcyh0lKy2lkKgJ0KbsN-KotoFWJUfTDQVyDSFOLba_6S-nt-Zutbl9uTNjUVsb2Gctb1b8-wptRVvq7sza8buEsAcOju8n9xYr0mLeLgYDTdjBTCsMUvwkQOc7uggxPlqTgIfa5n7otQaMkLGmCdASSbcBfUXNDnspcQ3pFxj5li.d928UBC3KL9J_jCJpd1EGQ',
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
    return jsonify(code=200, status=0, message='ok', data={
        'a': msg, 
        'q': q, 
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0')