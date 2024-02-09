import streamlit as st
import matplotlib.pyplot as plt, seaborn as sea


def pertanyaan1_10122104(order_items):
    st.write("<h4>Kategori barang apa yang paling banyak dibeli?<h4>", unsafe_allow_html=True)
    categories_count = order_items["product_category_name"].value_counts()

    with st.container():
        myexplode = [0.2 ,0 ,0 ,0 ,0 ,0 ,0]
    plt.pie(categories_count.head(7).values, labels = categories_count.head(7).keys(), explode=myexplode, shadow=True, colors=sea.color_palette('Set3'), autopct='%1.2f%%', startangle=90)
    plt.title(label="Kategori Produk yang paling banyak di pesan")
    grafik1 = plt.gcf()
    plt.close()
    st.pyplot(grafik1)

    del grafik1
    with st.expander("Kesimpulan"):
        st.write("Maka dari hasil diatas\
                 Kategori Produk yang sering dipesan adalah bed_bath_table.")

def pertanyaan2_10122104(delivered_orders):
    st.write("<h4>Apakah barang yang datang ke costumer melebihi tanggal estimasinya dapat mempengaruhi pembatalan pesanan?<h4>", unsafe_allow_html=True)
    st.caption('PART 1')
    batal               = (delivered_orders[delivered_orders["order_status"] == "canceled"])
    batal['is_delayed'] = batal['order_delivered_customer_date'] > batal['order_estimated_delivery_date']

    with st.write(batal[['order_id','order_status','order_delivered_customer_date', 'order_estimated_delivery_date', 'is_delayed']])
    
    with st.container():
        grup1 = batal.groupby('is_delayed').size()

    del batal
    labels    = ['Not delayed', 'Delayed']
    myexplode = [0.2,0]
    colors    = sea.color_palette('Set3')

    plt.pie(grup1, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, shadow=True, explode=myexplode)
    plt.title('Pembatalan Pesanan')
    grafik2 = plt.gcf()
    plt.close()
    st.pyplot(grafik2)

    del grafik2

    st.caption('PART 2')
    batal               = delivered_orders
    batal["is_delayed"] = batal['order_delivered_customer_date'] > batal['order_estimated_delivery_date']
    batal               = batal[batal["is_delayed"]]

    with st.container():
        grup2 = batal.groupby('order_status').size()

    del batal

    labels    = ['canceled', 'delivered']
    myexplode = [0.10,0]
    colors    = ['blue','pink']

    plt.pie(grup2, labels=labels, colors=colors, autopct='%1.2f%%',  shadow=True, explode=myexplode)
    plt.title('Barang Yang Datang Melebihi Tanggal Estimasi Dan di Cancel')
    grafik3 = plt.gcf()
    plt.close()
    st.pyplot(grafik3)

    del grafik3

    with st.expander("Kesimpulan"):
        st.write("Maka dari hasil diatas\
                 Keterlambatan kedatangan barang kepada konsumen melebihi estimasi\
                  tidak mempengaruhi secara besar dalam pembatalan pesanan.")