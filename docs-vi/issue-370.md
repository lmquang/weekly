# Cách hiển thị code highlight chính xác

## Ảnh bìa

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025102301.webp)

Chùa cổ Linh Nhạc nghìn năm tuổi ở khu Môn Đầu Câu, Bắc Kinh. Ngôi chùa này đóng cửa từ năm 1979 và mới hoàn thành tu sửa để mở cửa trở lại vào tháng này. Trong quá trình trùng tu, người ta để lại một cửa sổ quan sát trên tường để giới thiệu những viên gạch nguyên bản từ thời Đường và thời Liêu. ([visuals_china@instagram](https://www.instagram.com/p/DQEjgx-EUNN/?img_index=6))

## Cách hiển thị code highlight chính xác

Lập trình viên thường dùng code highlight để tô màu khác nhau cho mã nguồn, giúp việc đọc code dễ dàng hơn.

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025102304.webp)

Vấn đề nằm ở chỗ: **Tổ hợp màu sắc nào là phù hợp nhất để đọc code?**

Đa số mọi người có lẽ giống tôi, thường chọn những gì mình thấy đẹp. Ví dụ như hình dưới đây với đủ loại màu sắc rực rỡ, nhìn rất thích mắt.

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025101704.webp)

Cách đây không lâu, tôi đọc được [một bài viết](https://tonsky.me/blog/syntax-highlighting/) với nhận định rằng: Sai rồi, màu đẹp chưa chắc đã phù hợp để đọc code.

Một hệ thống code highlight đúng nghĩa phải **giúp bạn nhận ra ngay lập tức những thông tin quan trọng nhất**. Quá nhiều màu sắc chỉ khiến mắt bị rối và khó tìm ra trọng tâm.

Tác giả đưa ra 5 nguyên tắc cho code highlight:

(1) **Dùng tối đa 4 màu.** Nhiều màu hơn sẽ làm phân tán sự chú ý.

(2) **Định nghĩa biến, hàm và lớp là quan trọng nhất.** Thông thường, đây là những phần cốt lõi của mã nguồn. Do đó, tên biến, tên hàm và tên lớp khi định nghĩa cần được làm nổi bật.

(3) **Chú thích cũng rất quan trọng.** Chúng thường chứa thông tin then chốt hoặc những gì tác giả muốn người khác đọc được. Vì vậy, chú thích cần phải hiển thị rõ ràng. Nhiều bộ màu để chú thích màu xám mờ là không đúng.

(4) **Hằng số và các dấu ngoặc lồng nhau cũng là thông tin quan trọng** cần được highlight.

(5) **Các phần code khác không cần highlight.** Điều này bao gồm việc đọc biến, gọi hàm, các từ khóa (class, function, if, else...). Chúng xuất hiện ở khắp mọi nơi và bạn hiếm khi phải chủ động đi tìm chúng.

Bạn có đồng tình với 5 nguyên tắc này không?

Nếu có, bạn có thể dùng thử bộ màu [Alabaster](https://github.com/tonsky/sublime-scheme-alabaster#variations-1) do tác giả thiết kế.

Dưới đây là hiệu quả hiển thị của bộ màu này.

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025101706.webp)

Để so sánh, hãy nhìn lại hiệu quả của bộ màu "đẹp mắt" trước đó.

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025101705.webp)

Theo bạn, hiệu ứng nào tốt hơn và giúp làm nổi bật thông tin cốt lõi của mã nguồn?

## Cách mua API các mô hình lớn

Nếu dùng cùng lúc mô hình của nhiều công ty, bạn sẽ giải quyết thế nào, mua API của từng bên một?

Hôm nay tôi giới thiệu một "AI Gateway" mà tôi đang sử dụng. Bạn có thể **gọi hơn 50 mô hình phổ biến chỉ qua một cổng duy nhất**. Đó chính là [Nền tảng suy luận AI của Qiniu Cloud](https://s.qiniu.com/JrUbmm).

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025102313.webp)

