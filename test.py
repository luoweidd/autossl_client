#!/usr/bin/python3
# _*_coding:utf8_*_

'''
 * Created with IntelliJ Pycharm.
 * Description:  
 * Project : autossl_client
 * Ide tools : PyCharm
 * File name : test.py
 * Author <a href="mailto:3245554@qq.com">罗卫</a>
 * User: devops
 * Date: 2019/7/26
 * Time: 上午10:42
'''

# from sysbase.confparser import configparser
#
# ll = configparser()
# ls = ll.confparser()
# print(ls)
# import re
# path = 'f:\\Windows\\ll\dsa'
# path1 = '/oot/afaosf/afasf'
# if re.match('^[C-Z,c-z]:\\\*\\\*', path):
#     print(True)
# else:
#     print(False)
# if re.match('^/*/*', path1):
#     print(True)
# else:
#     print(False)
# path = './sdfklasf/sajfkaslf'
# sub = re.sub('^\./','',path)
# print(sub)

# def test(fun):
#     if fun != None:
#         def test2():
#             print(fun.__name__,fun.__globals__)
#             data = fun()
#             return data
#         return test2
#
# @test
# def test3():
#     print(3)
#
# test3()


# data = {"heard":"root","msg":{"domain":"*.1a27d.cn","old_domain":"*.g8d6c.cn",
#                               "ca_key":"-----BEGIN CERTIFICATE----- MIIGTTCCBTWgAwIBAgISBGvaMrzEHX0HEo96dGwE41kaMA0GCSqGSIb3DQEBCwUAMEoxCzAJBgN"
#                                        "VBAYTAlVTMRYwFAYDVQQKEw1MZXQncyBFbmNyeXB0MSMwIQYDVQQDExpMZXQncyBFbmNyeXB0IEF1dGhvcml0eSBYMzAeFw0xOTA3MD"
#                                        "UwNzMxMjhaFw0xOTEwMDMwNzMxMjhaMBUxEzARBgNVBAMMCiouMWEyN2QuY24wggIiMA0GCSqGSIb3DQEBAQUAA4ICDwAwggIKAoICAQD"
#                                        "Orvg8UHBng3hvdxPDtjETHr72iA212YugDHZbalBlF6wKcuaFKmcdbwiZMQncI/GBk0hSzzLR43OUWLH1X3dW1GzwbpPobxCBcWMGAPsKR"
#                                        "+9HHyyQEimNqDPyFIg63IFCH/dHlmiVWb4NFAaVVPMZ3pt9RgRZsSg8CuGLme2zAkkME234y4wJXtuxsaxWsTXEejIFiNcotUDmuEUUWyTR"
#                                        "IdM2p4KrPeQ2Gr2OboZeb/ANeYTz+/eODKGEJkTbI+7pWNVCJUEnBJSd4WJ2FZwLQgGcD8P4QMS0Jr3y5IR3+/628O/JHttRrSy9tIhVTrt"
#                                        "zPFDYQoJ/SJB+v6HcwYP6yk+zZqlDvED35VDgPKRGya4AxC/iXnFsC8b4oOlwBEI7Y2ncrIkQCv/PBWA4R/J2bxrWReSe1cNj9le4X+S6O5KL"
#                                        "Iio8uVaMxVg72rgE9PBC9Vm/PoHgUZVul+0h8zFlzz2lbIpqnGNf9+CF+VdADvr7WPsQenktlolQG4JfzisewGIqhfmZauf+q8Yf+m6jM7/kxl"
#                                        "i1U9kF815Mq3v1tmPFAy5h0eXrQTaecTH4HOP0FvCosQBgpTNycaBCCpujUy8SJtVJ7/Wro6CoNesLgi9O/YxCQcKbNjXwQZbTorPdidVXI/XXw"
#                                        "7PU4Pjx9UruRayaFw6TEomm3VMUJrenZQIDAQABo4ICYDCCAlwwDgYDVR0PAQH/BAQDAgWgMB0GA1UdJQQWMBQGCCsGAQUFBwMBBggrBgEFBQcDA"
#                                        "jAMBgNVHRMBAf8EAjAAMB0GA1UdDgQWBBQyLnWwv9a86Kugjhga8iq6yf95BzAfBgNVHSMEGDAWgBSoSmpjBH3duubRObemRWXv86jsoTBvBggrBg"
#                                        "EFBQcBAQRjMGEwLgYIKwYBBQUHMAGGImh0dHA6Ly9vY3NwLmludC14My5sZXRzZW5jcnlwdC5vcmcwLwYIKwYBBQUHMAKGI2h0dHA6Ly9jZXJ0Lmlu"
#                                        "dC14My5sZXRzZW5jcnlwdC5vcmcvMBUGA1UdEQQOMAyCCiouMWEyN2QuY24wTAYDVR0gBEUwQzAIBgZngQwBAgEwNwYLKwYBBAGC3xMBAQEwKDAmBgg"
#                                        "rBgEFBQcCARYaaHR0cDovL2Nwcy5sZXRzZW5jcnlwdC5vcmcwggEFBgorBgEEAdZ5AgQCBIH2BIHzAPEAdwDiaUuuJujpQAnohhu2O4PUPuf+dIj7pI8o"
#                                        "kwGd3fHb/gAAAWvBQn4EAAAEAwBIMEYCIQCqLKprPzz84MpXoStlFnuLTOGXT1K/MTDNqE0OBMYuOgIhALubUD5rLjCHoh/DydhaMPC6evq9kQ6D/7/nosE"
#                                        "WssqzAHYAKTxRllTIOWW6qlD8WAfUt2+/WHopctykwwz05UVH9HgAAAFrwUKABQAABAMARzBFAiB5btLrihLzsMsVkGrTXm4JaDyEcFbHY74oy1B8BHaqyAI"
#                                        "hAJovv263EyVuZt3UE1JKrP6xr7u6vubxxLt9eT1DCrZKMA0GCSqGSIb3DQEBCwUAA4IBAQAXkm9uLqFdGcxVP3EI96ENAsZE5JFEPZQ9uqBeoRuqvEyNgjp22"
#                                        "7K4ieHY9iEiMjGhfEKH5SxEjPyghieScJGme++aLEqbwuPPDUKTmEXNyccPQbSu52AxwXCzsr5K84ReT/0GnpesHkuSlQ6vZ9G5VHwctgwsisYn4l+AZO1gCAH"
#                                        "nGNupgUl8EQ3qjAYBTmygh2reBXZ9HUcnhk6gi1yJjiPLTW1wj3dOvAghoVm31ub62XcxImfXkYJ0tV0uLUN7x3qVVkHq/ZQo7EZyWtGO5M1Uj+Cp4IxCeY/jXY"
#                                        "oq/g8k0Qgau6rdpW/rBVroUUW0JQrBq9Iqjbu92NnbHlk8-----END CERTIFICATE----- -----BEGIN CERTIFICATE-----MIIEkjCCA3qgAwIBAgIQCgFB"
#                                        "QgAAAVOFc2oLheynCDANBgkqhkiG9w0BAQsFADA/MSQwIgYDVQQKExtEaWdpdGFsIFNpZ25hdHVyZSBUcnVzdCBDby4xFzAVBgNVBAMTDkRTVCBSb290IENBIFg"
#                                        "zMB4XDTE2MDMxNzE2NDA0NloXDTIxMDMxNzE2NDA0NlowSjELMAkGA1UEBhMCVVMxFjAUBgNVBAoTDUxldCdzIEVuY3J5cHQxIzAhBgNVBAMTGkxldCdzIEVuY3"
#                                        "J5cHQgQXV0aG9yaXR5IFgzMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAnNMM8FrlLke3cl03g7NoYzDq1zUmGSXhvb418XCSL7e4S0EFq6meNQhY7L"
#                                        "EqxGiHC6PjdeTm86dicbp5gWAf15Gan/PQeGdxyGkOlZHP/uaZ6WA8SMx+yk13EiSdRxta67nsHjcAHJyse6cF6s5K671B5TaYucv9bTyWaN8jKkKQDIZ0Z8h/pZ"
#                                        "q4UmEUEz9l6YKHy9v6Dlb2honzhT+Xhq+w3Brvaw2VFn3EK6BlspkENnWAa6xK8xuQSXgvopZPKiAlKQTGdMDQMc2PMTiVFrqoM7hD8bEfwzB/onkxEz0tNvjj/P"
#                                        "Izark5McWvxI0NHWQWM6r6hCm21AvA2H3DkwIDAQABo4IBfTCCAXkwEgYDVR0TAQH/BAgwBgEB/wIBADAOBgNVHQ8BAf8EBAMCAYYwfwYIKwYBBQUHAQEEczBxMDI"
#                                        "GCCsGAQUFBzABhiZodHRwOi8vaXNyZy50cnVzdGlkLm9jc3AuaWRlbnRydXN0LmNvbTA7BggrBgEFBQcwAoYvaHR0cDovL2FwcHMuaWRlbnRydXN0LmNvbS9yb29"
#                                        "0cy9kc3Ryb290Y2F4My5wN2MwHwYDVR0jBBgwFoAUxKexpHsscfrb4UuQdf/EFWCFiRAwVAYDVR0gBE0wSzAIBgZngQwBAgEwPwYLKwYBBAGC3xMBAQEwMDAuBggr"
#                                        "BgEFBQcCARYiaHR0cDovL2Nwcy5yb290LXgxLmxldHNlbmNyeXB0Lm9yZzA8BgNVHR8ENTAzMDGgL6AthitodHRwOi8vY3JsLmlkZW50cnVzdC5jb20vRFNUUk9PV"
#                                        "ENBWDNDUkwuY3JsMB0GA1UdDgQWBBSoSmpjBH3duubRObemRWXv86jsoTANBgkqhkiG9w0BAQsFAAOCAQEA3TPXEfNjWDjdGBX7CVW+dla5cEilaUcne8IkCJLxWh"
#                                        "9KEik3JHRRHGJouM2VcGfl96S8TihRzZvoroed6ti6WqEBmtzw3Wodatg+VyOeph4EYpr/1wXKtx8/wApIvJSwtmVi4MFU5aMqrSDE6ea73Mj2tcMyo5jMd6jmeWU"
#                                        "HK8so/joWUoHOUgwuX4Po1QYz+3dszkDqMp4fklxBwXRsW10KXzPMTZ+sOPAveyxindmjkW8lGy+QsRlGPfZ+G6Z6h7mjem0Y+iWlkYcV4PIWL1iwBi8saCbGS5jN2p8M+X+Q7UNKEkROb3N6KOqkqm"
#                                        "57TH2H3eDJAkSnh6/DNFu0Qg== -----END CERTIFICATE-----","privte_key":"-----BEGIN RSA PRIVATE KEY----- MIIJKAIBAAKCAgEAzq74PFBwZ4N4b3cTw7YxEx6+9ogNtdmLoAx"
#                                                                                                            "2W2pQZResCnLmhSpnHW8ImTEJ3CPxgZNIUs8y0eNzlFix9V93VtRs8G6T6G8QgXFjBgD7CkfvRx8skBIpjagz8"
#                                                                                                            "hSIOtyBQh/3R5ZolVm+DRQGlVTzGd6bfUYEWbEoPArhi5ntswJJDBNt+MuMCV7bsbGsVrE1xHoyBYjXKLVA"
#                                                                                                            "5rhFFFsk0SHTNqeCqz3kNhq9jm6GXm/wDXmE8/v3jgyhhCZE2yPu6VjVQiVBJwSUneFidhWcC0IBnA/D+"
#                                                                                                            "EDEtCa98uSEd/v+tvDvyR7bUa0svbSIVU67czxQ2EKCf0iQfr+h3MGD+spPs2apQ7xA9+VQ4DykRsmuAM"
#                                                                                                            "Qv4l5xbAvG+KDpcARCO2Np3KyJEAr/zwVgOEfydm8a1kXkntXDY/ZXuF/kujuSiyIqPLlWjMVYO9q4BPT"
#                                                                                                            "wQvVZvz6B4FGVbpftIfMxZc89pWyKapxjX/fghflXQA76+1j7EHp5LZaJUBuCX84rHsBiKoX5mWrn/qvGH"
#                                                                                                            "/puozO/5MZYtVPZBfNeTKt79bZjxQMuYdHl60E2nnEx+Bzj9BbwqLEAYKUzcnGgQgqbo1MvEibVSe/1q6O"
#                                                                                                            "gqDXrC4IvTv2MQkHCmzY18EGW06Kz3YnVVyP118Oz1OD48fVK7kWsmhcOkxKJpt1TFCa3p2UCAwEAAQKC"
#                                                                                                            "AgA96P1km7e/2grGYMXj1vxGPOx4znJE6aBAVdtSMLtaPMgE7TwN4ZC3qV3K/Xx1m7Ko3KRKYdRYOKiTZ"
#                                                                                                            "CoSVQFbWhAzyPu3ISWxkHRYBQ0tnDSZekYP9dDKpPrCZdIUx55UX1zj7bLwIcyjAD+klaioNB0hXkrJTx69"
#                                                                                                            "NYkwFvCzsViOLHfBkb8lw2tNg+oaocR4UR4QuFey0vBY7BONMGwL1PT+pximEMj+R+5F7ueC/EbM0ny31N7"
#                                                                                                            "nhvMOsaPofJABB+IBiUVF2cJmtG+Y7YoreR8gTzylbUk+qWg2jKr9gddflzZMaVjK03PWc3BvFUFjGEsjLH"
#                                                                                                            "EIjYTy4pYqmTDd8WxOTIjLlt6+EKZ2RUS6XPmjfIrbFBbShj0+DlWv9+FUZtWFn6uupUZ1jDm83m1dQ7cGsR"
#                                                                                                            "dFfV6wQavwIm6Pqa2hyPEWwrzu3WvPpxXZFixL0MYIW01P34v8QA+jajZ3dAXzolDSb7A5TT7A8kSiSh8h/I"
#                                                                                                            "QJOQ1lr+hmYSAPxI4vfiPVDaRr6rBdCyPvweRuFp7s9yJC8AOlrzzMGulZL+vg1+z8q1JWf91OQyAhi5xYkqs"
#                                                                                                            "GoSwTzwcqRN3p+7HHSJUpdlC1doF/Uvj1DalzAXzIFm3/9dOjBr29fOd8Zaab/tLlusGgmAS8D0i/iHjXu8T/"
#                                                                                                            "k/+yaRmY3lBQ8/KftQKCAQEA1Q7QUlwBitBBPM7mNmpnaAYaRHt+pYHHhVM3deNK2RC4rrkCMe8A2oh3ulddBb"
#                                                                                                            "QD5GHc2B+lukADQlRZIXs9BK9KrVy7MB2pChQHus/mwvWW8GudJHwvzOi9px053gED2tQTTMjorq97izWrUF5"
#                                                                                                            "cVijchCN/oiJEvLnMSEPGb+McqVVsbQLUwAeA34e04wA9RPU32gYERnJi94oBqzQ3EpVCT+P3PaizWApR+o6Z2T"
#                                                                                                            "KPQt9sIoKYrMbb4si4ZMHkmWHm/SprHF5amWV2OOqtEMnrQX+SgGaEtlhkYir7Igeweylb07rY5WTVT1MnInk1JW"
#                                                                                                            "5JKB6JSkVZx3B8wzsGKwKCAQEA+FdBWhSv1G4vOftVYJJEPcf5Z8VLi70aM+iA0XbqlTxUoZmzTWzX7H9I9zFfV"
#                                                                                                            "PDs0pKNKgl7FnoptM5dUm7wWMNp5E0wvR1hDAtLIS2b61v+fLJx1y4w+6iqDfxDtTzhQCxI0cEN6abJX0Yjm9"
#                                                                                                            "80kFZWcOy4l3erw8IASnS4DsyoEQioiQP/RT903xnNOWmgJTW+g535W98ivnQ0kzc/PiQtZCzzKYp1z9nKBpaUZ"
#                                                                                                            "jnSfJH02AFIZJH4vX+yuxjIl8J5h9F/417nt8xFhy+lOmgYM16xm/2Y/eflytScJiGwgDsRqA3iMl0veteVa1z+e"
#                                                                                                            "x0i5msmL/ct7sLLftNQrwKCAQAZRd6URnGwY6+5ZNmODuUhQ8gN45BMVa6zNAHaLBIO2ZrurueBwNYbFiENq5tPN"
#                                                                                                            "+FWT/2AbZCdHUbFsXe5LwM38QsssVlLBdmtZl7cXBkFe1hiQIGteEW7SshkcGUS3o/0fz+i1hozzoEbLEycBfVyCvr"
#                                                                                                            "NeeCD/QimUmvXDqMVVp1pwMZR0AoolTtGSLS+UKLz8Rqk9B3BtYPj1S0Jf/IgdDAfhe0oFUDg6qh6zjuVthekWRhcp"
#                                                                                                            "50wsY4XwrOM0Csrvp9F3KhD/zVECPMTIVNSMIGFjXp1XLPVZXrS4kJT8RGQKoHIBdwAqgtbk4OK5VHWlNR8u9KRStS"
#                                                                                                            "xgbhq+C9tAoIBAQDqHaAPYwcrtcAx4h3nz5wjvh0CVf3VO62zF9IxJfEaRWjne7WMHTslyg0odFQSCJrKHLyVz6BJXV"
#                                                                                                            "tqB031A37zvy1Zu+dhsYumxhLKsWuXIv+z4KnvmK024heG3bWa60zSqazwiRYrmj+m4MF7FZ5BIBOXm6KdsISuJHsPt"
#                                                                                                            "h86XHdor4fqu2jwiFUOag2NvWTrD1KOU+QbVy0y7OwPiPrHA2YDVVjbZZuRGhkZwuUdxg8HvrVa2UK9BNvBEdyWA1Q/"
#                                                                                                            "tWfKwZbV68d4/0rgmesjN7Tw4KmBjD6pxu9cGrkmPYZeLNGFY6lFn5G+NfS35VBHEf2vyX2TpGuZ9evPoTkjAoIBABvJ"
#                                                                                                            "h4XBDoPc9rt8nzcGV6eqMdJayR2TF5DRo2HZdJ9pvd/SuOoUdSSDoOW39oWsHXFbakvnZzQ1BbX2iQH2hHgAK3FbZ07"
#                                                                                                            "Fnk8CJdlOQbSNQhbc4BKrth4bt6HXrtH76iJgtgYsZ/oc1+0gHc3H2QRFNiXs3rIOCGF/SpuHZZlSihoWzjNfqi/g2"
#                                                                                                            "4Pi1+rH0wXMWn+SVuSBfPTHM864jZHC4zacGpK2fUsH1tFHbedoTi/g9pgH9El2zyXDxR2rgm4JnmKsjHr4pgnbyqZD"
#                                                                                                            "oSFxon9doqwq9BdCp9rQODibmMLkO83m9F9gLyHqOiTV506TleH6rD4t8315P5tJUD4= -----END RSA PRIVATE "
#                                                                                                            "KEY-----"}}
#
# import json
# bdata =  bytes(json.dumps(data).encode('utf-8'))
# print(len(bdata))

