import yaml
import json
import pandas as pd
import xml.etree.ElementTree as ET
import codecs


class SaveData():

    def __init__(self):
        self.__fname = "test.yaml"
        self.__list_data = list()

    def get_data(self):
        return [
            {
                "field1": "data1",
                "field2": "data2",
                "field3": "data3",
                "field4": "data4",
            },
            {
                "field1": "data11",
                "field2": "data22",
                "field3": "data33",
                "field4": "data44",
            }
        ]

    def save_yaml(self, v_name):
        with open(v_name, "w") as file:
            yaml.dump(self.get_data(), file)

    def read_yaml(self, v_name):
        with open(v_name) as file:
            doc = yaml.load(file, Loader=yaml.FullLoader)
            print(doc)

    def save_json(self, v_name):
        with open(v_name, "w") as file:
            doc = json.dumps(self.get_data(), indent=4)
            file.write(doc)

    def read_json(self, v_name):
        with open(v_name) as file:
            doc = json.load(file)
            print(doc)

    def save_csv(self, v_name):
        df = pd.DataFrame(self.get_data())
        df.to_csv(v_name, index=False)

    def read_csv(self, v_name):
        doc = pd.read_csv(v_name)
        pd.re
        print(doc)

    def read_tms_cfg(self, v_name):

        # channels = pd.read_xml(v_name, iterparse={"CHANNEL": ["ChannelNum", "ChannelName"]})
        # print(channels)

        # rtus = pd.read_xml(v_name, iterparse={"RTU": ["RTUNum", "RTUName"]})
        # print(rtus)

        # statuses = pd.read_xml(v_name, iterparse={"STATUS": ["StatusName", "StatusPoint"]})

        # print(statuses)
        # statuses.to_csv('tms.csv', index=False)

        xml_data = codecs.open(v_name, 'r', 'utf-8').read()  # Read file
        root = ET.XML(xml_data)  # Parse XML

        names = list()
        addrs = list()
        matrix = list()

        channels = root.findall("CHANNEL")
        for ch in channels:
            ch_num = ch.get("ChannelNum")
            ch_name = ch.get("ChannelName")
            rtus = ch.findall("RTU")
            for rtu in rtus:
                rtu_num = rtu.get("RTUNum")
                rtu_name = rtu.get("RTUName")
                statuses = rtu.find("STATUSES")
                sts = statuses.findall("STATUS")
                for st in sts:
                    key_name = f'{ch_name} {rtu_name} {st.get("StatusName")}'
                    key_adr = f'{ch_num}:{rtu_num}:{st.get("StatusPoint")}'
                    key_matrix = st.get("StatusClass")
                    names.append(key_name)
                    addrs.append(key_adr)
                    matrix.append(key_matrix)

                analogs = rtu.find("ANALOGS")
                if analogs is not None:
                    ans = analogs.findall("ANALOG")
                    for an in ans:
                        key_name = f'{ch_name} {rtu_name} {an.get("AnalogName")}'
                        key_adr = f'{ch_num}:{rtu_num}:{an.get("AnalogPoint")}'
                        key_matrix = None
                        names.append(key_name)
                        addrs.append(key_adr)
                        matrix.append(key_matrix)

        #signals = {'addr_oik': addrs, 'name': names, 'matrix': matrix}

        empty_list = list()
        for i in range(len(names)):
            empty_list.append(None)

        signals = {
            'name': names,
            'ip': empty_list,
            'ld': empty_list,
            'ld_value_names': empty_list,
            'ld_value_tags': empty_list,
            'oik_addr': addrs,
            'attr_tmts': empty_list,
            'attr_rd_names': matrix,
        }

        df = pd.DataFrame(signals)
        df.to_csv('tms.csv', sep=";", index=True, index_label='index_column_tms')
        print(df)
        return df

    def read_hw_cfg(self, v_name):

        xml_data = codecs.open(v_name, 'r', 'utf-8').read()  # Read file
        root = ET.XML(xml_data)  # Parse XML

        name = []
        ip = []
        ld = []
        ld_value_names = []
        ld_value_tags = []
        attr_tmas = []
        attr_tmts = []
        attr_rd_names = []

        root = root.find("TMSTATION")
        tmd = root.find("TMD85000000")
        tmad = tmd.find("TMADAPT.24TcprawTCP_0")
        kps = tmad.findall("TMPORT.24Tcpraw")
        for kp in kps:
                kp_name = kp.get("BP.240RawName")
                ip_addr = kp.get("BP.240RawRemIpAddr")

                tmo_mms = kp.find("TMO_MMS850")
                tmo_104 = kp.find("TMO_IEC_870_5_104")

                if tmo_mms is not None:
                    try:
                        lds = tmo_mms.findall("I850LD")

                        for ld_el in lds:
                            ld_name = ld_el.get("i850LDName")
                            ld_st = ld_el.findall("I850ST")
                            ld_mmx = ld_el.findall("I850MX")
                            ld_co = ld_el.findall("I850CO")

                            for ld_s in ld_st:
                                ld_values = ld_s.findall("I850VALUE")

                                for ld_val in ld_values:
                                    ld_value_name = ld_val.get("i850VName")
                                    ld_value_tag = ld_val.get("i850VRdName")

                                    for attr in ld_val:
                                        attr_tma = attr.get("i850ATma")

                                        if attr_tma is not None:
                                            attr_tmt = attr.get("i850ATmt")
                                            attr_name = attr.get("i850AName")
                                            attr_rd_name = attr.get("i850ARdName")

                                            name.append(kp_name)
                                            ip.append(ip_addr)
                                            ld.append(ld_name)
                                            ld_value_names.append(f'{ld_name}/{ld_value_name}.{attr_name}')
                                            ld_value_tags.append(ld_value_tag)
                                            attr_tmas.append(attr_tma)
                                            attr_tmts.append(attr_tmt)
                                            attr_rd_names.append(attr_rd_name)
                            if ld_mmx is not None:
                                for ld_m in ld_mmx:
                                    ld_values = ld_m.findall("I850VALUE")

                                    for ld_val in ld_values:
                                        ld_value_name = ld_val.get("i850VName")
                                        ld_value_tag = ld_val.get("i850VRdName")

                                        for attr in ld_val:
                                            attr_tma = attr.get("i850ATma")

                                            if attr_tma is not None:
                                                attr_tmt = attr.get("i850ATmt")
                                                attr_name = attr.get("i850AName")
                                                attr_rd_name = attr.get("i850ARdName")

                                                name.append(kp_name)
                                                ip.append(ip_addr)
                                                ld.append(ld_name)
                                                ld_value_names.append(f'{ld_name}/{ld_value_name}.{attr_name}')
                                                ld_value_tags.append(ld_value_tag)
                                                attr_tmas.append(attr_tma)
                                                attr_tmts.append(attr_tmt)
                                                attr_rd_names.append(attr_rd_name)
                            if ld_co is not None:
                                for ld_c in ld_co:
                                    ld_values = ld_c.findall("I850VALUE")

                                    for ld_val in ld_values:
                                        ld_value_name = ld_val.get("i850VName")
                                        ld_value_tag = ld_val.get("i850VRdName")

                                        for attr in ld_val:
                                            attr_tma = attr.get("i850ATma")

                                            if attr_tma is not None:
                                                attr_tmt = attr.get("i850ATmt")
                                                attr_name = attr.get("i850AName")
                                                attr_rd_name = attr.get("i850ARdName")

                                                name.append(kp_name)
                                                ip.append(ip_addr)
                                                ld.append(ld_name)
                                                ld_value_names.append(f'{ld_name}/{ld_value_name}.{attr_name}')
                                                ld_value_tags.append(ld_value_tag)
                                                attr_tmas.append(attr_tma)
                                                attr_tmts.append(attr_tmt)
                                                attr_rd_names.append(attr_rd_name)

                    except Exception as e:
                        print(kp_name)
                        print(e)
                elif tmo_104 is not None:
                    try:
                        lds = tmo_104.findall("iec104Recv")

                        for ld_el in lds:
                            ld_st = ld_el.findall("iec101PrimAsdu")

                            for ld_s in ld_st:
                                asdu_num = ld_s.get("iec101PAAsduAddr")
                                stgs = ld_s.find("iec101PrimStg")

                                for st in stgs:
                                    st_tms_pt = st.get("iec101PVStTmsPt")

                                    if st_tms_pt is not None:
                                        st_tms_ch = st.get("iec101PVStTmsChn")
                                        st_tms_rtu = st.get("iec101PVStTmsRtu")
                                        st_tms_iec104 = st.get("iec101PVStAddr")

                                        name.append(kp_name)
                                        ip.append(ip_addr)
                                        ld.append(asdu_num)
                                        ld_value_names.append(None)
                                        ld_value_tags.append(None)
                                        attr_tma = f'{st_tms_ch}:{st_tms_rtu}:{st_tms_pt}'
                                        attr_tmas.append(attr_tma)
                                        attr_tmts.append('1 (ТС)')
                                        attr_iec104 = f'iec104addr={st_tms_iec104}'
                                        attr_rd_names.append(attr_iec104)

                    except Exception as e:
                        print(kp_name)
                        print(e)

                else:
                    print("беда с контроллером")



        vars = {
            'name': name,
            'ip': ip,
            'ld': ld,
            'ld_value_names': ld_value_names,
            'ld_value_tags': ld_value_tags,
            'oik_addr': attr_tmas,
            'attr_tmts': attr_tmts,
            'attr_rd_names': attr_rd_names,
        }
        df = pd.DataFrame(vars)
        print(df)
        df.to_csv('hw.csv', sep=";", index_label='index_column_hw')
        return df

        #
        #
        # for i, child in enumerate(root):
        #         data.append([child.text for child in child])
        #         cols.append(child.tag)
        # data.append([subchild.text for subchild in child])
        # cols.append(child.tag)

        # df = pd.DataFrame(data).T  # Write in DF and transpose it
        # df.columns = cols  # Update column names
        # print(df)


doc = SaveData()
# print('yaml file')
# doc.save_yaml('test_file.yaml')
# doc.read_yaml('test_file.yaml')
# print('json file')
# doc.save_json('test_file.json')
# doc.read_json('test_file.json')
# print('csv file')
# doc.save_csv('test_file.csv')
# doc.read_csv('test_file.csv')

df_tms = pd.DataFrame()
df_tms = doc.read_tms_cfg('tms.cfg')

df_hw = pd.DataFrame()
df_hw = doc.read_hw_cfg('hw.cfg')

df_result = pd.DataFrame()
df_result = df_hw.merge(df_tms, on='oik_addr', how="left")

groups = df_result.groupby(by='name_x')

with pd.ExcelWriter('groups.xlsx', engine='xlsxwriter') as writer:
    df_result.to_excel(writer, sheet_name='result', index=False, startrow=0, startcol=0)
    #df_tms.to_excel(writer, sheet_name='tms', index=False)
    #df_hw.to_excel(writer, sheet_name='hw', index=False)



#another_df.to_excel(writer,sheet_name='Validation',startrow=20, startcol=0)

#df_result.to_csv('oik_result.csv', index=False, sep=";")


