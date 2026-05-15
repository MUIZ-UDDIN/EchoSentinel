const input_box = document.getElementById("searchInput");
const Search_btn = document.getElementById("Search_btn")
const History_div = document.getElementById("history_data")
const History_btn = document.getElementById("History_btn")
const Market_st = document.getElementById("sentimentText")
const Articles_num = document.getElementById("articleCount")
const sentimentIcon = document.querySelector(".sentiment-icon")

async function RenderNews(New_list) {

    let Pos_scr = 0
    let Neg_scr = 0

     const icons = {
                'bullish': '📈',
                'bearish': '📉',
                'neutral': '⚖️'
            };

    sentimentIcon.innerHTML = ""
    Market_st.innerHTML = "Search or fetch history to analyze market sentiment"
    Articles_num.innerHTML = `${New_list.length} articles`
    History_div.innerHTML = ""

    New_list.forEach(article => {
        if (article.sentiment == "POSITIVE") {
            Pos_scr +=1
        }
        if (article.sentiment == "NEGATIVE") {
            Neg_scr +=1
        }

            History_div.innerHTML += `
            <div class="article-card ${article.sentiment}">
                <h4 class="article-title">${article.title}</h4>
                <div class="article-meta">
                    <span class="badge">${article.sentiment}</span>
                </div>
            </div>
            `;
        }
    )

    if (Pos_scr > Neg_scr){
        sentimentIcon.innerHTML = icons.bullish
        Market_st.innerHTML = "Market is Bullish"
        }

    else if (Neg_scr > Pos_scr){
        sentimentIcon.innerHTML = icons.bearish
        Market_st.innerHTML = "Market is Bearish"
        }

    else{
        sentimentIcon.innerHTML = icons.neutral
        Market_st.innerHTML = "Market is NETURAL"
        }

}

async function On_Click() {
    const input_value = input_box.value

    if (input_value === ""){
       alert("please enter the search text in input Box")
       return input_value

       }
    else {
        const response = await fetch(`/search/${input_value}`)
        const data = await response.json()
        RenderNews(data)  
        // const hstr = fetch("/history/20")
    }
      

}

async function DisplayData() {

    const response = await fetch(`/history/${20}`)
    const data = await response.json()
    
    RenderNews(data)

}


Search_btn.onclick = On_Click
History_btn.onclick = DisplayData
