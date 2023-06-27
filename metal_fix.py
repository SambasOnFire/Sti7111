import serial
import time
s = serial.Serial("/dev/ttyUSB0", 115200, write_timeout=0.5)

time.sleep(2.0)
s.write(b"poke fe24e678 00D05B15\n")
s.write(b"poke FE24F6D4 008C06FE\n")
s.write(b"poke FE24F6D8 00741CE0\n")
s.write(b"poke FE24F6DC 00751CE7\n")
s.write(b"poke FE24F6E0 00761CEE\n")
time.sleep(2.0)
s.write(b"poke FE24F6E4 00771CF5\n")
s.write(b"poke FE24F6E8 00144001\n")
s.write(b"poke FE24F6EC 00155009\n")
s.write(b"poke FE24F6F0 00166011\n")
s.write(b"poke FE24F6F4 00177019\n")
time.sleep(2.0)
s.write(b"poke FE24F6F8 0001043C\n")
s.write(b"poke FE24F6FC 00211500\n")
s.write(b"poke FE24F700 00211600\n")
s.write(b"poke FE24F704 00211700\n")
s.write(b"poke FE24F708 00840D00\n")
time.sleep(2.0)
s.write(b"poke FE24F70C 00741C20\n")
s.write(b"poke FE24F710 00751C21\n")
s.write(b"poke FE24F714 00761C22\n")
s.write(b"poke FE24F718 00771C23\n")
s.write(b"poke FE24F71C 00155008\n")
time.sleep(2.0)
s.write(b"poke FE24F720 00166010\n")
s.write(b"poke FE24F724 00177018\n")
s.write(b"poke FE24F728 0001043C\n")
s.write(b"poke FE24F72C 00211500\n")
s.write(b"poke FE24F730 00211600\n")
time.sleep(2.0)
s.write(b"poke FE24F734 00211700\n")
s.write(b"poke FE24F738 00840D00\n")
s.write(b"poke FE24F73C 00FA4000\n")
s.write(b"poke FE24F740 000F033C\n")
s.write(b"poke FE24F744 008E15D1\n")
time.sleep(2.0)
s.write(b"poke FE24F748 00D00004\n")
s.write(b"poke FE24F74C 000F003C\n")
s.write(b"poke FE24F750 008E15D4\n")
s.write(b"poke FE24F754 00040F3C\n")
s.write(b"poke FE24F758 00050F3C\n")
time.sleep(2.0)
s.write(b"poke FE24F75C 00060F3C\n")
s.write(b"poke FE24F760 00070F3C\n")
s.write(b"poke FE24F764 00840D00\n")
s.write(b"poke FE24F768 00F54000\n")
s.write(b"poke FE24F76C 000F033C\n")
time.sleep(2.0)
s.write(b"poke FE24F770 008D85DC\n")
s.write(b"poke FE24F774 00D00004\n")
s.write(b"poke FE24F778 000F003C\n")
s.write(b"poke FE24F77C 008D85DF\n")
s.write(b"poke FE24F780 00040F3C\n")
time.sleep(2.0)
s.write(b"poke FE24F784 00050F3C\n")
s.write(b"poke FE24F788 00060F3C\n")
s.write(b"poke FE24F78C 00070F3C\n")
s.write(b"poke FE24F790 00840D00\n")
s.write(b"poke FE24F794 00A30069\n")
time.sleep(2.0)
s.write(b"poke FE24F798 00D00090\n")
s.write(b"poke FE24F79C 00233200\n")
s.write(b"poke FE24F7A0 00F00000\n")
s.write(b"poke FE24F7A4 00D00090\n")
s.write(b"poke FE24F7A8 00D00090\n")
time.sleep(2.0)
s.write(b"poke FE24F7AC 00AF0068\n")
s.write(b"poke FE24F7B0 000F033C\n")
s.write(b"poke FE24F7B4 000F043C\n")
s.write(b"poke FE24F7B8 000F053C\n")
s.write(b"poke FE24F7BC 000F063C\n")
time.sleep(2.0)
s.write(b"poke FE24F7C0 000F073C\n")
s.write(b"poke FE24F7C4 00D00090\n")
s.write(b"poke FE24F7C8 00D00090\n")
s.write(b"poke FE24F7CC 00840D00\n")
s.write(b"poke FE24F7D0 00E600FF\n")
time.sleep(2.0)
s.write(b"poke FE24F7D4 00E50000\n")
s.write(b"poke FE24F7D8 00756210\n")
s.write(b"poke FE24F7DC 00FA4000\n")
s.write(b"poke FE24F7E0 000F053C\n")
s.write(b"poke FE24F7E4 008E15F9\n")
time.sleep(2.0)
s.write(b"poke FE24F7E8 00AF0050\n")
s.write(b"poke FE24F7EC 00AF0051\n")
s.write(b"poke FE24F7F0 00AF0052\n")
s.write(b"poke FE24F7F4 00AF0053\n")
s.write(b"poke FE24F7F8 008E15FE\n")
time.sleep(2.0)
s.write(b"poke FE24F7FC 00B0F054\n")
s.write(b"poke FE24F800 00B0F055\n")
s.write(b"poke FE24F804 00B0F056\n")
s.write(b"poke FE24F808 00B0F057\n")
s.write(b"poke FE24F80C 00840D00\n")
time.sleep(2.0)
s.write(b"poke FE24F810 00E00000\n")
s.write(b"poke FE24F814 00E00000\n")
s.write(b"poke FE24F818 00E00000\n")
s.write(b"poke FE24F81C 00ED0609\n")
s.write(b"poke FE24F820 008C05F4\n")
time.sleep(2.0)
s.write(b"poke FE24F824 00ED060C\n")
s.write(b"poke FE24F828 00A30064\n")
s.write(b"poke FE24F82C 008C05CF\n")
s.write(b"poke FE24F830 00ED060F\n")
s.write(b"poke FE24F834 00A30065\n")
time.sleep(2.0)
s.write(b"poke FE24F838 008C05CF\n")
s.write(b"poke FE24F83C 00B04058\n")
s.write(b"poke FE24F840 00B05059\n")
s.write(b"poke FE24F844 00B0605A\n")
s.write(b"poke FE24F848 00B0705B\n")
time.sleep(2.0)
s.write(b"poke FE24F84C 00ED0616\n")
s.write(b"poke FE24F850 00A30065\n")
s.write(b"poke FE24F854 008C05DA\n")
s.write(b"poke FE24F858 00B0405C\n")
s.write(b"poke FE24F85C 00B0505D\n")
time.sleep(2.0)
s.write(b"poke FE24F860 00B0605E\n")
s.write(b"poke FE24F864 00B0705F\n")
s.write(b"poke FE24F868 008C0701\n")
s.write(b"poke FE24F86C 00AB006A\n")
s.write(b"poke FE24F870 00E00000\n")
time.sleep(2.0)
s.write(b"poke FE24F874 00010B3C\n")
s.write(b"poke FE24F878 00ED0620\n")
s.write(b"poke FE24F87C 008C05B6\n")
s.write(b"poke FE24F880 00E23464\n")
s.write(b"poke FE24F884 00A4006E\n")
time.sleep(2.0)
s.write(b"poke FE24F888 00A5006E\n")
s.write(b"poke FE24F88C 00A6006E\n")
s.write(b"poke FE24F890 0007013C\n")
s.write(b"poke FE24F894 00ED0627\n")
s.write(b"poke FE24F898 008C05E5\n")
time.sleep(2.0)
s.write(b"poke FE24F89C 00ED062A\n")
s.write(b"poke FE24F8A0 00A30067\n")
s.write(b"poke FE24F8A4 008C05CF\n")
s.write(b"poke FE24F8A8 00ED062D\n")
s.write(b"poke FE24F8AC 00A30065\n")
time.sleep(2.0)
s.write(b"poke FE24F8B0 008C05CF\n")
s.write(b"poke FE24F8B4 00A30058\n")
s.write(b"poke FE24F8B8 00E00000\n")
s.write(b"poke FE24F8BC 003BB001\n")
s.write(b"poke FE24F8C0 0098161B\n")
time.sleep(2.0)
s.write(b"poke FE24F8C4 00344300\n")
s.write(b"poke FE24F8C8 009C161D\n")
s.write(b"poke FE24F8CC 0021B001\n")
s.write(b"poke FE24F8D0 00ED0636\n")
s.write(b"poke FE24F8D4 008C05B6\n")
time.sleep(2.0)
s.write(b"poke FE24F8D8 00A3006C\n")
s.write(b"poke FE24F8DC 00E00000\n")
s.write(b"poke FE24F8E0 00333100\n")
s.write(b"poke FE24F8E4 0098161B\n")
s.write(b"poke FE24F8E8 00B01060\n")
time.sleep(2.0)
s.write(b"poke FE24F8EC 00B01054\n")
s.write(b"poke FE24F8F0 008C0703\n")
s.write(b"poke FE24F8F4 00AB006A\n")
s.write(b"poke FE24F8F8 00E00000\n")
s.write(b"poke FE24F8FC 00010B3C\n")
time.sleep(2.0)
s.write(b"poke FE24F900 00ED0642\n")
s.write(b"poke FE24F904 008C05B6\n")
s.write(b"poke FE24F908 00E23468\n")
s.write(b"poke FE24F90C 00A4006E\n")
s.write(b"poke FE24F910 00A5006E\n")
time.sleep(2.0)
s.write(b"poke FE24F914 00A60060\n")
s.write(b"poke FE24F918 0007013C\n")
s.write(b"poke FE24F91C 00ED0649\n")
s.write(b"poke FE24F920 008C05E5\n")
s.write(b"poke FE24F924 00ED064C\n")
time.sleep(2.0)
s.write(b"poke FE24F928 00A30067\n")
s.write(b"poke FE24F92C 008C05CF\n")
s.write(b"poke FE24F930 00ED064F\n")
s.write(b"poke FE24F934 00A30065\n")
s.write(b"poke FE24F938 008C05CF\n")
time.sleep(2.0)
s.write(b"poke FE24F93C 00A30059\n")
s.write(b"poke FE24F940 00E00000\n")
s.write(b"poke FE24F944 003BB001\n")
s.write(b"poke FE24F948 0098163D\n")
s.write(b"poke FE24F94C 00355300\n")
time.sleep(2.0)
s.write(b"poke FE24F950 009C163F\n")
s.write(b"poke FE24F954 0021B001\n")
s.write(b"poke FE24F958 00ED0658\n")
s.write(b"poke FE24F95C 008C05B6\n")
s.write(b"poke FE24F960 00A3006C\n")
time.sleep(2.0)
s.write(b"poke FE24F964 00E00000\n")
s.write(b"poke FE24F968 00333100\n")
s.write(b"poke FE24F96C 0098163D\n")
s.write(b"poke FE24F970 00B01061\n")
s.write(b"poke FE24F974 00B01054\n")
time.sleep(2.0)
s.write(b"poke FE24F978 008C0705\n")
s.write(b"poke FE24F97C 00AB006A\n")
s.write(b"poke FE24F980 00E00000\n")
s.write(b"poke FE24F984 00010B3C\n")
s.write(b"poke FE24F988 00ED0664\n")
time.sleep(2.0)
s.write(b"poke FE24F98C 008C05B6\n")
s.write(b"poke FE24F990 00E2346C\n")
s.write(b"poke FE24F994 00A4006E\n")
s.write(b"poke FE24F998 00A50060\n")
s.write(b"poke FE24F99C 00A60061\n")
time.sleep(2.0)
s.write(b"poke FE24F9A0 0007013C\n")
s.write(b"poke FE24F9A4 00ED066B\n")
s.write(b"poke FE24F9A8 008C05E5\n")
s.write(b"poke FE24F9AC 00ED066E\n")
s.write(b"poke FE24F9B0 00A30067\n")
time.sleep(2.0)
s.write(b"poke FE24F9B4 008C05CF\n")
s.write(b"poke FE24F9B8 00ED0671\n")
s.write(b"poke FE24F9BC 00A30065\n")
s.write(b"poke FE24F9C0 008C05CF\n")
s.write(b"poke FE24F9C4 00A3005A\n")
time.sleep(2.0)
s.write(b"poke FE24F9C8 00E00000\n")
s.write(b"poke FE24F9CC 003BB001\n")
s.write(b"poke FE24F9D0 0098165F\n")
s.write(b"poke FE24F9D4 00366300\n")
s.write(b"poke FE24F9D8 009C1661\n")
time.sleep(2.0)
s.write(b"poke FE24F9DC 0021B001\n")
s.write(b"poke FE24F9E0 00ED067A\n")
s.write(b"poke FE24F9E4 008C05B6\n")
s.write(b"poke FE24F9E8 00A3006C\n")
s.write(b"poke FE24F9EC 00E00000\n")
time.sleep(2.0)
s.write(b"poke FE24F9F0 00333100\n")
s.write(b"poke FE24F9F4 0098165F\n")
s.write(b"poke FE24F9F8 00B01062\n")
s.write(b"poke FE24F9FC 00B01054\n")
s.write(b"poke FE24FA00 008C0707\n")
time.sleep(2.0)
s.write(b"poke FE24FA04 00AB006A\n")
s.write(b"poke FE24FA08 00E00000\n")
s.write(b"poke FE24FA0C 00010B3C\n")
s.write(b"poke FE24FA10 00ED0686\n")
s.write(b"poke FE24FA14 008C05B6\n")
time.sleep(2.0)
s.write(b"poke FE24FA18 00E23470\n")
s.write(b"poke FE24FA1C 00A40060\n")
s.write(b"poke FE24FA20 00A50061\n")
s.write(b"poke FE24FA24 00A60062\n")
s.write(b"poke FE24FA28 0007013C\n")
time.sleep(2.0)
s.write(b"poke FE24FA2C 00ED068D\n")
s.write(b"poke FE24FA30 008C05E5\n")
s.write(b"poke FE24FA34 00ED0690\n")
s.write(b"poke FE24FA38 00A30067\n")
s.write(b"poke FE24FA3C 008C05CF\n")
time.sleep(2.0)
s.write(b"poke FE24FA40 00ED0693\n")
s.write(b"poke FE24FA44 00A30065\n")
s.write(b"poke FE24FA48 008C05CF\n")
s.write(b"poke FE24FA4C 00A3005B\n")
s.write(b"poke FE24FA50 00E00000\n")
time.sleep(2.0)
s.write(b"poke FE24FA54 003BB001\n")
s.write(b"poke FE24FA58 00981681\n")
s.write(b"poke FE24FA5C 00377300\n")
s.write(b"poke FE24FA60 009C1683\n")
s.write(b"poke FE24FA64 0021B001\n")
time.sleep(2.0)
s.write(b"poke FE24FA68 00ED069C\n")
s.write(b"poke FE24FA6C 008C05B6\n")
s.write(b"poke FE24FA70 00A3006C\n")
s.write(b"poke FE24FA74 00E00000\n")
s.write(b"poke FE24FA78 00333100\n")
time.sleep(2.0)
s.write(b"poke FE24FA7C 00981681\n")
s.write(b"poke FE24FA80 00B01063\n")
s.write(b"poke FE24FA84 00B01054\n")
s.write(b"poke FE24FA88 008C0709\n")
s.write(b"poke FE24FA8C 00AC006B\n")
time.sleep(2.0)
s.write(b"poke FE24FA90 00E00000\n")
s.write(b"poke FE24FA94 0078CC80\n")
s.write(b"poke FE24FA98 0079CC84\n")
s.write(b"poke FE24FA9C 007ACC88\n")
s.write(b"poke FE24FAA0 007BCC8C\n")
time.sleep(2.0)
s.write(b"poke FE24FAA4 0001083C\n")
s.write(b"poke FE24FAA8 00ED06AC\n")
s.write(b"poke FE24FAAC 008C05C3\n")
s.write(b"poke FE24FAB0 0008013C\n")
s.write(b"poke FE24FAB4 0001093C\n")
time.sleep(2.0)
s.write(b"poke FE24FAB8 00ED06B0\n")
s.write(b"poke FE24FABC 008C05C3\n")
s.write(b"poke FE24FAC0 0009013C\n")
s.write(b"poke FE24FAC4 00010A3C\n")
s.write(b"poke FE24FAC8 00ED06B4\n")
time.sleep(2.0)
s.write(b"poke FE24FACC 008C05C3\n")
s.write(b"poke FE24FAD0 000A013C\n")
s.write(b"poke FE24FAD4 00010B3C\n")
s.write(b"poke FE24FAD8 00ED06B8\n")
s.write(b"poke FE24FADC 008C05C3\n")
time.sleep(2.0)
s.write(b"poke FE24FAE0 000B013C\n")
s.write(b"poke FE24FAE4 00A3006D\n")
s.write(b"poke FE24FAE8 00A40060\n")
s.write(b"poke FE24FAEC 00A50061\n")
s.write(b"poke FE24FAF0 00A60062\n")
time.sleep(2.0)
s.write(b"poke FE24FAF4 00A70063\n")
s.write(b"poke FE24FAF8 00444300\n")
s.write(b"poke FE24FAFC 00455300\n")
s.write(b"poke FE24FB00 00466300\n")
s.write(b"poke FE24FB04 00477300\n")
time.sleep(2.0)
s.write(b"poke FE24FB08 00544800\n")
s.write(b"poke FE24FB0C 00555900\n")
s.write(b"poke FE24FB10 00566A00\n")
s.write(b"poke FE24FB14 00577B00\n")
s.write(b"poke FE24FB18 00B04060\n")
time.sleep(2.0)
s.write(b"poke FE24FB1C 00B05061\n")
s.write(b"poke FE24FB20 00B06062\n")
s.write(b"poke FE24FB24 00B07063\n")
s.write(b"poke FE24FB28 00E23470\n")
s.write(b"poke FE24FB2C 00ED06CD\n")
time.sleep(2.0)
s.write(b"poke FE24FB30 008C05E5\n")
s.write(b"poke FE24FB34 00ED06D0\n")
s.write(b"poke FE24FB38 00A30067\n")
s.write(b"poke FE24FB3C 008C05DA\n")
s.write(b"poke FE24FB40 00ED06D3\n")
time.sleep(2.0)
s.write(b"poke FE24FB44 00A30065\n")
s.write(b"poke FE24FB48 008C05DA\n")
s.write(b"poke FE24FB4C 00A8005C\n")
s.write(b"poke FE24FB50 00A9005D\n")
s.write(b"poke FE24FB54 00AA005E\n")
time.sleep(2.0)
s.write(b"poke FE24FB58 00AB005F\n")
s.write(b"poke FE24FB5C 003CC001\n")
s.write(b"poke FE24FB60 00344800\n")
s.write(b"poke FE24FB64 009C16A5\n")
s.write(b"poke FE24FB68 00355900\n")
time.sleep(2.0)
s.write(b"poke FE24FB6C 009C16A5\n")
s.write(b"poke FE24FB70 00366A00\n")
s.write(b"poke FE24FB74 009C16A5\n")
s.write(b"poke FE24FB78 00377B00\n")
s.write(b"poke FE24FB7C 009C16A5\n")
time.sleep(2.0)
s.write(b"poke FE24FB80 00A40060\n")
s.write(b"poke FE24FB84 00A50061\n")
s.write(b"poke FE24FB88 00A60062\n")
s.write(b"poke FE24FB8C 00A70063\n")
s.write(b"poke FE24FB90 00B04054\n")
time.sleep(2.0)
s.write(b"poke FE24FB94 00B05055\n")
s.write(b"poke FE24FB98 00B06056\n")
s.write(b"poke FE24FB9C 00B07057\n")
s.write(b"poke FE24FBA0 008C070B\n")
s.write(b"poke FE24FBA4 00A40060\n")
time.sleep(2.0)
s.write(b"poke FE24FBA8 00A50061\n")
s.write(b"poke FE24FBAC 00A60062\n")
s.write(b"poke FE24FBB0 00A70063\n")
s.write(b"poke FE24FBB4 00FA4000\n")
s.write(b"poke FE24FBB8 00AF0066\n")
time.sleep(2.0)
s.write(b"poke FE24FBBC 008E16EF\n")
s.write(b"poke FE24FBC0 000F043C\n")
s.write(b"poke FE24FBC4 000F053C\n")
s.write(b"poke FE24FBC8 000F063C\n")
s.write(b"poke FE24FBCC 000F073C\n")
time.sleep(2.0)
s.write(b"poke FE24FBD0 008E16F4\n")
s.write(b"poke FE24FBD4 00040F3C\n")
s.write(b"poke FE24FBD8 00050F3C\n")
s.write(b"poke FE24FBDC 00060F3C\n")
s.write(b"poke FE24FBE0 00070F3C\n")
time.sleep(2.0)
s.write(b"poke FE24FBE4 00B04054\n")
s.write(b"poke FE24FBE8 00B05055\n")
s.write(b"poke FE24FBEC 00B06056\n")
s.write(b"poke FE24FBF0 00B07057\n")
s.write(b"poke FE24FBF4 008C070D\n")
time.sleep(2.0)
s.write(b"poke FE24FBF8 00E00000\n")
s.write(b"poke FE24FBFC 00E00000\n")
s.write(b"poke FE24FC00 008C0607\n")
s.write(b"poke FE24FC04 00E00000\n")
s.write(b"poke FE24FC08 008C061B\n")
time.sleep(2.0)
s.write(b"poke FE24FC0C 00E00000\n")
s.write(b"poke FE24FC10 008C063D\n")
s.write(b"poke FE24FC14 00E00000\n")
s.write(b"poke FE24FC18 008C065F\n")
s.write(b"poke FE24FC1C 00E00000\n")
time.sleep(2.0)
s.write(b"poke FE24FC20 008C0681\n")
s.write(b"poke FE24FC24 00E00000\n")
s.write(b"poke FE24FC28 008C06A3\n")
s.write(b"poke FE24FC2C 00E00000\n")
s.write(b"poke FE24FC30 008C06E9\n")
time.sleep(2.0)
s.write(b"poke FE24FC34 00B0007F\n")
s.write(b"poke FE24FC38 00D01A12\n")
s.write(b"poke FE24C180 00000000\n")
s.write(b"poke FE24C184 00000000\n")
s.write(b"poke FE24C188 00000000\n")
time.sleep(2.0)
s.write(b"poke FE24C18C 00000000\n")
s.write(b"poke FE24C190 15000001\n")
s.write(b"poke FE24C194 FFFF1500\n")
s.write(b"poke FE24C198 FFFF0000\n")
s.write(b"poke FE24C19C FFFF1400\n")
time.sleep(2.0)
s.write(b"poke FE24C1A0 23104022\n")
s.write(b"poke FE24C1A4 FE248000\n")
s.write(b"poke FE24C1A8 0FFFFFFF\n")
s.write(b"poke FE24C1AC 0000FFFF\n")
s.write(b"poke FE24C1B0 FEFEFEFE\n")
time.sleep(2.0)
s.write(b"poke FE24C1B4 FEFEFEFE\n")
s.write(b"poke FE24C1B8 11223344\n")
s.write(b"poke FE24C138 624d6153\n")
s.write(b"poke fe24c13C 21217341\n")
time.sleep(2.0)
s.write(b"poke FE24C140 ecwpk \n")
s.write(b"poke FE24C144 ecwpk  \n")
s.write(b"poke FE24C148 ecwpk  \n")
s.write(b"poke FE24C14C ecwpk  \n")
time.sleep(2.0)
s.write(b"poke FE24C01C 00000005\n")
s.write(b"poke FE24DE1C 01000000\n")
s.write(b"display FE24C140\n")


























































































































































































































































































































































































