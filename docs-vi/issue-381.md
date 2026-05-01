# Những người đứng đầu mảng AI mô hình lớn tại Trung Quốc đang nghĩ gì?

## Ảnh bìa

![](https://cdn.beekka.com/blogimg/asset/202601/bg2026011024.webp)

Ga Bắc Kinh Thông Châu vừa mới đi vào hoạt động nằm ở dưới lòng đất. Để tận dụng tối đa ánh sáng tự nhiên, mái che được làm bằng cấu trúc màng xuyên sáng, phía trên còn có một khung bảo vệ hình cánh buồm. ([via](https://news.cnr.cn/native/gd/kx/20251226/t20251226_527472908.shtml))

## Những người đứng đầu mảng AI mô hình lớn tại Trung Quốc đang nghĩ gì?

Thứ Bảy tuần trước (10/01), tại Bắc Kinh đã diễn ra "Hội nghị Thượng đỉnh Tiền phong AGI-Next" do Phòng thí nghiệm Mô hình Cơ bản của Đại học Thanh Hoa tổ chức.

![](https://cdn.beekka.com/blogimg/asset/202601/bg2026011406.webp)

Nhiều lãnh đạo hàng đầu trong lĩnh vực AI mô hình lớn tại Trung Quốc đã góp mặt:

> - Đường Kiệt: Giáo sư Đại học Thanh Hoa, người sáng lập Zhipu AI
> - Dương Thực Lân: Người sáng lập Moonshot AI (Kimi)
> - Lâm Tuấn Dương: Trưởng bộ phận kỹ thuật Qwen của Alibaba
> - Diêu Thuận Vũ: Cựu nhà nghiên cứu cốt cán tại OpenAI, hiện đứng đầu bộ phận AI mới của Tencent

Họ đã thảo luận về tầm nhìn đối với các mô hình lớn và sự phát triển của AI tại Trung Quốc. Trên mạng cũng đã có [bản ghi chép đầy đủ](https://www.53ai.com/news/LargeLanguageModel/2026011069524.html).

Nội dung rất đồ sộ với nhiều ý kiến thú vị. Dưới đây là phần tôi lược trích lại.

## I. Phát biểu của Đường Kiệt

### 1. Nguồn gốc của Zhipu AI

Năm 2019, chúng tôi bắt đầu nghiên cứu xem liệu có thể làm cho máy móc suy nghĩ như con người hay không. Với sự hỗ trợ mạnh mẽ từ phía nhà trường, Zhipu AI đã được thành lập từ chính những kết quả nghiên cứu tại Thanh Hoa. Hiện tôi là nhà khoa học trưởng tại đây.

Lúc đó, phòng thí nghiệm của chúng tôi đang làm khá tốt ở mảng mạng thần kinh đồ thị (Graph Neural Networks) và biểu đồ tri thức (Knowledge Graphs) trên đấu trường quốc tế. Tuy nhiên, chúng tôi đã kiên quyết tạm dừng hai hướng đi này để dồn toàn lực sang làm mô hình lớn.

### 2. Khả năng tổng quát hóa và Scaling

Chúng tôi muốn máy móc có khả năng tổng quát hóa (generalization), nghĩa là chỉ cần dạy một chút, nó có thể suy luận ra nhiều thứ khác. Giống như khi dạy trẻ con, chúng ta luôn hy vọng dạy ba vấn đề thì nó sẽ biết vấn đề thứ tư, thứ mười, thậm chí cả những thứ chưa từng được dạy. Làm sao để máy móc có được năng lực này?

Cho đến nay, chúng tôi chủ yếu đạt được mục tiêu này thông qua Scaling (mở rộng quy mô) ở nhiều tầng bậc khác nhau.

(1) Ban đầu, chúng tôi dùng Transformer để huấn luyện mô hình nhằm ghi nhớ mọi kiến thức. Dữ liệu huấn luyện càng nhiều, năng lực tính toán càng lớn thì khả năng ghi nhớ của mô hình càng mạnh. Điều đó có nghĩa là nó đã "học thuộc" mọi kiến thức trên thế giới và có khả năng tổng quát hóa nhất định để trừu tượng hóa hay suy luận đơn giản. Ví dụ, khi bạn hỏi thủ đô của Trung Quốc là gì, mô hình không cần suy luận mà chỉ cần lấy ra từ kho kiến thức.

(2) Tầng thứ hai là thực hiện căn chỉnh (alignment) và suy luận cho mô hình, giúp nó có năng lực suy luận phức tạp hơn và hiểu được ý định của chúng ta. Chúng tôi cần liên tục Scaling SFT (Supervised Fine-Tuning - tinh chỉnh có giám sát) và thậm chí cả học tăng cường (Reinforcement Learning). Thông qua một lượng lớn dữ liệu phản hồi từ con người, việc Scaling dữ liệu phản hồi giúp mô hình trở nên thông minh và chính xác hơn.

(3) Năm nay là năm bùng nổ của RLVR (Reinforcement Learning with Verifiable Rewards - Học tăng cường với phần thưởng có thể kiểm chứng). "Có thể kiểm chứng" ở đây nghĩa là gì? Ví dụ, toán học hay lập trình là những thứ có thể kiểm chứng được. Nhưng rộng hơn, việc một trang web có đẹp hay không thì lại rất khó kiểm chứng, nó cần con người phán đoán.

Đó là lý do tại sao việc này rất khó. Ban đầu chúng tôi chỉ có thể làm thông qua dữ liệu phản hồi của con người, nhưng dữ liệu này chứa rất nhiều nhiễu và kịch bản cũng rất đơn điệu.

Nếu có một môi trường có thể kiểm chứng, chúng ta có thể để máy móc tự khám phá, tự tìm ra dữ liệu phản hồi để tự trưởng thành. Đây là một thách thức lớn.

### 3. Từ Chat đến thực thi: Khởi đầu của một hệ tư tưởng mới

Nhiều người sẽ hỏi, liệu cứ tiếp tục huấn luyện mô hình thì trí thông minh sẽ ngày càng mạnh lên? Thực tế không hẳn vậy.

Đầu năm 2025, DeepSeek xuất hiện như một cú sốc. Cả giới học thuật lẫn công nghiệp đều không lường trước được sự xuất hiện đột ngột và hiệu năng cực mạnh của DeepSeek.

Lúc đó chúng tôi đã tự hỏi một câu: Có lẽ trong hệ tư tưởng của DeepSeek, bài toán Chat (đối thoại) coi như đã được giải quyết. Nghĩa là dù chúng ta có làm tốt đến đâu thì kết quả cuối cùng ở mảng Chat cũng sẽ tương đương với DeepSeek. Có thể chúng ta sẽ cá nhân hóa hơn, thêm cảm xúc hoặc làm nó phức tạp hơn, nhưng nhìn chung hệ tư tưởng này đã đi đến giới hạn. Phần còn lại chủ yếu là vấn đề về kỹ thuật và công trình.

Vậy bước tiếp theo của AI là gì? Chúng tôi nghĩ rằng việc để mỗi người có thể dùng AI để "làm một việc gì đó" thực sự mới là hệ tư tưởng tiếp theo. Trước đây là Chat, giờ là thực sự làm việc.

Lúc đó có hai hướng đi: một là lập trình (Coding, Agent); hai là dùng AI hỗ trợ nghiên cứu (DeepResearch) hay viết các báo cáo nghiên cứu phức tạp. Lựa chọn hiện tại của chúng tôi là tích hợp ba năng lực Coding, Agentic và Reasoning lại với nhau.

## II. Phát biểu của Lâm Tuấn Dương

### 4. Qwen đã được mã nguồn mở như thế nào?

Qwen có khá nhiều mô hình mã nguồn mở, tại sao vậy?

Mọi chuyện bắt đầu từ ngày 03/08/2023, khi chúng tôi mở mã nguồn một mô hình nhỏ 1.8B dùng để làm thí nghiệm nội bộ. Khi làm tiền huấn luyện (pre-training), nguồn lực vốn có hạn, bạn không thể dùng toàn bộ mô hình 7B để thử nghiệm, nên chúng tôi dùng 1.8B.

Lúc đó, một người đàn em nói với tôi rằng nên mở mã nguồn mô hình này. Tôi thực sự không hiểu nổi, vì vào năm 2023, mô hình đó gần như ở trạng thái không thể sử dụng được. Cậu ấy giải thích rằng mô hình 7B rất tốn tài nguyên máy móc, nhiều sinh viên cao học và nghiên cứu sinh không có đủ tài nguyên để làm thí nghiệm. Nếu mở mã nguồn 1.8B, nhiều bạn sinh viên sẽ có cơ hội để tốt nghiệp. Đó là một ý định rất tốt đẹp.

Cứ thế làm tiếp, các hãng điện thoại lại bảo 7B quá lớn mà 1.8B lại quá nhỏ, liệu có thể làm cái 3B hay 4B không. Việc đó không khó. Cứ thế, danh sách các mô hình ngày càng dài thêm, một phần cũng vì mục tiêu phục vụ cộng đồng.

### 5. Mục tiêu của chúng tôi là mô hình đa phương thức

Thứ mà chúng tôi thực tâm theo đuổi không chỉ là phục vụ lập trình viên hay nhà nghiên cứu, mà là liệu có thể tạo ra một Multimodal Foundation Agent (Tác nhân nền tảng đa phương thức).

Tôi đặc biệt tin vào điều này. Năm 2023, khi mô hình lớn vẫn là thứ chưa ai mặn mà lắm, đa phương thức (multimodal) đã là thứ chúng tôi muốn làm từ lâu.

Tại sao ư? Chúng tôi cảm thấy nếu muốn làm một thứ thông minh, hiển nhiên nó phải là đa phương thức. Tất nhiên có nhiều quan điểm khác nhau về việc liệu đa phương thức có thực sự thúc đẩy trí thông minh hay không. Tôi không muốn tranh cãi chuyện đó. Con người có mắt và tai để làm được nhiều việc hơn. Góc nhìn của tôi là Foundation Agent cần có năng lực sản xuất cao hơn để hỗ trợ con người tốt hơn, vậy nên chắc chắn chúng ta phải làm về thị giác và âm thanh.

Xa hơn nữa, chúng tôi muốn làm gì? Một mô hình Omni (toàn phương thức) không chỉ dừng lại ở việc hiểu văn bản, hình ảnh, âm thanh mà còn có thể tạo ra chúng. Hiện nay chúng tôi đã làm được phần nào, nhưng chưa kết hợp được việc tạo ra hình ảnh vào chung. Nếu làm được "ba đầu vào - ba đầu ra", đó mới thực sự là thứ tôi yêu thích.

## III. Phát biểu của Diêu Thuận Vũ

### 6. Sự khác biệt giữa To C và To B

Một quan sát của tôi là có sự phân hóa rõ rệt giữa To C (mô hình cho người tiêu dùng) và To B (mô hình cho doanh nghiệp).

Khi nghĩ về AI, người ta thường nghĩ đến hai thứ: ChatGPT và Claude Code. Đó là những điển hình cho To C và To B.

Với To C, phần lớn mọi người trong phần lớn thời gian không cần đến trí thông minh quá mạnh. Có thể ChatGPT của năm nay so với năm ngoái đã mạnh hơn nhiều về khả năng nghiên cứu phân tích, nhưng đa số người dùng không cảm nhận được. Họ coi nó như một bản nâng cấp của công cụ tìm kiếm và nhiều khi không biết cách kích hoạt hết trí tuệ của nó.

Nhưng với To B, trí thông minh càng cao đồng nghĩa với năng suất càng cao, và do đó nó càng có giá trị. Vì thế, người dùng doanh nghiệp luôn sẵn sàng dùng mô hình mạnh nhất. Một mô hình giá 200 USD/tháng so với mô hình kém hơn giá 20 hay 50 USD/tháng, chúng tôi thấy nhiều người Mỹ sẵn sàng trả giá cao để dùng cái tốt nhất. Có thể lương của họ là 200.000 USD/năm, mỗi ngày làm 10 nhiệm vụ. Một mô hình cực mạnh có thể làm đúng 9/10, trong khi cái kém hơn chỉ đúng 5/10. Vấn đề là nếu bạn không biết 5 nhiệm vụ đúng đó là những cái nào, bạn sẽ tốn thêm cực nhiều công sức để giám sát.

Do đó, ở thị trường To B, sự phân hóa giữa mô hình mạnh và yếu sẽ ngày càng rõ nét.

### 7. Tích hợp theo chiều dọc và Phân tầng ứng dụng

Quan sát thứ hai của tôi là liệu mô hình cơ bản và ứng dụng bên trên nên tích hợp theo chiều dọc (vertical integration) hay phân tầng rõ rệt.

Ví dụ, ChatGPT Agent là tích hợp theo chiều dọc, còn Claude (hoặc Gemini) kết hợp với Manus là phân tầng ứng dụng. Trước đây người ta tin rằng có năng lực tích hợp theo chiều dọc sẽ làm tốt hơn, nhưng ít nhất đến nay điều đó chưa chắc đã đúng.

Đầu tiên, năng lực cần thiết cho tầng mô hình và tầng ứng dụng là rất khác nhau. Đặc biệt với các kịch bản To B hay năng suất lao động, việc huấn luyện quy mô lớn vẫn là mấu chốt, và điều này thực sự khó với các công ty sản phẩm. Nhưng để dùng tốt một mô hình như vậy, hoặc để mô hình có năng lực thực thi vượt trội, cũng cần phải làm rất nhiều việc ở phía ứng dụng và môi trường.

Chúng tôi nhận thấy ở các ứng dụng To C, việc tích hợp theo chiều dọc vẫn rất hiệu quả. Dù là ChatGPT hay Doubao, mô hình và sản phẩm luôn gắn kết cực kỳ chặt chẽ. Nhưng với To B, xu hướng dường như ngược lại: mô hình ngày càng mạnh hơn, nhưng đồng thời sẽ có rất nhiều ứng dụng tầng trên đưa những mô hình tốt đó vào các quy trình sản xuất khác nhau.

### 8. Cần một Context lớn hơn

Làm sao để mô hình lớn hay AI hiện nay mang lại nhiều giá trị hơn cho người dùng? Chúng tôi thấy rằng thứ cần thiết chính là Context (ngữ cảnh) bổ sung.

Ví dụ, tôi hỏi AI hôm nay nên ăn gì? Thực tế nếu bạn hỏi ChatGPT hôm nay, năm ngoái hay ngày mai, câu trả lời sẽ rất khác nhau. Để trả lời tốt câu hỏi này, không phải bạn cần một mô hình lớn hơn hay huấn luyện mạnh hơn, mà là cần nhiều đầu vào bổ sung hơn, hay chính là Context. Nếu nó biết hôm nay tôi thấy lạnh và muốn ăn gì đó ấm nóng, tôi đang ở khu vực nào, hay vợ tôi đang ăn gì ở đâu đó, câu trả lời sẽ tốt hơn nhiều.

Việc giải quyết những vấn đề như vậy cần nhiều đầu vào ngoại lai. Chúng ta có thể dùng những dữ liệu từ các cuộc trò chuyện với người thân để làm đầu vào cho AI, điều đó sẽ mang lại rất nhiều giá trị gia tăng cho người dùng. Đây là tư duy của chúng tôi về mảng To C.

## IV. Tọa đàm: Tương lai của AI Trung Quốc

Lý Quảng Mật (Người dẫn chương trình): Tôi muốn hỏi mọi người một câu, trong 3 đến 5 năm tới, xác suất để các công ty AI hàng đầu thế giới là các đội ngũ đến từ Trung Quốc là bao nhiêu? Để chúng ta từ vị thế người theo đuôi hiện nay trở thành người dẫn dắt trong tương lai, cần phải làm tốt những gì?

### 9. Câu trả lời của Diêu Thuận Vũ

Tôi thấy xác suất khá cao, tôi khá lạc quan. Hiện tại có vẻ như bất cứ thứ gì được phát hiện ra thì ở Trung Quốc đều có thể tái hiện rất nhanh và thậm chí làm tốt hơn ở một số khía cạnh cục bộ, giống như ví dụ về ngành sản xuất hay xe điện.

Tôi nghĩ có vài điểm mấu chốt:

(1) Liệu máy quang khắc của Trung Quốc có thể đột phá hay không. Nếu năng lực tính toán trở thành nút thắt cổ chai, chúng ta có giải quyết được không.

(2) Liệu có một thị trường To B trưởng thành hơn không. Hiện nay nhiều mô hình hay ứng dụng về năng suất lao động vẫn sinh ra ở Mỹ vì người dùng ở đó sẵn sàng chi trả hơn và có văn hóa tốt hơn. Làm việc này ở trong nước hiện tại rất khó, nên mọi người thường chọn đi ra thị trường quốc tế. Đây là yếu tố khách quan lớn tương đương với năng lực tính toán.

(3) Quan trọng hơn là yếu tố chủ quan. Tôi thấy số lượng người sẵn sàng mạo hiểm để đột phá hệ tư tưởng mới ở Trung Quốc có vẻ vẫn chưa đủ nhiều. Liệu có thêm nhiều người có tinh thần khởi nghiệp và dám dấn thân để thực hiện các cuộc khám phá tiền phong hay không. Việc chúng ta có thể dẫn dắt một hệ tư tưởng mới hay không chính là vấn đề duy nhất cần giải quyết, vì mọi thứ khác từ thương mại, thiết kế công nghiệp đến kỹ thuật, chúng ta ở một mức độ nào đó đã làm tốt hơn Mỹ.

### 10. Câu trả lời của Lâm Tuấn Dương

Đây là một câu hỏi khá nhạy cảm. Về lý thuyết thì ở đây không nên tạt gáo nước lạnh, nhưng nếu nói về xác suất, tôi muốn nói về sự khác biệt mà tôi cảm nhận được giữa Trung Quốc và Mỹ. Ví dụ, năng lực tính toán (Compute) của Mỹ tổng thể lớn hơn chúng ta từ 1 đến 2 bậc quy mô. Nhưng tôi thấy dù là OpenAI hay bất cứ đâu, họ dồn một lượng lớn năng lực tính toán vào các nghiên cứu thế hệ tiếp theo, trong khi chúng ta hiện nay khá "giật gấu vá vai", việc bàn giao sản phẩm hiện tại đã chiếm gần hết năng lực tính toán rồi. Đó là một sự khác biệt lớn.

Đây có lẽ là vấn đề lịch sử: Đổi mới sáng tạo sẽ diễn ra trong tay người giàu hay người nghèo. Người nghèo không phải không có cơ hội. Chúng tôi thấy những "đại gia" đó thực sự rất lãng phí, họ huấn luyện rất nhiều thứ mà có khi chẳng để làm gì. Nhưng nếu hôm nay bạn nghèo, ví dụ như việc tối ưu hóa liên kết thuật toán và Infra (hạ tầng), nếu bạn thực sự giàu thì bạn chẳng có động lực nào để làm việc đó cả.

Tương lai có thể có một điểm nữa: Nếu nhìn từ góc độ kết hợp phần cứng và phần mềm, liệu mô hình và chip thế hệ tiếp theo của chúng ta có thực sự khả thi không?

Năm 2021, khi tôi đang làm mô hình lớn, các đồng nghiệp làm chip ở Alibaba hỏi tôi liệu có thể dự đoán xem 3 năm nữa mô hình có còn là Transformer hay đa phương thức không. Tại sao lại là 3 năm? Vì họ cần 3 năm để ra mắt một con chip (tape-out). Câu trả lời của tôi lúc đó là 3 năm nữa tôi có còn ở Alibaba không tôi còn chẳng biết! Nhưng hôm nay tôi vẫn ở đây, và nó vẫn là Transformer, vẫn là đa phương thức. Tôi rất hối hận vì lúc đó không thúc giục họ làm. Lúc đó chúng tôi nói chuyện như "ông nói gà bà nói vịt", tôi chẳng hiểu họ nói gì và họ cũng chẳng biết chúng tôi đang làm gì, thế là lỡ mất cơ hội. Liệu cơ hội đó có đến lần nữa không? Dù là một nhóm người nghèo, liệu chúng ta có "cái khó ló cái khôn", liệu cơ hội đổi mới có xuất hiện ở đây không?

Hiện nay giáo dục đang tốt lên. Tôi thuộc thế hệ đầu 90, Thuận Vũ thuộc cuối 90, trong đội ngũ của chúng tôi có nhiều bạn Gen Z. Tôi cảm thấy tinh thần mạo hiểm của mọi người ngày càng mạnh mẽ. Người Mỹ bẩm sinh có tinh thần mạo hiểm rất lớn, ví dụ điển hình là khi xe điện mới ra đời, dù có những tai nạn chết người nhưng nhiều giới siêu giàu vẫn sẵn sàng dấn thân. Ở Trung Quốc, tôi tin là giới siêu giàu sẽ không làm thế, họ sẽ chọn những thứ an toàn hơn. Nhưng hôm nay tinh thần mạo hiểm đã bắt đầu tốt hơn, môi trường kinh doanh cũng đang cải thiện, tôi nghĩ là có khả năng mang lại sự đổi mới. Xác suất không quá lớn, nhưng thực sự có khả năng.

Trong 3 đến 5 năm tới, xác suất công ty AI dẫn đầu là một công ty Trung Quốc, tôi nghĩ là 20%. 20% đã là rất lạc quan rồi, vì thực sự có rất nhiều rào cản lịch sử ở đây.

### 11. Câu trả lời của Đường Kiệt

Đầu tiên, phải thừa nhận rằng dù là nghiên cứu, đặc biệt là các AI Lab trong doanh nghiệp, chúng ta vẫn có khoảng cách với Mỹ. Đó là điểm thứ nhất.

Chúng ta đã mở mã nguồn một số thứ, có người thấy phấn khích và nghĩ rằng mô hình lớn của Trung Quốc đã vượt Mỹ. Nhưng thực tế có lẽ là khoảng cách vẫn đang nới rộng, vì các mô hình lớn bên Mỹ phần nhiều vẫn đang đóng mã nguồn, còn chúng ta thì đang chơi với các mô hình mở và cảm thấy vui vẻ với điều đó. Khoảng cách không hề thu hẹp như chúng ta tưởng tượng. Có những chỗ chúng ta làm khá tốt, nhưng cũng phải thừa nhận những thách thức và khoảng cách đang đối mặt.

Nhưng tôi thấy mọi thứ đang dần tốt lên.

(1) Thế hệ Gen Z và cuối 90 hiện nay tốt hơn hẳn trước đây. Một nhóm người thông minh thực sự dám làm những việc cực kỳ mạo hiểm. Tôi thấy điều đó ở những người như Tuấn Dương, Kimi hay Thuận Vũ.

(2) Môi trường của chúng ta có thể đang tốt hơn, từ môi trường quốc gia đến sự cạnh tranh giữa các doanh nghiệp lớn và nhỏ, hay môi trường kinh doanh nói chung.

(3) Quay lại với bản thân mỗi người, đó là liệu chúng ta có thể kiên trì hay không. Liệu chúng ta có dám làm, dám mạo hiểm trên một con đường và bền bỉ với nó hay không. Nếu chúng ta kiên trì một cách "ngốc nghếch", có lẽ chúng ta sẽ là những người đi đến cuối cùng.

## Tin tức công nghệ

1. [Khí cầu chở người](http://news.cnhubei.com/content/2026-01/11/content_19769355.html)

Ngày 09/01, khí cầu chở người Xiangyun AS700 do Hồ Bắc sản xuất đã hoàn thành chuyến bay khứ hồi từ Kinh Môn đến Vũ Hán. Đây là chuyến bay thương mại đầu tiên của khí cầu chở người tại Trung Quốc và có lẽ cũng là khí cầu thương mại duy nhất đang hoạt động trên thế giới hiện nay.

![](https://cdn.beekka.com/blogimg/asset/202601/bg2026011101.webp)

Khí cầu dài 50 mét, sức chứa tối đa 9 người. Do sức chứa quá nhỏ nên nó không thể dùng làm phương tiện giao thông thông thường mà chỉ phục vụ mục đích tham quan ngắm cảnh.

![](https://cdn.beekka.com/blogimg/asset/202601/bg2026011102.webp)

2. [Điều khiển bằng mũi](https://variationsonnormal.com/2011/04/28/finger-nose-stylus-for-touchscreens/)

Một nhà sáng chế người Anh muốn dùng điện thoại khi đang tắm, nhưng ngón tay dính nước nên không thể chạm vào màn hình.

Anh ta nảy ra ý tưởng chế ra một cây bút cảm ứng đeo trên mũi.

![](https://cdn.beekka.com/blogimg/asset/202601/bg2026011014.webp)

Cấu tạo của nó rất đơn giản: một ống mũi bằng sợi thạch cao với một cây bút cảm ứng cắm bên trong.

![](https://cdn.beekka.com/blogimg/asset/202601/bg2026011015.webp)

Phát minh này trông có vẻ hữu dụng vì giúp giải phóng đôi tay, cũng phù hợp khi đeo găng tay hoặc cho người khuyết tật.

![](https://cdn.beekka.com/blogimg/asset/202601/bg2026011016.webp)

3. [Việt Nam cấm quảng cáo không thể bỏ qua](https://saigoneer.com/vietnam-news/28652-vienam-bans-unskippable-ads,-requires-skip-button-to-appear-after-5-seconds)

Việt Nam vừa ban hành Nghị định số 342, cấm các loại quảng cáo không thể bỏ qua, có hiệu lực từ ngày 15/02/2026.

![](https://cdn.beekka.com/blogimg/asset/202601/bg2026011013.webp)

Nghị định quy định thời gian chờ của quảng cáo video phải dưới 5 giây, sau đó người xem có quyền chọn bỏ qua. Ngoài ra, cách đóng quảng cáo phải rõ ràng, dễ dàng, cấm sử dụng các ký hiệu giả mạo hoặc mờ nhạt để đánh lừa người dùng.

Điều này rõ ràng nhắm vào quảng cáo đầu video trên các nền tảng như YouTube. Đây là lần đầu tiên tôi thấy internet Việt Nam có thứ đáng để khen ngợi.

## Bài viết

1. [Tất cả mã nguồn mới của tôi sẽ đóng lại](https://x.com/MarcJSchmidt/status/2009688028931875156) (Tiếng Anh)

Tác giả là một người đóng góp cho phần mềm mã nguồn mở. Anh cảm thấy mã nguồn của mình đều bị các mô hình lớn thu thập, dẫn đến lượt truy cập vào kho lưu trữ giảm đi, từ đó không còn thu nhập. Vậy nên các đoạn mã sau này anh sẽ đóng lại.

2. [Visual Regression Testing cho trang web](https://marending.dev/notes/visual-testing/) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202601/bg2026011201.webp)

Bài viết giới thiệu cách dùng Playwright để kiểm thử thị giác cho trang web, nhằm phát hiện những thay đổi về giao diện.

3. [Tôi dùng PostgreSQL thay cho Redis](https://dev.to/polliog/i-replaced-redis-with-postgresql-and-its-faster-4942) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202601/bg2026011202.webp)

Redis là công cụ cache phổ biến nhất, nhưng tác giả chỉ ra những điểm yếu của nó và cách dùng database PostgreSQL để thay thế.

4. [Những điều ít biết về thẻ `<a>`](https://blog.jim-nielsen.com/2025/href-value-possibilities/) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202601/bg2026011008.webp)

Thẻ `<a>` dùng để tạo liên kết, bài viết giới thiệu các trường hợp liên kết đến những ký tự đặc biệt.

5. [Học về Custom Elements](https://railsdesigner.com/custom-elements/) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202512/bg2025120405.webp)

Một bài hướng dẫn về HTML Custom Elements, viết rất đơn giản và dễ hiểu.

6. [Vài suy nghĩ về Go, Rust và Zig](https://sinclairtarget.com/blog/2025/08/thoughts-on-go-vs.-rust-vs.-zig/) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202512/bg2025120503.webp)

Tác giả là một lập trình viên cao cấp, chia sẻ cảm nhận về ba ngôn ngữ Go, Rust và Zig. Điểm thú vị là cả ba đều không có lớp (class) và không hỗ trợ lập trình hướng đối tượng truyền thống.

7. [Vấn đề bo góc trên macOS Tahoe](https://noheger.at/blog/2026/01/11/the-struggle-of-resizing-windows-on-macos-tahoe/) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202601/bg2026011207.webp)

Phiên bản macOS Tahoe mới nhất đã tăng bán kính bo góc, gây khó khăn khi điều chỉnh kích thước cửa sổ. Tác giả cho rằng từ góc độ thao tác, diện tích bo góc tốt nhất không nên quá 50% ở các đầu mút.

## Công cụ

1. [whenwords](https://github.com/dbreunig/whenwords)

![](https://cdn.beekka.com/blogimg/asset/202601/bg2026011105.webp)

Tuần này trên GitHub xuất hiện một kho lưu trữ kỳ lạ: không có lấy một dòng code, chỉ có duy nhất tài liệu API.

Người dùng cần đưa tài liệu này vào mô hình lớn, chỉ định ngôn ngữ lập trình để nó tự tạo ra mã nguồn tương ứng rồi mới sử dụng. Liệu tương lai các thư viện phần mềm sẽ chỉ gồm mô tả interface mà không có code?

2. [Hongdown](https://github.com/dahlia/hongdown)

Công cụ làm đẹp định dạng văn bản Markdown, sửa đổi phong cách hiển thị theo các quy tắc thiết lập sẵn.

3. [VAM Seek](https://github.com/unhaya/vam-seek)

![](https://cdn.beekka.com/blogimg/asset/202601/bg2026011204.webp)

Trình phát video trên web mã nguồn mở, tự động hiển thị ảnh thumbnail tại nhiều mốc thời gian giúp người dùng nhấn vào để chuyển đoạn nhanh chóng.

4. [kodbox](https://github.com/kalcaddle/kodbox)

![](https://cdn.beekka.com/blogimg/asset/202601/bg2026011205.webp)

Trình quản lý tệp tin trên web mã nguồn mở.

5. [Nigate](https://github.com/hoochanlon/Free-NTFS-for-Mac)

Công cụ mã nguồn mở giúp máy Mac có thể đọc và ghi đĩa định dạng NTFS.

6. [Flippy Lid](https://github.com/huanglizhuo/Flappy.Lid)

![](https://cdn.beekka.com/blogimg/asset/202601/bg2026011206.webp)

Phần mềm thực nghiệm biến hành động đóng mở bản lề MacBook thành dữ liệu đầu vào, có thể dùng để chơi game Flippy Lid hoặc làm mật khẩu mở khóa.

7. [Jumble](https://github.com/CodyTseng/jumble)

![](https://cdn.beekka.com/blogimg/asset/202601/bg2026011301.webp)

Web client mã nguồn mở cho mạng Nostr, chuyên dùng để duyệt các nút relay tập trung vào nội dung feed.

8. [Clash Kit](https://github.com/wangrongding/clash-kit)

Công cụ quản lý Clash bằng dòng lệnh dựa trên Node.js.

9. [SlideNote](https://github.com/maoruibin/SlideNote)

![](https://cdn.beekka.com/blogimg/asset/202601/bg2026011501.webp)

Plugin Chrome mã nguồn mở để ghi chú ở thanh bên, hỗ trợ tự động đồng bộ hóa đa thiết bị.

10. [NginxPulse](https://github.com/likaia/nginxpulse)

![](https://cdn.beekka.com/blogimg/asset/202601/bg2026011502.webp)

Bảng điều khiển trực quan hóa và phân tích nhật ký truy cập Nginx, cung cấp thống kê thời gian thực, lọc PV, địa chỉ IP và phân tích client.

## Liên quan đến AI

1. [Auto Paper Digest (APD)](https://github.com/brianxiadong/auto-paper-digest)

![](https://cdn.beekka.com/blogimg/asset/202601/bg2026010901.webp)

Một ứng dụng AI tự động thu thập các bài báo AI hot hàng tuần từ arXiv, dùng NotebookLM để tạo video thuyết trình và có thể đăng lên Douyin.

2. [CC Switch](https://github.com/farion1231/cc-switch)

![](https://cdn.beekka.com/blogimg/asset/202601/bg2026011104.webp)

Ứng dụng desktop đa nền tảng giúp chuyển đổi mô hình nền tảng của Claude Code / Codex / Gemini CLI chỉ với một cú nhấp chuột, cùng các thiết lập quản lý khác.

3. [Phân tích playlist NetEase Cloud Music bằng AI](https://wangyiyun.yeyuqiudeng.com/)

![](https://cdn.beekka.com/blogimg/asset/202601/bg2026011404.webp)

Dùng AI để phân tích và tóm tắt danh sách nhạc của người dùng trên NetEase Cloud Music.

## Tài nguyên

1. [EverMsg](https://www.evermsg.com/zh)

![](https://cdn.beekka.com/blogimg/asset/202601/bg2026010902.webp)

Trang web cho phép xem trường `OP_RETURN` trong blockchain BTC. Trường này ghi lại một đoạn văn bản và một khi đã đưa lên blockchain thì sẽ không bao giờ bị xóa hay sửa đổi.

2. [DeepTime Mammalia](https://github.com/SeanWong17/Mammalia-tree)

![](https://cdn.beekka.com/blogimg/asset/202601/bg2026011208.webp)

Dự án trực quan hóa web 3D/2D tương tác về cây tiến hóa của lớp Thú, khám phá 200 triệu năm tiến hóa của động vật có vú.

## Hình ảnh

1. [Sửa tàu dưới lớp băng](https://eugene.kaspersky.com/2022/04/26/how-to-repair-the-underside-of-a-ships-hull-still-in-the-river-in-50%CB%9Ac-yakutsk/)

Nga có một xưởng đóng tàu nằm gần vòng Bắc Cực. Hàng năm vào mùa đông, bến tàu đều đóng băng.

![](https://cdn.beekka.com/blogimg/asset/202601/bg2026011001.webp)

Để có thể sửa tàu vào mùa đông, xưởng sẽ đục một mảng băng để lộ ra đáy tàu.

![](https://cdn.beekka.com/blogimg/asset/202601/bg2026011002.webp)

Lớp băng thường không quá dày để chạm đến đáy tàu nên phải đục theo từng lớp. Công nhân dùng cưa điện cắt lớp băng trên cùng, chờ nước sông bên dưới đóng băng tiếp rồi lại cắt xuống, lặp lại nhiều lần cho đến khi đáy tàu lộ ra trong băng.

![](https://cdn.beekka.com/blogimg/asset/202601/bg2026011003.webp)

Đôi khi họ phải đục một rãnh băng rất dài.

![](https://cdn.beekka.com/blogimg/asset/202601/bg2026011004.webp)

![](https://cdn.beekka.com/blogimg/asset/202601/bg2026011005.webp)

Dưới đây là hình ảnh công nhân đi xuống dưới lớp băng để kiểm tra đáy tàu. Do điều kiện làm việc khắc nghiệt và nguy hiểm, lương của họ thường rất cao.

![](https://cdn.beekka.com/blogimg/asset/202601/bg2026011006.webp)

![](https://cdn.beekka.com/blogimg/asset/202601/bg2026011007.webp)

## Ngôn luận

1.

Tôi cảm thấy thế nào khi code của mình bị các mô hình lớn hấp thụ? Tôi thấy vui vì điều đó, bởi tôi coi đó là sự tiếp nối nỗ lực cả đời mình: dân chủ hóa mã nguồn, hệ thống và tri thức.

Các mô hình lớn giúp chúng ta viết phần mềm tốt hơn, hiệu quả hơn một cách nhanh chóng và mang lại cơ hội cho các đội ngũ nhỏ cạnh tranh với các tập đoàn lớn. Điều này cũng giống như những gì phần mềm mã nguồn mở đã làm vào thập niên 90. Tuy nhiên, công nghệ này quá quan trọng nên tuyệt đối không được chỉ nằm trong tay một vài công ty.

-- [Antirez](https://antirez.com/news/158), người sáng lập dự án Redis

2.

Ngay cả khi bạn không tin vào AI, việc bỏ qua nó cũng chẳng giúp ích gì cho bạn và sự nghiệp của bạn. Trước đây, bạn thức đêm lập trình và cảm thấy rạo rực khi thấy dự án chạy ổn định. Bây giờ, nếu bạn tận dụng AI hiệu quả, bạn có thể xây dựng nhiều dự án tốt hơn. Niềm vui vẫn còn đó, không hề bị ảnh hưởng.

-- [Antirez](https://antirez.com/news/158), người sáng lập dự án Redis

3.

Nếu bạn không viết, bạn chỉ là một máy trạng thái hữu hạn. Khi bạn viết, bạn có sức mạnh phi thường của một máy Turing.

-- [Manuel Blum](http://muratbuffalo.blogspot.com/2026/01/the-agentic-self-parallels-between-ai.html), người đạt giải Turing

4.

Con người rơi vào bế tắc vì ba nguyên nhân chính: (1) thiếu năng lực hành động, (2) hành động sai hướng, (3) chờ sung rụng (ảo tưởng vấn đề sẽ tự thuyên giảm mà từ chối hành động).

-- [ "Khi bạn muốn thoát khỏi bế tắc"](https://www.experimental-history.com/p/so-you-wanna-de-bog-yourself)

(Hết)
