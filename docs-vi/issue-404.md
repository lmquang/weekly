---
date: 2026-07-17
tags: ["ai", "trí tuệ nhân tạo", "lập trình", "phần cứng", "thiết kế", "bảo mật", "mã nguồn mở", "javascript", "go", "công nghệ"]
---

# Những điều cần biết về bộ nhớ AI

## Ảnh bìa

![](https://cdn.beekka.com/blogimg/asset/202607/bg2026071603.webp)

Triển lãm "SpongeBob" đang diễn ra tại một trung tâm thương mại ở Thượng Hải. ([via](https://m.thepaper.cn/newsDetail_forward_33450995))

## Những điều cần biết về bộ nhớ AI

Để tự chạy các mô hình AI tại nhà, bạn có hai lựa chọn phần cứng.

Một là sử dụng card đồ họa rời. Hiện tại, dòng card đồ họa cao cấp nhất cho người dùng phổ thông là RTX 5090 của Nvidia, sở hữu bộ nhớ VRAM 32GB với mức giá khoảng 30.000 Nhân dân tệ.

![](https://cdn.beekka.com/blogimg/asset/202607/bg2026071511.webp)

Lựa chọn thứ hai là những chiếc máy tính gia đình sử dụng chipset tích hợp (CPU + GPU tích hợp + RAM tích hợp), chẳng hạn như chiếc mini PC trang bị chipset Strix Halo của AMD (mẫu cụ thể là Ryzen AI Max+ 395) với bộ nhớ RAM đi kèm lên tới 128GB, giá khoảng 20.000 Nhân dân tệ.

![](https://cdn.beekka.com/blogimg/asset/202607/bg2026071512.webp)

Câu hỏi đặt ra là: Lựa chọn nào tốt hơn?

Hầu hết mọi người sẽ chọn ngay card đồ họa rời mà không cần suy nghĩ, vì hiệu năng tính toán của nó vượt trội hơn hẳn chipset tích hợp.

Dưới đây là thông số hiệu năng tính toán dấu phẩy động đơn chính xác 32-bit (FP32) của cả hai mà tôi tìm hiểu được:

> - Card đồ họa rời (RTX 5090): **104.8 TFLOPS**
> - Chipset tích hợp (AMD Ryzen AI Max+ 395): **14.8 TFLOPS**

Có thể thấy hiệu năng của card đồ họa rời cao gấp 7 lần chipset tích hợp. Với các phép toán dấu phẩy động có độ chính xác thấp hơn (như FP16 hay FP4), khoảng cách này còn lớn hơn nữa.

Nhưng câu trả lời thực tế lại là: Chưa chắc chắn. Trong nhiều trường hợp, một chiếc mini PC dùng chipset tích hợp mới là giải pháp tối ưu hơn để chạy các mô hình AI cục bộ.

Lý do rất đơn giản: phần lớn các mô hình AI có số lượng tham số lớn một chút thì RTX 5090 hoàn toàn bất lực.

Vấn đề nằm ở dung lượng VRAM 32GB là quá ít. Một mô hình 70B tham số, nếu lượng tử hóa về độ chính xác 4-bit, sẽ cần khoảng 32.6GB bộ nhớ để tải toàn bộ trọng số vào RAM. Con số này vượt quá dung lượng VRAM của RTX 5090, khiến nó không thể khởi chạy.

Trong khi đó, chiếc mini PC của AMD có sẵn tới 128GB RAM, việc tải mô hình diễn ra cực kỳ dễ dàng. Bộ nhớ trên chipset tích hợp được chia sẻ chung giữa GPU và CPU, nên được gọi là "bộ nhớ thống nhất" (unified memory). Ưu điểm của nó là có thể phân bổ tối đa dung lượng bộ nhớ cho một bộ xử lý duy nhất, nhờ đó xử lý được các mô hình AI tiêu tốn nhiều bộ nhớ.

Apple đã áp dụng kiến trúc "bộ nhớ thống nhất" này trên các dòng chip M từ lâu. Các nhà sản xuất khác hiện cũng đang nối gót, có thể kể đến Strix Halo của AMD, DGX Spark của Nvidia, Core Ultra của Intel hay Snapdragon X của Qualcomm. Ngoài dung lượng bộ nhớ lớn, giá thành của giải pháp này cũng rẻ hơn nhiều so với việc mua card đồ họa rời.

Đến đây, có thể bạn sẽ tự hỏi: Nếu chipset tích hợp có nhiều ưu điểm như vậy, liệu có cần mua card rời nữa không?

Câu trả lời là bộ nhớ có hai thông số quan trọng: dung lượng và băng thông bộ nhớ. Điểm yếu chí mạng của chipset tích hợp lại chính là băng thông bộ nhớ.

Băng thông bộ nhớ là tốc độ truyền dữ liệu từ bộ nhớ đến bộ xử lý. RTX 5090 tuy có dung lượng VRAM ít nhưng băng thông lại cực kỳ lớn, đạt tới 1792GB/s, trong khi con số này của AMD chỉ là 256GB/s.

Mỗi khi tạo ra một Token, bộ xử lý của mô hình AI phải đọc lại toàn bộ mô hình từ bộ nhớ để tính toán. Nếu băng thông bộ nhớ là 256GB/s, với một mô hình nặng 40GB, bộ xử lý chỉ có thể đọc 6 lần mỗi giây (256 chia cho 40), tức là tốc độ tạo ra chỉ khoảng 6 Token/s trên lý thuyết (thực tế có thể còn thấp hơn). Tốc độ chậm như rùa này thì khó ai có thể kiên nhẫn nổi.

Ngay cả con chip M3 Ultra của Apple, vốn là dòng có băng thông bộ nhớ lớn nhất với 819GB/s, cũng chỉ tạo được khoảng 20 Token/s, vẫn kém xa mức 1792GB/s của RTX 5090.

Do đó, cả dung lượng lẫn băng thông bộ nhớ đều là những nút thắt cổ chai đối với các mô hình AI. Đây cũng là lý do tại sao giá của bộ nhớ băng thông cao (HBM) lại tăng phi mã trong thời gian qua.

Nếu quyết định chọn mini PC dùng chipset tích hợp, bạn phải chuẩn bị tâm lý chấp nhận tốc độ tạo Token rất chậm.

May mắn thay, để tiết kiệm tài nguyên tính toán, kiến trúc "Mô hình hỗn hợp chuyên gia (MoE)" đã ra đời. Khi tính toán Token, MoE không cần đọc toàn bộ tham số mà chỉ kích hoạt một phần nhỏ trong số đó.

Ví dụ với mô hình Qwen3-30B-A3B, nó sở hữu 30 tỷ tham số nhưng mỗi lần chạy chỉ kích hoạt 3 tỷ tham số. Do đó, lượng dữ liệu cần đọc cho mỗi Token giảm từ 20GB xuống còn 2GB. Trên chiếc mini PC của AMD, tốc độ tạo Token về mặt lý thuyết có thể đạt hơn 100 Token/s, một con số thực sự ấn tượng.

Vì vậy, nếu bạn dùng mini PC chạy theo cơ chế "bộ nhớ thống nhất", hãy ưu tiên chọn các mô hình MoE.

Bên cạnh đó, mini PC còn một nhược điểm lớn khác không liên quan đến bộ nhớ, mà nằm ở tốc độ xử lý chậm của bản thân con chip.

Chúng ta đều biết trước khi tạo ra Token đầu tiên, mô hình phải xử lý các đoạn prompt đầu vào của người dùng. Vì hiệu năng tính toán của mini PC yếu nên quá trình xử lý prompt này cũng diễn ra rất chậm.

Theo các thử nghiệm thực tế, chiếc mini PC của AMD khi chạy mô hình 70B chỉ đạt tốc độ xử lý prompt khoảng 95 Token/s. Nghĩa là nếu người dùng nhập vào một tài liệu dài khoảng 4000 token, máy sẽ mất khoảng 40 giây để xử lý xong trước khi có thể xuất ra Token đầu tiên.

Hãy tưởng tượng nếu bạn đưa một lượng ngữ cảnh lớn hơn vào cửa sổ chat, thời gian chờ đợi xử lý prompt có thể kéo dài từ vài phút đến hàng chục phút.

Tóm lại, ở thời điểm hiện tại, việc chạy các mô hình lớn cục bộ trên máy tính cá nhân vẫn còn nhiều hạn chế, dù bạn chọn card đồ họa rời hay chipset tích hợp. Lựa chọn khả dĩ nhất là chạy các mô hình MoE quy mô vừa phải và không nên nhập các đoạn prompt quá dài.

## Cách đặt tên biến Boolean

Người ta thường đùa rằng trong lập trình có hai bài toán khó nhất: một là vô hiệu hóa bộ nhớ đệm (cache invalidation), và hai là đặt tên biến.

Trong đó, việc đặt tên cho các biến Boolean lại càng đau đầu hơn. Làm thế nào để thể hiện một cách rõ ràng rằng biến này chỉ nhận giá trị đúng (true) hoặc sai (false)?

Gần đây tôi có đọc được bài viết "Nghệ thuật đặt tên biến Boolean". Tác giả gợi ý sử dụng bốn tiền tố dưới đây để đặt tên cho biến Boolean, và tôi thấy điều này rất hữu ích.

(1) **is-**: mô tả trạng thái của sự vật, theo sau là một tính từ. Ví dụ: `isActive`, `isDeleted`, `isEmpty`.

(2) **has-**: mô tả quyền sở hữu hoặc quan hệ chứa đựng, theo sau là một danh từ. Ví dụ: `hasAccess`, `hasChildren`, `hasValidationErrors`.

(3) **can-**: mô tả khả năng hoặc quyền hạn của sự vật. Ví dụ: `canEdit`, `canDelete`, `canRetry`.

(4) **should-**: mô tả ý định hoặc logic xử lý. Ví dụ: `shouldRetry`, `shouldCacheResponse`.

Ngoài bốn tiền tố này, có một quy tắc vàng khác là không bao giờ sử dụng từ phủ định trong tên biến Boolean.

Ví dụ, thay vì dùng `isDisabled`, hãy dùng `isEnabled = false`.

## Tin tức công nghệ

1\. [Bàn phím OpenAI](https://openai.com/zh-Hans-CN/supply/co-lab/work-louder/)

OpenAI vừa cho ra mắt một chiếc bàn phím tiện dụng để hỗ trợ thao tác với các AI agent.

![](https://cdn.beekka.com/blogimg/asset/202607/bg2026071601.webp)

Phía dưới bàn phím là một hàng phím tắt dùng cho các thao tác phê duyệt, từ chối, nhập liệu bằng giọng nói. Phía trên là hàng đèn LED RGB hiển thị trạng thái hiện tại của AI agent (đang suy nghĩ, đang chạy, đang chờ, hoàn thành).

![](https://cdn.beekka.com/blogimg/asset/202607/bg2026071602.webp)

Sản phẩm này có giá 230 USD, trông không có gì mới mẻ và cũng chưa chắc đã tiện dụng hơn bàn phím thường.

Nhà thiết kế nổi tiếng Jony Ive sau khi rời Apple hiện đang phụ trách mảng thiết kế phần cứng cho OpenAI. Mọi người đều kỳ vọng ông sẽ mang tới những thiết bị thông minh đột phá, nhưng chiếc bàn phím nhỏ đầu tiên này thực sự gây thất vọng.

2\. [Tiểu hành tinh 2016HO3](https://www.cnsa.gov.cn/n6758823/n6758838/c10760422/content.html)

Tàu thăm dò Thiên Vấn 2 được phóng vào tháng 5 năm 2025. Sau hành trình bay khoảng 400 ngày, tàu đã tiếp cận mục tiêu là tiểu hành tinh 2016HO3 và gửi những bức ảnh đầu tiên về Trái Đất.

![](https://cdn.beekka.com/blogimg/asset/202607/bg2026071501.webp)

Tiểu hành tinh này dài khoảng 20 mét, chỉ lớn hơn một chút so với nửa sân bóng rổ tiêu chuẩn. Hình dạng của nó không đều và có nhiều góc nhọn, cho thấy đây có khả năng là một mảnh vỡ sau va chạm chứ không phải được hình thành từ dung nham nguội lạnh.

Khi chụp những bức ảnh này, Thiên Vấn 2 cách tiểu hành tinh 20 km. Bước tiếp theo theo kế hoạch là thu thập các mẫu đá từ tiểu hành tinh này để mang về Trái Đất.

Thách thức ở chỗ sải cánh của tàu Thiên Vấn 2 lên tới 15 mét, chỉ nhỏ hơn tiểu hành tinh một chút. Việc lấy mẫu có thể làm thay đổi quỹ đạo của tiểu hành tinh này.

3\. [Máy dệt chạy bằng sức gió](https://www.merelkarhof.nl/work/wind-knitting-factory)

Một nhà thiết kế người Hà Lan đã phát minh ra chiếc máy dệt len chạy bằng sức gió dùng trong gia đình, có thể lắp đặt ở ban công hoặc sân thượng.

![](https://cdn.beekka.com/blogimg/asset/202507/bg2025070405.webp)

Sức gió sẽ làm quay các cánh quạt, truyền lực đến một bàn xoay dệt tròn để đan len thành khăn quàng cổ.

![](https://cdn.beekka.com/blogimg/asset/202507/bg2025070406.webp)

Khi gió lớn, tốc độ dệt diễn ra cực kỳ nhanh. Đây là một thiết bị thuần cơ khí, không sử dụng điện gió.

![](https://cdn.beekka.com/blogimg/asset/202507/bg2025070407.webp)

Ý tưởng của nhà thiết kế là chứng minh cho mọi người thấy rằng chúng ta hoàn toàn có thể tận dụng năng lượng gió ngay trong lòng đô thị.

![](https://cdn.beekka.com/blogimg/asset/202507/bg2025070408.webp)

## Bài viết

1\. [Cẩm nang tìm việc dành cho Tiến sĩ Machine Learning](https://silviasapora.github.io/blog/ml-interviews.html) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202607/bg2026071509.webp)

Tác giả là một Tiến sĩ ngành Machine Learning vừa tốt nghiệp tại Mỹ và đã đầu quân cho DeepMind. Bài viết này đúc kết và nhìn lại quá trình tìm việc của cô.

Ngoài ra còn có một [bài viết tương tự](https://alisawuffles.github.io/blog/job-search/).

2\. [Xác thực ACME qua DNS](https://hsm.tunnel53.net/article/dns-for-acme-challenges/) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202509/bg2025092405.webp)

Chứng chỉ HTTPS miễn phí cần được cấp thông qua giao thức ACME. Giao thức này yêu cầu xác minh quyền sở hữu tên miền, và một trong những phương pháp xác thực là sử dụng DNS. Bài viết này sẽ giải thích chi tiết cơ chế hoạt động của nó.

3\. [Tình cảnh tiến thoái lưỡng nan của ngôn ngữ Go](https://www.andrewvittiglio.com/thoughts/go-killed-arenas) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202512/bg2025120608.webp)

Bài viết nhận định ngôn ngữ Go đang rơi vào tình thế lấp lửng và tương lai không mấy tươi sáng. "Khi các ngôn ngữ chậm chạp trở nên nhanh hơn, các ngôn ngữ phức tạp trở nên dễ tiếp cận hơn, vùng đệm ở giữa mà Go đang chiếm giữ sẽ dần biến mất."

4\. [So sánh tốc độ các thuật toán băm trong JavaScript](https://lemire.me/blog/2025/01/11/javascript-hashing-speed-comparison-md5-versus-sha-256/) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202501/bg2025011918.webp)

MD5 và SHA256 đều là các thuật toán băm phổ biến. Bài viết này thử nghiệm xem trong môi trường JavaScript, thuật toán nào có tốc độ tạo mã băm nhanh hơn. Kết quả có thể sẽ khiến bạn bất ngờ.

5\. [Bảng tra cứu ký tự điều khiển trong Terminal](https://jvns.ca/blog/2024/10/31/ascii-control-characters/) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202411/bg2024110405.webp)

Tác giả đã vẽ một sơ đồ tổng hợp 33 phím tắt điều khiển thông dụng trên dòng lệnh (chẳng hạn như Ctrl-C để hủy lệnh đang chạy).

6\. [Khi Richard Feynman gia nhập công ty khởi nghiệp của tôi](https://longnow.org/ideas/richard-feynman-and-the-connection-machine/) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202607/bg2026071605.webp)

Hồi ký của tác giả về nhà vật lý nổi tiếng Richard Feynman khi ông tham gia vào công ty khởi nghiệp phát triển siêu máy tính, chứa đựng nhiều câu chuyện thú vị.

## Công cụ

1\. [WhatCable](https://github.com/darrylmorley/whatcable)

![](https://cdn.beekka.com/blogimg/asset/202607/bg2026071510.webp)

Ứng dụng trên thanh menu macOS, hiển thị thông số và đặc tính của sợi cáp USB-C đang cắm vào máy tính.

2\. [amber](https://amber-lang.com/)

![](https://cdn.beekka.com/blogimg/asset/202607/bg2026071401.webp)

Một ngôn ngữ mới giúp đơn giản hóa cú pháp Bash, các đoạn mã viết bằng ngôn ngữ này có thể biên dịch trực tiếp thành Bash.

3\. [Ant](https://antjs.org)

![](https://cdn.beekka.com/blogimg/asset/202607/bg2026071402.webp)

Một runtime cực nhẹ cho JS/TS được viết mới hoàn toàn, kích thước file nhị phân chỉ vỏn vẹn 8MB.

4\. [Screen Translator](https://github.com/ciddwd/overlay-translator)

![](https://cdn.beekka.com/blogimg/asset/202607/bg2026071404.webp)

Ứng dụng Android mã nguồn mở giúp dịch màn hình theo thời gian thực. (Đóng góp từ [@ciddwd](https://github.com/ruanyf/weekly/issues/10701))

5\. [TurboOCR](https://turboocr.com/)

![](https://cdn.beekka.com/blogimg/asset/202607/bg2026071406.webp)

Công cụ nhận diện ký tự quang học (OCR) tốc độ cao tận dụng sức mạnh của GPU. (Đóng góp từ [@nataell95](https://github.com/ruanyf/weekly/issues/10706))

Ngoài ra còn có [light-ocr](https://github.com/arcships/light-ocr), một thư viện nhận diện chữ chạy offline hoàn toàn, cung cấp API cho JS/C++. (Đóng góp từ [@eric8810](https://github.com/ruanyf/weekly/issues/10714))

6\. [Visprex](https://visprex.com/)

![](https://cdn.beekka.com/blogimg/asset/202411/bg2024111013.webp)

Trang web hỗ trợ tải lên các tệp dữ liệu CSV để tự động tạo ra các biểu đồ trực quan hóa dữ liệu.

7\. [Loro](https://www.loro.dev/)

![](https://cdn.beekka.com/blogimg/asset/202311/bg2023111321.webp)

Thư viện thuật toán đồng bộ CRDT mã nguồn mở, dùng để đồng bộ hóa trạng thái theo thời gian thực giữa nhiều người dùng.

8\. [File Wizard](https://github.com/LoredCast)

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025100202.webp)

Dịch vụ tự host chạy trên nền web hỗ trợ chuyển đổi các định dạng tệp tin phổ biến, nhận diện chữ trên ảnh (OCR) và chuyển âm thanh thành văn bản.

## AI liên quan

1\. [Oh My HuggingFace](https://github.com/oh-my-hf/ohmyhf)

![](https://cdn.beekka.com/blogimg/asset/202607/bg2026071405.webp)

Ứng dụng khách đa nền tảng không chính thức dành cho Hugging Face, dùng để duyệt và tải về các mô hình, tập dữ liệu. (Đóng góp từ [@fzlzjerry](https://github.com/ruanyf/weekly/issues/10705))

2\. [pi-auto-approval](https://github.com/Europa2061/pi-auto-approval)

![](https://cdn.beekka.com/blogimg/asset/202607/bg2026071403.webp)

Plugin dành cho Pi Agent giúp tự động phê duyệt các yêu cầu xác nhận quyền hạn có mức độ rủi ro thấp, trong khi các tác vụ rủi ro cao vẫn được chuyển đến người dùng để xác nhận. (Đóng góp từ [@Europa2061](https://github.com/ruanyf/weekly/issues/10669))

3\. [GPT Crawler](https://github.com/BuilderIO/gpt-crawler)

Công cụ thu thập nội dung từ một trang web chỉ định và xuất ra tệp JSON, sau đó tải lên ChatGPT để tạo chatbot tùy chỉnh cho riêng trang web đó.

4\. [Tokenwiz](https://github.com/1rgs/tokenwiz)

![](https://cdn.beekka.com/blogimg/asset/202311/bg2023111305.webp)

Dự án mã nguồn mở mô phỏng thuật toán phân tách từ tố (tokenization) của OpenAI trên văn bản đầu vào.

## Tài nguyên

1\. [Goto Onion](https://gotoonion.site/)

![](https://cdn.beekka.com/blogimg/asset/202607/bg2026071506.webp)

Cổng kết nối đến mạng ẩn danh Tor, giúp các trình duyệt thông thường có thể truy cập được các địa chỉ có đuôi `.onion`.

2\. [Fading Maize](https://www.fadingmaize.com/)

![](https://cdn.beekka.com/blogimg/asset/202607/bg2026071507.webp)

Một dự án khá thú vị: một ban nhạc đại học tại Mỹ thu âm một album vào năm 2001 rồi tan rã ngay sau đó.

Giờ đây, họ dùng AI để chuyển thể bản thu âm cũ đó sang phong cách của năm 2026. Trang web này phát song song cả hai bản thu âm để người nghe tự so sánh.

![](https://cdn.beekka.com/blogimg/asset/202607/bg2026071508.webp)

Âm nhạc thực sự kỳ diệu, dù đã qua hơn 20 năm nhưng bản nhạc cũ vẫn không hề có dấu vết của thời gian, tiếng guitar nghe như thể mới được ghi âm ngày hôm qua.

3\. [Thuật toán tạo mê cung](https://www.jamisbuck.org/mazes/) (Maze Algorithms)

![](https://cdn.beekka.com/blogimg/asset/202601/bg2026012505.webp)

Trang web tổng hợp và minh họa trực quan các thuật toán tạo mê cung khác nhau.

## Hình ảnh

1\. [Vòng xoay giao lộ dưới lòng đại dương](https://visitfaroeislands.com/en/plan-your-stay/getting-around/world-first-under-sea-roundabout)

Vòng xoay giao lộ thường nằm ở những ngã đường đông đúc trên mặt đất, nhưng tại quần đảo Faroe thuộc Đại Tây Dương, có một vòng xoay giao lộ độc nhất vô nhị nằm dưới đáy biển.

![](https://cdn.beekka.com/blogimg/asset/202607/bg2026071502.webp)

Hình ảnh trên là sơ đồ đường hầm dưới biển của quần đảo Faroe, tại vị trí khoanh tròn màu vàng, đường hầm chia làm đôi dẫn sang hai đảo khác nhau. Một vòng xoay giao lộ đã được xây dựng ngay tại đây.

![](https://cdn.beekka.com/blogimg/asset/202607/bg2026071503.webp)

![](https://cdn.beekka.com/blogimg/asset/202607/bg2026071504.webp)

Để thu hút sự chú ý của tài xế, chính quyền địa phương đã thuê nghệ sĩ trang trí khu vực này thành hình dáng một chú sứa khổng lồ.

![](https://cdn.beekka.com/blogimg/asset/202607/bg2026071505.webp)

## Trích đoạn

1\. [AI vốn được kỳ vọng giúp tiết kiệm thời gian và giảm tải công việc](https://decrypt.co/357527/ai-save-time-instead-created-new-kind-burnout)

Nhiều người từng nghĩ AI sẽ giúp tiết kiệm thời gian và giảm bớt khối lượng công việc, nhưng một khảo sát từ Đại học California lại chỉ ra điều ngược lại. AI đang làm tăng khối lượng cũng như cường độ công việc, dẫn đến tình trạng kiệt sức nghề nghiệp (burnout).

![](https://cdn.beekka.com/blogimg/asset/202602/bg2026021615.webp)

**Tại sao AI không những không bớt việc mà lại làm phát sinh thêm việc?** Dưới đây là một số nguyên nhân chính.

**(1) Ranh giới trách nhiệm công việc bị mở rộng**. Quản lý sản phẩm bắt đầu tự viết code, nhà nghiên cứu tự cấu hình máy chủ, ranh giới nhiệm vụ của từng vị trí không còn rõ ràng mà trở nên mờ nhạt. Nhân viên phải đảm nhận những việc vốn nằm ngoài chuyên môn của họ, và AI là công cụ giúp điều đó khả thi.

Hệ quả kéo theo là các kỹ sư bỗng dưng phải dành thời gian kiểm tra, sửa lỗi và hướng dẫn code cho những đồng nghiệp không chuyên, những người đang lập trình theo kiểu "dựa vào cảm giác" (vibe coding).

Tự động hóa công việc ngoài chuyên môn thực chất lại đang tạo thêm việc cho những người khác.

**(2) Ranh giới giữa công việc và cuộc sống bị xóa nhòa**. Giao diện trò chuyện của AI giúp việc xử lý tác vụ trở nên quá dễ dàng, không còn cảm giác bế tắc trước trang giấy trắng và cũng không đòi hỏi quá trình học hỏi phức tạp.

Vì thế, nhân viên có xu hướng gửi một câu lệnh nhanh cho AI xử lý trước khi rời bàn làm việc (chẳng hạn như đi vệ sinh). Nhiều người thậm chí vẫn nhập prompt để AI chạy trong thời gian nghỉ ngơi. Việc lạm dụng AI ngoài giờ làm việc tích tụ lại làm giảm thời gian nghỉ ngơi thực tế và tăng đáng kể giờ làm việc.

**(3) Tình trạng đa nhiệm gia tăng**. Vì AI tạo ra ảo giác rằng các tác vụ có thể tự chạy ngầm ở chế độ nền, nhân viên thường bị yêu cầu quản lý nhiều luồng công việc cùng một lúc.

Điều này bề ngoài trông có vẻ giúp tăng năng suất, nhưng thực tế thường dẫn đến việc liên tục bị phân tán sự chú ý và kéo dài thêm danh sách việc cần làm.

**(4) Vòng lặp tự củng cố của các yếu tố trên.** AI giúp mọi thứ trở nên đơn giản hơn, nhân viên làm nhiều việc hơn, dẫn đến việc họ lại càng phụ thuộc vào AI để xử lý khối lượng công việc đó. Vòng lặp này cứ thế tiếp diễn và cuối cùng dẫn đến kiệt sức.

Các nhà nghiên cứu lưu ý: "Một số người tham gia khảo sát cho biết dù cảm thấy hiệu suất làm việc cao hơn nhưng họ không hề thấy thảnh thơi hơn, trái lại còn bận rộn hơn trước."

**(5) Giải pháp**. Nhóm nghiên cứu đề xuất rằng để giải quyết tình trạng kiệt sức do AI gây ra, các doanh nghiệp cần có các quy định rõ ràng định hướng nhân viên sử dụng AI một cách khoa học.

1. Hãy tạm dừng công việc một lát trước khi đưa ra các quyết định quan trọng.
2. Sắp xếp thứ tự ưu tiên các đầu việc để hạn chế tối đa việc chuyển đổi ngữ cảnh.
3. Dành thời gian cố định cho các tương tác trực tiếp giữa người với người.

## Trích dẫn

1\.

Nếu bạn là mặt trời, tôi sẽ là hố đen.

-- [Stephen Hawking](https://geohot.github.io//blog/jekyll/update/2026/05/03/punk-or-why-i-dont-stream.html)

2\.

Thế giới của các mô hình AI giống như một thành phố lớn, nơi có năm trụ sở tập đoàn lớn và một khu phố Tàu.

-- [《Kỷ nguyên độc nhất đang đến gần》](https://geohot.github.io//blog/jekyll/update/2026/05/03/punk-or-why-i-dont-stream.html)

3\.

AI là một chiếc hộp đen hoàn toàn, đồng nghĩa với việc những khái niệm như "kỹ nghệ AI" hay "kỹ nghệ prompt" chỉ là trò lừa bịp. Mọi tuyên bố rằng có thể điều khiển chiếc hộp đen này một cách tinh vi đều là giả tạo.

Bạn không thể biết được logic vận hành bên trong của AI, nó thực chất chỉ là một hệ thống kiểu "hãy tin tôi đi, người anh em" được cơ khí hóa.

-- [《AI là một công cụ tồi tệ》](https://bytecode.news/posts/2026/07/user-submission-ai-is-a-bad-tool)

4\.

Tôi có một chiếc máy làm bánh mì có thể làm gần như mọi công đoạn từ nhào bột, ủ men cho đến nướng. Tôi chỉ việc bỏ nguyên liệu vào, nhấn nút và ba tiếng sau bánh mì nóng hổi ra lò.

Thế nhưng trong suốt ba năm qua, tôi chắc chỉ dùng nó đúng hai lần. Thay vào đó, mỗi tuần tôi vẫn ra siêu thị mua một ổ bánh mì gối cắt lát sẵn đóng bao.

Điều này giải thích tại sao dù AI có thể tạo mã nguồn dễ dàng, các doanh nghiệp SaaS vẫn còn lâu mới đến hồi kết.

-- [《Tại sao sự tiện lợi luôn chiến thắng và tại sao SaaS sẽ không lụi tàn》](https://www.joanwestenberg.com/p/the-bread-paradox-why-convenience)