Họ cung cấp hầu hết các mô hình chủ chốt (như OpenAI, Gemini, Claude của nước ngoài; DeepSeek, Qwen, Doubao, Zhipu, Kimi của Trung Quốc). [Model Plaza](https://t.wangbase.com/AR4lw) (hình trên) liệt kê một số mô hình, danh sách đầy đủ có thể [tra cứu qua API](https://developer.qiniu.com/aitokenapi/13000/claude-inference-api#3).

Qiniu Cloud là nhà cung cấp dịch vụ đám mây lâu đời với 15 năm hoạt động và đã niêm yết, nên rất đáng tin cậy. Bạn hoàn toàn có thể yên tâm về độ ổn định và chất lượng dịch vụ.

Sử dụng "Giao diện thống nhất" của họ có vài ưu điểm đáng giá: (1) **Sử dụng thuận tiện**, thanh toán bằng Nhân dân tệ, không cần thẻ tín dụng quốc tế; (2) **Kết nối đơn giản**, hỗ trợ mọi AI client, IDE, dòng lệnh, MCP với hai định dạng API của OpenAI/Claude; (3) **Độ trễ thấp + Băng thông cao**, dùng [AIPerf](https://www.aiperf.top/test) đo thử khi gọi mô hình Google, thời gian phản hồi trung bình khoảng 700ms, băng thông trung bình đạt 184.6 Token/s; (4) **Hạn mức cao**, người dùng thông thường có thể đạt 500 yêu cầu/phút và 5 triệu Token/phút, đủ dùng cho hầu hết các tình huống.

Hiện tại, chương trình khuyến mãi cho người dùng mới vẫn đang diễn ra. <u>Người dùng mới được tặng miễn phí 3 triệu Token. Nếu mời thêm một người bạn sử dụng, bạn sẽ nhận thêm 5 triệu Token, còn người bạn đó nhận được 10 triệu Token</u>.

Tóm lại, nếu bạn đăng ký qua [link giới thiệu của tôi](https://s.qiniu.com/JrUbmm), bạn sẽ có sẵn 13 triệu Token miễn phí. Sau đó, bạn tạo link giới thiệu của riêng mình để nhận thêm 5 triệu Token cho mỗi người bạn mời được.

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025102402.webp)

## Tin tức công nghệ

1. Tuần này, một chiếc máy bay Boeing 737 Max của Mỹ đã va chạm với [vật thể lạ](https://economictimes.indiatimes.com/news/international/us/united-airlines-737-max-carrying-140-passengers-to-lax-diverts-after-mysterious-object-cracks-cockpit-windshield-midair-pilot-injured/articleshow/124683266.cms) ở độ cao 11.000 mét. Kính chắn gió bị vỡ khiến phi công bị thương ở tay.

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025102008.webp)

Ở độ cao này thì không thể là chim. Kính chắn gió có vết cháy sém do nhiệt độ cao nên cũng không thể là mưa đá. Khả năng cao là thiên thạch hoặc rác vũ trụ.

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025102009.webp)

Nếu xác định là rác vũ trụ, đây sẽ là chiếc máy bay đầu tiên trong lịch sử bị rác vũ trụ va trúng.

(Cập nhật: Tin mới nhất cho biết máy bay có thể đã va phải khinh khí cầu thời tiết trên cao. Đây cũng có thể là trường hợp máy bay đâm vào khinh khí cầu đầu tiên.)

2. Một công ty lốp xe Trung Quốc tại Trường Xuân, Cát Lâm vừa sản xuất chiếc [lốp xe lớn nhất thế giới](https://finance.sina.cn/tech/2025-10-19/detail-infumsek4716883.d.html).

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025102002.webp)

Chiếc lốp này có đường kính hơn 4 mét, nặng hơn 6 tấn, dùng cho xe khai thác mỏ lộ thiên loại lớn.

3. Quốc gia nào trên thế giới không có muỗi?

Trước đây, Iceland là quốc gia duy nhất không có muỗi. Nhưng tuần này, một nông dân Iceland đã phát hiện ba con [muỗi còn sống](https://www.npr.org/2025/10/22/nx-s1-5582748/iceland-mosquitoes-first-time) tại trang trại của mình.

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025102305.webp)

Từ nay, mọi quốc gia trên thế giới đều có muỗi. Chính phủ Iceland cho rằng chúng đi theo máy bay hoặc tàu thủy để đến đây. Nhưng nguyên nhân sâu xa là hiện tượng ấm lên toàn cầu giúp muỗi có thể sinh tồn và sinh sản ở các vùng vĩ độ cao.

4. Nghiên cứu của Đại học Mie, Nhật Bản cho thấy [mùa hè ở Nhật](https://english.kyodonews.net/articles/-/62626) hiện nay dài hơn ba tuần so với 42 năm trước.

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025101201.webp)

Biến đổi khí hậu khiến mùa hè ngày càng dài và nóng hơn. Trong khi độ dài mùa đông gần như không đổi, mùa xuân và mùa thu bị rút ngắn đáng kể, chỉ còn khoảng một đến hai tuần.

5. Công ty X (trước đây là Twitter) chính thức ra mắt [thị trường tên người dùng](https://www.engadget.com/social-media/xs-handle-marketplace-will-sell-some-rare-usernames-for-millions-of-dollars-224852740.html), nơi người dùng có thể mua các tên người dùng đã bị thu hồi.

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025102110.webp)

Chính sách của nền tảng là nếu người dùng không đăng nhập trong một khoảng thời gian (ví dụ 6 tháng), tên người dùng sẽ bị thu hồi. X là nền tảng lớn đầu tiên công khai bán tên người dùng. Một số tên hiếm (như @one, @fly, @compute) có giá từ 2.500 USD đến tận 1 triệu USD.

Việc này nhắc nhở chúng ta rằng tên người dùng không thuộc về bạn mà thuộc về nền tảng. Họ chỉ cho bạn mượn tạm và có thể thu hồi bất cứ lúc nào.

## Bài viết

1. [TypeScript rất giống C#](https://typescript-is-like-csharp.chrlschn.dev/pages/intro-and-motivation.html) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025100916.webp)

Bài viết lập luận rằng cú pháp TypeScript rất giống C# vì cả hai đều do cùng một người thiết kế. Vì vậy, khi cần nâng cao hiệu suất cho TypeScript, bạn có thể cân nhắc chuyển code sang C#, vốn hiện nay cũng là nền tảng đa hệ điều hành.

2. [Cách nén hiệu ứng chuyển động web xuống 16.67ms mỗi khung hình](https://koolcodez.com/blog/inside-the-frame/) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025101002.webp)

Tần số quét màn hình thường là 60 khung hình/giây. Để chuyển động mượt mà, thời gian Render mỗi khung hình không nên quá 16.67ms. Bài viết giới thiệu một kỹ thuật CSS giúp cải thiện hiệu suất chuyển động trên web.

3. [Từ HTTP Polling đến MQTT: Quá trình tiến hóa kiến trúc trên AWS IoT Core](https://mp.weixin.qq.com/s/3wyrIFf3pQh5EJ0NWbHOjA) (Tiếng Trung)

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025101902.webp)

Dự án IoT của công ty tác giả ban đầu dùng HTTP Polling, sau đó chuyển sang giao thức MQTT và sử dụng dịch vụ đám mây AWS IoT Core.

4. [Tại sao NetNewsWire không phải là một ứng dụng Web](https://inessential.com/2025/10/04/why-netnewswire-is-not-web-app.html) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025101407.webp)

NetNewsWire là một trình đọc RSS trên máy tính. Luôn có người yêu cầu tác giả chuyển nó thành ứng dụng Web. Bài viết giải thích lý do tại sao tác giả không làm vậy với những lập luận rất thuyết phục.

5. [Phép biến đổi Burrows-Wheeler](https://sandbox.bio/concepts/bwt) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025101001.webp)

Giới thiệu thuật toán Burrows-Wheeler Transform (BWT). Nó xáo trộn chuỗi ký tự sao cho các ký tự giống nhau có xu hướng tụ lại gần nhau. Điều kỳ diệu là sau khi xáo trộn, người ta có thể dùng phép nghịch đảo để khôi phục chuỗi ban đầu, khiến thuật toán này cực kỳ phù hợp để nén văn bản.

6. [Chèn nội dung ẩn vào ảnh chụp màn hình](https://simonwillison.net/2025/Oct/21/unseeable-prompt-injections/)

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025102307.webp)

Ngày càng nhiều công ty ra mắt AI browser với khả năng đọc màn hình qua ảnh chụp. Hiện đã xuất hiện kỹ thuật nhúng văn bản mà mắt người không thấy nhưng máy tính lại đọc được vào màn hình để thực hiện Prompt Injection, khiến mô hình AI thực hiện các hành vi độc hại.

7. [Virus sử dụng ký tự ẩn Unicode](https://www.koi.ai/blog/glassworm-first-self-propagating-worm-using-invisible-code-hits-openvsx-marketplace) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025102308.webp)

Giới thiệu một loại virus JS đáng kinh ngạc. Mã độc của nó được viết bằng các ký tự ẩn Unicode mà mắt người không thấy được (phần trống ở hình trên), nhưng các engine vẫn thực thi mã này bình thường.

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025102309.webp)

## Công cụ

1. [OpenZL](https://github.com/facebook/openzl)

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025101008.webp)

Một công cụ nén mới từ Meta, phù hợp để nén dữ liệu có cấu trúc (như cơ sở dữ liệu) với tỉ lệ nén cao hơn và tốc độ nhanh hơn.

2. [Handy](https://github.com/cjpais/Handy)

![](https://cdn.beekka.com/blogimg/asset/202509/bg2025092905.webp)

Ứng dụng máy tính đa nền tảng miễn phí, nguồn mở dùng để chuyển giọng nói thành văn bản.

3. [Feed me up, Scotty!](https://feed-me-up-scotty.vincenttunru.com/)

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025102111.webp)

Dịch vụ Web tự host giúp tạo RSS feed từ bất kỳ trang web nào bằng cách chỉ định CSS selector.

4. [Judo](https://judojj.com/releases/)

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025102306.webp)

Phần mềm giao diện đồ họa (GUI) cho Git/JJ trên máy tính.

5. [htmldocs](https://github.com/htmldocs-js/htmldocs)

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025101701.webp)

Một React component dùng để tạo, chỉnh sửa và xem trước tài liệu PDF trực tiếp trên trang web.

6. [Cent](http://github.com/glink25/Cent)

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025101703.webp)

Ứng dụng Web ghi chép chi tiêu nhóm nguồn mở, dữ liệu được lưu trữ trực tiếp trong kho GitHub cá nhân của bạn.

7. [Shell360](https://github.com/nashaofu/shell360)

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025101901.webp)

SSH client đa nền tảng nguồn mở, hỗ trợ Windows, macOS, Linux, Android và iOS.

8. [015](https://github.com/keven1024/015)

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025102003.webp)

Nền tảng chia sẻ file tạm thời tự host.

9. [MHtool](https://github.com/sudo1123/MHtool)

Bộ công cụ toán học Python chạy bằng dòng lệnh, tích hợp tính toán, xử lý dữ liệu và vẽ đồ thị.

10. [TextGO](https://github.com/C5H12O5/TextGO)

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025102204.webp)

Ứng dụng máy tính giúp thiết lập các phím tắt thống nhất cho nhiều phần mềm khác nhau và thực hiện các thao tác tùy biến dựa trên nội dung được chọn.

## Liên quan đến AI

1. [AICrop](https://aicrop.app/#upload)

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025101702.webp)

Công cụ web miễn phí dùng AI để cắt ảnh tự động cho phù hợp với các nền tảng mạng xã hội như Instagram, X/Twitter, TikTok.

2. [Trình tạo ảnh AI miễn phí](https://freeaiimage.net/zh/)

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025102203.webp)

Trang web tạo ảnh từ văn bản miễn phí, không cần đăng ký, sử dụng mô hình Qwen.

3. [XCodeReviewer](https://github.com/lintsinghua/XCodeReviewer)

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025102302.webp)

Nền tảng kiểm tra mã nguồn bằng mô hình lớn, cung cấp dịch vụ phân tích chất lượng code cho lập trình viên.

4. [SLOCCount](https://tools.simonwillison.net/sloccount)

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025102303.webp)

Trang web thống kê số dòng code của dự án do Simon Willison tạo ra bằng AI để đánh giá thời gian phát triển.

5. [Trình tạo podcast](https://github.com/justlovemaki/Podcast-Generator)

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025102113.webp)

Công cụ chuyển văn bản thành podcast nguồn mở, cần API key của OpenAI.

6. [MuseBot](https://github.com/yincongcyincong/MuseBot/blob/main/README_ZH.md)

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025102205.webp)

Bot thông minh kết nối với các phần mềm chat, hỗ trợ AI đối thoại và tự động trả lời cho Telegram, Feishu, DingTalk, WeChat...

## Tài nguyên

1. [EndlessWiki](https://www.endlesswiki.com)

![](https://cdn.beekka.com/blogimg/asset/202509/bg2025092704.webp)

Bách khoa toàn thư đầu tiên trên thế giới do AI tạo ra hoàn toàn, nội dung được tạo theo thời gian thực dựa trên tìm kiếm của người dùng.

2. [ISBN Visualization](https://phiresky.github.io/isbn-visualization/)

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025102101.webp)

Trực quan hóa toàn bộ mã số sách quốc tế (ISBN) trên thế giới thành một giá sách thư viện khổng lồ.

3. [Clone Wars](https://github.com/GorvGoyl/Clone-Wars)

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025101605.webp)

Kho lưu trữ thu thập hơn 100 bản clone nguồn mở của các trang web nổi tiếng như Airbnb, Amazon, Instagram, Netflix, TikTok...

## Hình ảnh

1. **Trạm quan sát neutrino ngầm Giang Môn**

Tháng 8 năm 2025, trạm quan sát neutrino ngầm Giang Môn (JUNO) tại Quảng Đông chính thức đi vào hoạt động. Nó nằm ở vị trí giữa hai nhà máy điện hạt nhân Dương Giang và Đài Sơn để thu nhận các hạt neutrino phát ra từ đó.

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025100910.webp)

Thiết bị cốt lõi là một máy dò hình cầu trong suốt đường kính 35.4 mét, đặt sâu 700 mét dưới lòng đất. Bên trong đổ đầy 20.000 tấn chất lỏng đặc biệt giúp phát sáng khi tương tác với neutrino.

Xung quanh quả cầu lắp đặt khoảng 43.212 máy dò quang học để liên tục ghi lại những tia sáng lóe lên đó.

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025100911.webp)

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025100912.webp)

Dựa vào những tia sáng này, các nhà khoa học có thể xác định được đặc tính của neutrino. Toàn bộ thiết bị được ngâm trong bể nước siêu thuần đường kính 44 mét. Phía trên bể có một máy dò khổng lồ gọi là Top Tracker để loại bỏ các hạt vũ trụ đi lạc, tránh nhầm lẫn với neutrino từ nhà máy điện.

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025100913.webp)

2. **Cầu Choluteca**

Từ năm 1996 đến 1998, một công ty Nhật Bản đã xây dựng cây cầu Choluteca dài nhất Honduras (484 mét). Ngay sau khi hoàn thành, một trận bão lớn đổ bộ. Thân cầu không hề hấn gì nhưng các đường dẫn hai đầu cầu đã bị phá hủy hoàn toàn.

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025102311.webp)

Chưa kịp sửa chữa thì điều tồi tệ hơn đã xảy ra: lũ lụt do bão khiến dòng sông Choluteca đổi dòng hoàn toàn.

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025102312.webp)

Bức hình trên cho thấy thực trạng hiện tại: cây cầu trơ trọi nằm cạnh dòng sông mới.

## Trích dẫn

**Làm sao để dự án nguồn mở phát triển bền vững?**

Một câu hỏi muôn thuở: Làm sao để các dự án nguồn mở có thể duy trì sức khỏe lâu dài? Nhiều người cho rằng cần có các công ty trả tiền cho thời gian của lập trình viên.

Điều này không sai, nhưng **cách hỗ trợ tốt nhất không phải là tiền mà là con người**. Ví dụ điển hình nhất là nhân Linux, hầu hết các đóng góp mã nguồn đều đến từ nhân viên của những công ty đang hưởng lợi từ hệ điều hành này. Nếu các công ty đó chỉ quyên tiền mà không cử người tham gia, nhân Linux không bao giờ phát triển tốt được như thế.

Một ví dụ khác là ngôn ngữ Ruby. Năm 2019, một kỹ sư của Shopify hỏi Matz (người sáng lập Ruby) rằng ông cần gì. Matz trả lời: "Tôi thiếu người." Sau đó, Shopify đã cử đội ngũ tham gia phát triển cốt lõi, giúp số lượng core committer tăng thêm hơn mười người.

Nếu ngày đó Matz nói "Tôi thiếu tiền" và Shopify quyên góp hàng triệu USD, điều đó chưa chắc đã tốt cho Ruby.

Thứ nhất, ai đảm bảo định hướng phát triển của Ruby sau này không bị Shopify chi phối? Một tính năng được chấp nhận là vì ưu điểm của nó hay vì nó đến từ nhà tài trợ lớn? Ruby có dám từ chối đề xuất của Shopify không? Sở thích của nhà tài trợ có thể làm lệch lạc dự án.

Thứ hai, tiền bạc dễ gây ra sự lệ thuộc. Nếu nhà tài trợ rút lui, bạn sẽ phải sa thải nhân sự và dừng dự án. Do đó, những người nhận tài trợ thường vô thức chiều theo ý muốn của người cho để dòng tiền không bị ngắt quãng.

Tôi không nói các dự án nguồn mở không nên nhận tài trợ, nhưng những khoản tài trợ lớn luôn đi kèm với tác dụng phụ. Lần tới, nếu bạn muốn ủng hộ một dự án nguồn mở, ngoài việc quyên tiền, cách tốt hơn là hãy trực tiếp tham gia phát triển để chia sẻ gánh nặng với người sáng lập.

## Phát ngôn

1. Chúng ta phải làm quen với một thế hệ học sinh được đào tạo bởi AI: màn hình của họ đầy chữ nhưng đầu ôc thì trống rỗng. -- [Rủi ro của "Chế độ học tập" trong OpenAI](https://resobscura.substack.com/p/openais-new-study-mode-and-the-risks)

2. Nước đi khôn ngoan nhất không phải là chạy theo trào lưu, mà là trồng một cái cây và để thời gian làm việc của nó. Cây cối không mang lại lợi nhuận vào ngày mai, chúng cần mười năm. Chúng lặng lẽ lớn lên và làm mọi thứ xung quanh tốt đẹp hơn: bóng mát, giá trị, thẩm mỹ và sự bền vững. -- [Lãi suất kép của thiết kế](https://designobserver.com/the-compound-interest-of-design-what-not-to-build/)

3. OpenAI ra mắt trình duyệt Atlas, nhưng thực chất nó là một "trình duyệt phản web", cố gắng tối đa việc ngăn người dùng lướt Internet. Ví dụ, khi bạn tìm kiếm "Taylor Swift", nó sẽ nói cho bạn biết đó là ai nhưng tuyệt nhiên không đưa ra bất kỳ liên kết nào dẫn đến trang web cá nhân của cô ấy. -- [Atlas của ChatGPT: Trình duyệt chống lại Web](https://www.anildash.com/2025/10/22/atlas-anti-web-browser/)

4. Kỹ sư không chỉ cần kỹ năng chuyên môn mà còn cần kỹ năng mềm, tức là kỹ năng giao tiếp giữa người với người. Nếu bạn không hiểu sự phức tạp của xã hội loài người, bạn sẽ không hiểu cách vận hành của công ty hay đội nhóm, từ đó ảnh hưởng đến hiệu quả công việc và khả năng mở rộng tầm ảnh hưởng của bản thân. -- [Kỹ năng mềm bị đánh giá thấp](https://utopianengineeringsociety.substack.com/p/new-series-underrated-soft-skills)

(Hết)

