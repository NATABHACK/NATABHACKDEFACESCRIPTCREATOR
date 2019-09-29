import base64, codecs
magic = 'IyEvdXNyL2Jpbi9weXRob24NCiMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjDQojICBodHRwczovL3d3dy55b3V0dWJlLmNvbS9jaGFubmVsL1VDS3NlVzVRWXpjdzROU1NTcDViYkQ2ZyAgIw0KIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMNCm1lc3MgPSAiIiI9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT0NCiAgICAgICAgICAgICBEZWZhY2UgU2NyaXB0IENyZWF0b3IgICAgICAgIA0KICAgICAgICAgICAgICAgICBCeSBOQVRBQiBIQUNLDQo9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT0iIiINCg0KcHJpbnQgbWVzcw0KcHJpbnQgIkNyZWF0ZWQgYnkgTkFUQUIgSEFDSyINCnRpdGxlID0gcmF3X2lucHV0KCJUaXRsZTogIikNCmhlYWRpbmcgPSByYXdfaW5wdXQoIkhhY2tlZCBieTogIikNCmltYWdlbGluayA9IHJhd19pbnB1dCgiSW1hZ2UgTGluayAobWlkZGxlKTogIikNCmJnaW1hZ2UgPSByYXdfaW5wdXQoIkltYWdlIExpbmsgKGJhY2tncm91bmQpOiAiKQ0KbWVzc2FnZSA9IHJhd19pbnB1dCgiTWVzc2FnZS4gVXNlPGJyPiBmb3IgdGhlIG5leHQgdGV4dDogIikNCnRleHRjb2xvciA9IHJhd19pbnB1dCgiVGV4dCBDb2xvdXIgKEV4YW1wbGU9UmVkKTogIikNCnlvdXR1YmVpZCA9IHJhd19pbnB1dCgiWW91dHViZSBMaW5rIChNdXNpYyk6ICIpDQoNCg0KI09wZW4gdGhlIGluZGV4DQpmbyA9IG9wZW4oIm5hdGFiaGFjay5odG1sIiwidyIpDQoNCm1lc3NhZ2VzY3JpcHQxID0gIiIiPGh0bWw+PGhlYWQ+PHRpdGxlPiIiIg0KDQptZXNzYWdlc2NyaXB0MiA9IHRpdGxlDQoNCm1lc3NhZ2VzY3JpcHQzID0gIiIiPC90aXRsZT48L2hlYWQ+DQo8Ym9keT4NCjxicj4NCjxsaW5rIGhyZWY9J2h0dHA6Ly9mb250cy5nb29nbGVhcGlzLmNvbS9jc3M/ZmFtaWx5PU'
love = '9lLzy0pz9hBwpjZPptpzIfCFqmqUyfMKAbMJI0WlO0rKOyCFq0MKu0Y2Amplp+QDb8oTyhnlObpzIzCFqbqUEjBv8iMz9hqUZhM29iM2kyLKOcpl5wo20iL3AmC2MuoJyfrG1OoaEiovptpzIfCFqmqUyfMKAbMJI0WlO0rKOyCFq0MKu0Y2Amplp+QDb8oTyhnlObpzIzCFqbqUEjBv8iMz9hqUZhM29iM2kyLKOcpl5wo20iL3AmC2MuoJyfrG1Xo3AyMzyhVSAuoaZaVUWyoQ0ap3E5oTImnTIyqPptqUyjMG0aqTI4qP9wp3ZaCt0XCTWiMUxtLzqwo2kipw0vVmNjZQNjZPVtLzSwn2qlo3IhMPN9VvVvQDbAPz1yp3AuM2ImL3WcpUD0VQ0tLzqcoJSaMD0XQDcgMKAmLJqyp2AlnKO0AFN9VPVvVw48MTy2VTAfLKAmCFqQMJ50MKWRnKLaCt0XCTAyoaEypw4APwkbZG48L2IhqTIlCwkzo250VTAioT9lCIjvpzIxKPVtMzSwMG1CpzWcqUWiow4vVvVAPt0XoJImp2SaMKAwpzyjqQLtCFObMJSxnJ5aQDbAPz1yp3AuM2ImL3WcpUD3VQ0tVvVvCTtkCwjiMz9hqQ4APwkcoJptp3WwCFVvVvNAPt0XoJImp2SaMKAwpzyjqQttCFOcoJSaMJkcozfAPt0XoJImp2SaMKAwpzyjqQxtCFNvVvVtq2yxqTt9AQHjpUttnTIcM2u0CGZ0ZUO4Ct0XCTWiMUxto25fo2SxCFWcozy0XPxvCwjiLz9xrG4APwkvo2E5Ct0XCTEcqvOcMQ0vLaIfoTHvCwjiMTy2CvVvVt0XQDcgMKAmLJqyp2AlnKO0ZGNtCFNvVvVAPwkmL3WcpUDtoTShM3IuM2H9KPWXLKMuH2AlnKO0KPV+QDc2LKVtnG0jQDc2LKVtnw0jQDc2LKVtqTI4qTIBEFjtLJMznJAbMD0XqzSlVUEyrUEyCIjvCTWlCwkvpw48LaV+CTWlCwkvpw48Mz9hqPOzLJAyCH9lLzy0pz9hVTAioT9lCFVvVt0XQDcgMKAmLJqyp2AlnKO0ZGRtCFO0MKu0L29fo3VAPt0XoJImp2SaMKAwpzyjqQRlVQ0tVvVvVUAcrzH9AQ4vVvVAPt0XoJImp2SaMKAwpzyjqQRmVQ0toJImp2SaMFNAPt0XoJImp2SaMKAwpzyjqQR0VQ0tVvVvCTWlCwkvpw48Y2Mi'
god = 'bnQ+PGJyPjwvYj48L2Rpdj5cIg0KdmFyIGllID0gKGRvY3VtZW50LmFsbCk7DQp2YXIgbmUgPSAoZG9jdW1lbnQubGF5ZXJzKTsgDQpmdW5jdGlvbiBpbml0KCl7DQp0ZXh0ZU5FPScnOw0KbWFjaGluZV9hX2VjcmlyZSgpOw0KfQ0KZnVuY3Rpb24gbWFjaGluZV9hX2VjcmlyZSgpew0KdGV4dGVORT10ZXh0ZU5FK3RleHRlLmNoYXJBdChpKQ0KYWZmaWNoZT0nPGZvbnQgZmFjZT1PcmJpdHJvbiBzaXplPTEgY29sb3I9I2ZmZmZmZj48c3Ryb25nPk1lc3NlbmdlIDogJyt0ZXh0ZU5FKyc8L3N0cm9uZz48L2ZvbnQ+Jw0KaWYgKHRleHRlLmNoYXJBdChpKT09IjwiKSB7DQpqPTENCn0NCmlmICh0ZXh0ZS5jaGFyQXQoaSk9PSI+Iikgew0Kaj0wDQp9DQppZiAoaj09MCkgew0KaWYgKGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKSB7IC8vIGF2ZWMgaW50ZXJuZXQgZXhwbG9yZXINCmRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCJidWxsZSIpLmlubmVySFRNTCA9IGFmZmljaGU7DQp9DQp9DQppZiAoaTx0ZXh0ZS5sZW5ndGgtMSl7DQppKysNCnNldFRpbWVvdXQoIm1hY2hpbmVfYV9lY3JpcmUoKSIsNzApDQp9DQplbHNlDQpyZXR1cm4NCn0NCjwvc2NyaXB0Pjxmb250IGZhY2U9Ik9yYml0cm9uIiBzaXplPSIxIj48Ymxpbms+PHNwYW4gc3R5bGU9ImNvbG9yOiByZ2IoMjU1LCAyNTUsIDI1NSk7Ij48Yj48Zm9udCBjb2xvcj1saW1lIHNpemU9ND48L2ZvbnQ+PC9iPjwvdT48L2JsaW5rPjxicj48L2ZvbnQ+PC9iPg0KPGEgaHJlZj0iL2luZGV4LnBocCI+PGltZyBzdHlsZT0icG9zaXRpb246Zml4ZWQ7Ym90dG9tOjBweDt6LWluZGV4OjEwMDA7cmlnaHQ6LTEwcHg7IiAgc3JjPSJodHRwOi8vc3RhdGljMS5zcXVhcmVzcGFjZS5jb20vc3RhdGljLzU3MDZjMTIwMDdlYWEwYjgyMzk5NjYwZC81NzA2YzY4YmYwYmMzMzk4N2NhZTZjNzEvNTc3ZDVjNWQzN2M1ODFmZD'
destiny = 'OyZwIwZGOvYmR0Awx3ZGp3ZQH2ZQtinJ5mqJk0YGR0AGR0Zy8kZwtjYaOhMlVtqUyjMG0vnJ1uM2HiM2yzVvO3nJE0nQ0vZGHjVw48Y2R+CP9vo2E5Ct0XCPRgYFOQH1ZtYF0+CUA0rJkyCt0XYxAyoaEypxEcqag3nJE0nQb2AGOjrQgvo3WxMKV6ZKO4VPAzMwNjZQNtp29fnJD7pTSxMTyhMmb1pUt7oJSlM2yhBwOjrPOuqKEiBlOvLJAeM3WiqJ5xBvO1pzjbW2u0qUN6Yl9cYzygM3IlYzAioF9mETWuGKAKYzqcMvpcB30APwjip3E5oTH+QDb8LaV+QDb8LaV+QDb8LaV+QDb8nJMlLJ1yVUqcMUEbCFVjVvObMJyanUD9VwNvVUAlLm0vnUE0pQbiY3q3ql55o3I0qJWyYzAioF92YlVvVt0XQDcgMKAmLJqyp2AlnKO0ZGHtCFO5o3I0qJWynJDAPt0XoJImp2SaMKAwpzyjqQR2VQ0tVvVvWzS1qT9joTS5CGRvVTMlLJ1yLz9lMTIlCFVjVw48Y2yzpzSgMG4vVvVAPt0XQDczol53pzy0MFugMKAmLJqyp2AlnKO0ZFxAPzMiYaqlnKEyXT1yp3AuM2ImL3WcpUDlXD0XMz8hq3WcqTHboJImp2SaMKAwpzyjqQZcQDczol53pzy0MFugMKAmLJqyp2AlnKO0APxAPzMiYaqlnKEyXT1yp3AuM2ImL3WcpUD1XD0XMz8hq3WcqTHboJImp2SaMKAwpzyjqQLcQDczol53pzy0MFugMKAmLJqyp2AlnKO0AlxAPzMiYaqlnKEyXT1yp3AuM2ImL3WcpUD4XD0XMz8hq3WcqTHboJImp2SaMKAwpzyjqQxcQDczol53pzy0MFugMKAmLJqyp2AlnKO0ZGNcQDczol53pzy0MFugMKAmLJqyp2AlnKO0ZGRcQDczol53pzy0MFugMKAmLJqyp2AlnKO0ZGVcQDczol53pzy0MFugMKAmLJqyp2AlnKO0ZGZcQDczol53pzy0MFugMKAmLJqyp2AlnKO0ZGDcQDczol53pzy0MFugMKAmLJqyp2AlnKO0ZGHcQDczol53pzy0MFugMKAmLJqyp2AlnKO0ZGLcQDbAPaOlnJ50VPWGL3WcpUDtGJSenJ5aVSA1L2Imp2M1oTjuVt0XpUWcoaDtVyA1LaAwpzyvMFN6VR5OIRSPVRuOD0fvQDbAPzMiYzAfo3AyXPx='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))