import base64

# The Base64-encoded data as a string
encoded_data = """SFJDVEZ7SDFEMW45
X2ZsNDk1XzFuXzFu
bjBWNDcxdjNfdzRZ
Mn0=Q3liZXIgU2Vj
dXJpdHk6IEhhY2tS
dXNoQ1RGIFtDXQoJ
U3Rha2Vob2xkZXI6
IE5pc2hhbnQgVGF0
YXIKClRoaXMgY2F0
ZWdvcnkgaW50cm9k
dWNlcyB5b3UgdG8g
dGhlIHdvcmxkIG9m
IEhhY2tpbmcgYW5k
IEN5YmVyU2VjLiBJ
ZiB5b3UgYXJlIGlu
dGVyZXN0ZWQgaW4g
ZGV2ZWxvcGluZyBh
IGRlZXBlciB1bmRl
cnN0YW5kaW5nIGFi
b3V0IENvbXB1dGVy
cywgaG93IGF0dGFj
a2VycyBsZXZlcmFn
ZSB2dWxuZXJhYmls
aXRpZXMgYW5kIGhv
dyB0byBhdm9pZCB0
aGVtLCB0aGlzIGV2
ZW50IGlzIGZvciB5
b3UuIFRoZSB0eXBl
cyBvZiBjaGFsbGVu
Z2VzIHdpbGwgcmFu
Z2UgZnJvbSBjcnlw
dG9ncmFwaHksIHBv
a2luZyBob2xlcyBp
biByYW5kb20gcGFy
dHMgb2YgdmFyaW91
cyBzb2Z0d2FyZXMs
IGFuZCBleHBsb3Jp
bmcgdGhlIHdvcmxk
IG9mIGNvbXB1dGVy
IGFwcGxpY2F0aW9u
cy4KCkhhY2tSdXNo
Q1RGIHdpbGwgYmUg
YSAzNi1ob3VyIEpl
b3BhcmR5LXN0eWxl
IENhcHR1cmUgdGhl
IEZsYWcgKENURikg
ZXZlbnQuIFlvdXIg
bWFpbiBnb2FsIGlz
IHRvIGNvbGxlY3Qg
YXMgbWFueSBmbGFn
cyBhcyBwb3NzaWJs
ZS4gQnV0IHdhaXQs
IHdoYXQgaXMgYSBD
VEY/IApSZWZlciBo
ZXJlOiBodHRwczov
L2N0ZmQuaW8vd2hh
dHMtYS1jdGYvIAoK
SGFja1J1c2hDVEYg
aXMgYmVnaW5uZXIg
ZnJpZW5kbHkgaS5l
LiB5b3UgZG9u4oCZ
dCBuZWVkIHRvIGhh
dmUgYW55IHByaW9y
IGtub3dsZWRnZSBp
biB0aGlzIGZpZWxk
IHRvIHBhcnRpY2lw
YXRlLiBUaGUgb25s
eSBwcmVyZXF1aXNp
dGUgaXMgYW4gaW50
ZXJlc3QgaW4gbGVh
cm5pbmcuIFlvdXIg
Z3JlYXRlc3QgdG9v
bCBpcyBnb29nbGUv
YmluZy9xdWFudC9z
dGFydHBhZ2Uoc2hh
bWVsZXNzIHBsdWdz
IGZvciBvdGhlciBw
cml2YWN5IGZvY3Vz
ZWQgc2VhcmNoIGVu
Z2luZXMpLiBZb3Ug
YXJlIGZyZWUgdG8g
dXNlIENoYXRHUFQg
YXMgd2VsbCwgdGhv
dWdoIG9ubHkgYmVj
YXVzZSBJIGhhZCB0
byBtYWtlIHF1ZXN0
aW9ucyB0aGF0IGl0
IGNvdWxkbuKAmXQg
c29sdmUgYnkgaXRz
ZWxmKGhlcmXigJlz
IHRvIGhvcGluZyku
CgpBY2Nlc3MgdGhl
IENoYWxsZW5nZXMg
aGVyZTogZGFzaGxh
bmRlci5tZQpQbGVh
c2Ugc3VibWl0IHlv
dXIgd3JpdGV1cHMg
aGVyZToge2dvb2ds
ZSBmb3JtLCBtdXN0
IHN1Ym1pdCBnaXRo
dWIgcmVwb3N9CgpG
bGFnIGZvcm1hdDog
SFJDVEZ7Kn0KClBs
ZWFzZSBqb2luIHRo
ZSBkaXNjb3JkIHNl
cnZlciBpZiB5b3Xi
gJlyZSBpbnRlcmVz
dGVkIGluIHRoZSBw
cm9ibGVtOiAKCllv
dXIgc3VibWlzc2lv
biBvZiBmbGFncyB3
aWxsIG9ubHkgYmUg
Y29uc2lkZXJlZCB2
YWxpZCBpZiB5b3Ug
cHJvdmlkZSBhIHdy
aXRldXAgb2YgdGhl
IHNvbHV0aW9uIG9m
IHRoZSBjaGFsbGVu
Z2UuIEEgd3JpdGV1
cCBpbmNsdWRlcyBh
IHN5c3RlbWF0aWMg
d2F5IG9mIGhvdyB5
b3Ugc29sdmVkIHRo
ZSBjaGFsbGVuZ2Us
IHdoYXQgdGhpbmdz
IHdvcmtlZCBmb3Ig
eW91LCB3aHkgZGlk
IHRoZXkgd29yaywg
YW55IGRpZmZpY3Vs
dGllcyB0aGF0IHlv
dSBmYWNlZCBldGMu
IEhlcmUgYXJlIHNv
bWUgb2YgdGhlIHdy
aXRldXBzIHByb3Zp
ZGVkIGZvciBwYXN0
IENURnMgY29uZHVj
dGVkLgpodHRwczov
L2dpdGh1Yi5jb20v
cHJhdHl1c2gzNzU3
L2lpdGduLXRlY2gt
Y291bmNpbC1jdGYt
d3JpdGV1cHMKaHR0
cHM6Ly9naXRodWIu
Y29tL0RldXMxNzA0
L1FDVEZfU29sdXRp
b25zCgoKQXQgdGhl
IGVuZCBvZiB0aGUg
aGFja2F0aG9uLCB5
b3UgYXJlIHN1cHBv
c2VkIHRvIGdpdmUg
YSBwcmVzZW50YXRp
b24gdGhhdCB3aWxs
IGluY2x1ZGUgdGhl
IGZvbGxvd2luZzoK
ClRoZSB3cml0ZSB1
cHMgb2YgYWxsIHRo
ZSBjaGFsbGVuZ2Vz
IHRoYXQgeW91IHNv
bHZlZApVbnN1Y2Nl
c3NmdWwgYXR0ZW1w
dHMgYXQgc29sdmlu
ZyBhIGNoYWxsZW5n
ZS4gVGhlIGFwcHJv
YWNoZXMgdGhhdCB5
b3UgY29uc2lkZXJl
ZCwgd2h5IGl0IGRp
ZCBub3Qgd29yayBl
dGMuCllvdXIgbGVh
cm5pbmdzLgpUaGUg
RmxhZ3MgdGhhdCB5
b3Ugd2VyZSBhYmxl
IHRvIGFjaGlldmUK
ClRoZSBwcmVzZW50
YXRpb24gc2hvdWxk
IHN1bW1hcml6ZSBh
bGwgdGhlIHdvcmsg
ZG9uZSBieSB5b3Vy
IHRlYW0gZHVyaW5n
IHRoZSBldmVudCB0
aW1lIGZyYW1lLgoK
SW1wb3J0YW50IElu
c3RydWN0aW9uOgoK
VGhpcyBldmVudCBh
c2tzIHlvdSB0byBw
ZXJmb3JtIGF0dGFj
a3MsIHdpdGggb3Vy
IHBlcm1pc3Npb24s
IGFnYWluc3QgYSBz
ZXQgb2YgdGFyZ2V0
cyB0aGF0IHdlIGFy
ZSBwcm92aWRpbmcg
Zm9yIHRoaXMgcHVy
cG9zZS4gQXR0ZW1w
dGluZyB0aGUgc2Ft
ZSBraW5kcyBvZiBh
dHRhY2tzIGFnYWlu
c3Qgb3RoZXIgc3lz
dGVtcyB3aXRob3V0
IGF1dGhvcml6YXRp
b24gaXMgcHJvaGli
aXRlZCBieSBsYXcg
YW5kIGluc3RpdHV0
aW9uIHBvbGljaWVz
LiBZb3UgbXVzdCBu
b3QgYXR0YWNrIGFu
eSBzeXN0ZW0gd2l0
aG91dCBhdXRob3Jp
emF0aW9uISBZb3Ug
YXJlIHJlcXVpcmVk
IHRvIHJlc3BlY3Qg
dGhlIHByaXZhY3kg
YW5kIHByb3BlcnR5
IHJpZ2h0cyBvZiBv
dGhlcnMgYXQgYWxs
IHRpbWVzLgoKICAg
ICAgICAgKioqTWFr
ZSBzdXJlIHRoYXQg
eW91IGFncmVlIHRv
IHRoZXNlIHRlcm1z
IGJlZm9yZSB5b3Ug
YmVnaW4geW91ciB3
b3JrLioqKgoKCkhl
cmUgYXJlIHNvbWUg
cmVzb3VyY2VzIHRv
IGdldCB5b3Ugc3Rh
cnRlZDoKaHR0cHM6
Ly9jdGYxMDEub3Jn
LwpodHRwczovL3d3
dy55b3V0dWJlLmNv
bS9jaGFubmVsL1VD
bGNFLWtWaHF5aUhD
Y2pZd2NwZmo5dyAo
bGl2ZW92ZXJmbG93
KQpodHRwczovL3Bp
Y29jdGYub3JnL3Jl
c291cmNlcyAKCg=="""

another_encoded_data = """16f5b795773092f9f1f99331527270d41912f9d954111979523b19105b573273d3159351f3d1b3d17211bb51b8f91991d9f13918f1331918f1d999731918f31910d97390d11971b0d39118f332f111b15151121152f9b2197338d8f97332f1121193b352b3b11151b133b15353b2d2d152d2fb121351b2f3149351b4535351b1b13212db12f978d9f97959b8f972f33353345339dffffffffff"""

encoded_data = encoded_data.replace("\n", "").replace(" ", "")
decoded_data = base64.b64decode(encoded_data)
print(decoded_data)

another_encoded_data = another_encoded_data.replace("\n", "").replace(" ", "")
decoded_data = base64.b64decode(another_encoded_data)
print(decoded_data)
