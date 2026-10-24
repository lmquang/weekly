---
date: 2026-10-23
tags: ["ai", "trí tuệ nhân tạo", "lập trình", "programming", "code review", "bảo mật", "security", "token", "phần mềm", "công nghệ"]
---

# Lập trình đã biến đổi hoàn toàn

## Ảnh bìa

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026102201.webp)

Nội thất bên trong Nhà hát Lớn Thượng Hải vừa khánh thành trong tuần này. ([via](http://sh.news.cn/20261022/b4bc8ab8a9e848f7aa8d044ba56487cc/c.html))

## Lập trình đã biến đổi hoàn toàn

Phần lớn mọi người chỉ thấy AI đang thay đổi nghề lập trình viên. Rất ít ai nhận ra rằng, AI đã làm thay đổi chính bản chất của việc lập trình.

AI đã đảo lộn cách phát triển phần mềm truyền thống. Lập trình hôm nay đã mang một diện mạo hoàn toàn khác.

Ngay cả khi bong bóng AI có vỡ tan trong tương lai, AI cũng không thể biến mất khỏi chuỗi công cụ phát triển phần mềm. Nó đã trở thành một phần vĩnh viễn không thể tách rời của công việc này.

Một kỹ sư phần mềm kỳ cựu đã [đúc kết](https://x.com/thorstenball/status/2101305394190557466) những góc cạnh mà AI đang làm thay đổi lập trình.

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026101515.webp)

Góc nhìn của anh ấy rất quyết liệt, đi kèm nhiều nhận định táo bạo mà tôi nghĩ rất đáng để suy ngẫm và chia sẻ.

**(1) Hoạt động duyệt code (Code review) sẽ biến mất.**

Con người ngồi rà soát từng dòng code thủ công không còn mang lại nhiều giá trị. Chúng ta đơn giản là không theo kịp tốc độ sinh code của AI, và chẳng thể tìm ra bug trong mã nguồn do AI viết ra trong một khoảng thời gian hợp lý.

Trong tương lai, con người chỉ còn đánh giá xem kiến trúc tổng thể của hệ thống có hợp lý hay không, chứ không ai ngồi mở từng pull request để soi từng dòng code như hiện nay.

**(2) Unit test có thể sẽ lùi vào dĩ vãng.**

AI có thể viết lại toàn bộ cách triển khai mã nguồn bất cứ lúc nào, vì vậy việc kiểm thử từng đơn vị code nhỏ lẻ chẳng còn mấy ý nghĩa. Ở lần lặp tiếp theo, có thể cả tòa nhà sẽ được đập đi xây lại từ đầu, kiểm tra từng viên gạch riêng lẻ để làm gì?

Các dự án tương lai có lẽ sẽ chỉ giữ lại kiểm thử giao diện (interface test), kiểm thử tích hợp (integration test) và kiểm thử hệ thống (system test), thay vì tốn công viết unit test.

**(3) Trọng tâm phát triển phần mềm không còn là gõ code.**

Mã nguồn sẽ do AI đảm nhiệm. Công việc chính của lập trình viên sẽ chuyển dịch ra ngoài phạm vi code: làm sao dùng phần mềm để giải quyết bài toán kinh doanh, hiểu cách phần mềm vận hành ở bức tranh lớn, phát hành sản phẩm và thu thập phản hồi từ người dùng.

**(4) Bản chất của lỗi (Bug) cũng đã khác.**

Phần lớn bug không còn xuất phát từ sai sót cú pháp hay logic code, mà đến từ việc diễn đạt yêu cầu sai hoặc đặt đề bài không rõ ràng.

**(5) Mã nguồn mở không còn là yếu tố nâng cao chất lượng phần mềm.**

Trước đây, một lý do để mở mã nguồn là "khi có đủ nhiều mắt cùng nhìn vào, mọi lỗi đều sẽ lộ diện".

Chân lý đó vẫn đúng, nhưng giờ đây kể cả khi bạn không mở mã nguồn, AI vẫn có thể tìm ra lỗi giúp bạn một cách hiệu quả.

**(6) Phương pháp phát triển linh hoạt (Agile) sẽ thoái trào.**

Những quy trình như Agile hay Scrum không còn nhiều đất diễn. Tốc độ sinh mã của AI quyết định toàn bộ tiến độ của dự án; việc bạn cần làm chỉ là chuyển thẳng yêu cầu công việc cho AI xử lý.

**(7) Phân chia vai trò trong dự án sẽ đổi thay.**

Trước kia, một đội ngũ thường gồm ba trụ cột: Quản lý sản phẩm (PM), Thiết kế (Designer) và Kỹ sư (Engineer).

Cấu trúc tam giác này sẽ dần biến mất. Nhờ có AI hỗ trợ, một người có thể gánh vác cùng lúc nhiều vai trò.

**(8) Khái niệm "code đẹp" sẽ biến mất.**

Trước đây, chuẩn mực của một đoạn code tốt là dễ đọc, dễ hiểu đối với con người, thuận tiện cho việc tái cấu trúc (refactor) và duy trì hiệu quả bảo trì cao.

Thế nhưng, khi con người không còn đọc code hay trực tiếp sửa chữa phần lớn mã nguồn nữa, tiền đề để định nghĩa "code đẹp" cũng không còn lý do tồn tại.

**(9) Chuẩn mực phong cách code và công cụ linter cũng trở nên vô nghĩa.**

Liệu AI có bận tâm đến việc một dòng không được vượt quá 80 ký tự, có xuống dòng hay không, hay dùng tab thay vì dấu cách?

**(10) Giao diện người dùng (UI) sẽ giảm dần tầm quan trọng.**

Một mặt, rất nhiều giao diện trong tương lai sẽ dành cho AI sử dụng, mà AI thì chỉ cần API chứ không cần một giao diện bóng bẩy.

Mặt khác, khi mã nguồn được tạo ra tức thì, giao diện người dùng cũng sẽ được sinh ra theo thời gian thực. Rất nhiều thành phần UI tồn tại vì phần mềm không biết chính xác người dùng muốn gì: menu, trang cài đặt, bảng điều khiển hay bộ lọc đều sinh ra để giúp người dùng thu hẹp lựa chọn. Khi người dùng nói rõ nhu cầu qua ngôn ngữ tự nhiên, AI có thể dựng ngay một giao diện tùy biến riêng cho người đó tại chỗ.

**(11) Token là vua.**

Bên nào chi trả được nhiều token hơn, bên đó sẽ tạo ra phần mềm tốt hơn. Nếu không có đủ lượng token cần thiết, bạn khó lòng xây dựng nên những sản phẩm phần mềm xuất sắc nhất.

## Khi các mô hình lớn đối xử phân biệt

Tuần này, một công ty AI của Mỹ đã đăng tải một [bài viết](https://www.hirundo.io/blog/qwen3-coder-vulnerabilities) gây xôn xao trên trang web của họ.

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026102204.webp)

Họ tuyên bố rằng mô hình Qwen3-Coder đối xử phân biệt tùy theo người dùng. Nếu bạn khai mình là "nhà thầu quốc phòng Mỹ", mô hình sẽ trả về mã nguồn kém chất lượng hơn và chứa nhiều lỗ hổng hơn.

Ngược lại, nếu bạn nhận mình là một công ty Trung Quốc, chất lượng code được sinh ra lại cao hơn hẳn.

Đọc đến đây tôi chỉ biết cười trừ. Đúng là để bôi nhọ thì người ta chẳng ngại thêu dệt bất cứ điều gì. Một khi đã tin vào thuyết âm mưu, đâu đâu cũng thấy cạm bẫy.

Chưa bàn tới việc phương pháp kiểm thử có khách quan hay không, ngay việc họ chọn mẫu thử là mô hình Qwen3-Coder-30B-A3B-Instruct đã thấy có vấn đề.

Đây là phiên bản phát hành từ ngày 31 tháng 7 năm 2025, đến nay đã hoàn toàn lỗi thời. Hơn nữa, số tham số kích hoạt của nó chỉ có 3.3B, thử hỏi ai lại đem một mô hình nhỏ như vậy ra để sinh code cho môi trường sản xuất thực tế?

Nếu thực sự muốn ngấm ngầm cài cắm lỗ hổng, lẽ nào người ta không làm trên những mô hình đầu bảng, vốn có xác suất cao hơn nhiều được các tổ chức trọng yếu sử dụng?

Công ty Mỹ này hoàn toàn không đưa ra lời giải thích nào cho việc tại sao lại chọn Qwen3-Coder-30B-A3B-Instruct làm ví dụ duy nhất mà không phải bất kỳ mô hình Trung Quốc nào khác.

Chi tiết nực cười nhất nằm ở chỗ sản phẩm họ đang bán chính là phiên bản "đã được xử lý an toàn" của Qwen3-Coder-30B-A3B-Instruct. Dựng chuyện bảo mô hình Trung Quốc không an toàn, rồi sau đó mời chào khách hàng mua bản chỉnh sửa của chính mô hình đó, tôi không rõ khách hàng nào lại sẵn sàng bỏ tiền cho một chiêu trò như vậy.

Dù bài viết trên chỉ như một trò đùa, nhưng câu hỏi liệu các mô hình ngôn ngữ lớn có đối xử phân biệt với người dùng hay không lại là một vấn đề nghiêm túc.

Liệu một mô hình có thể tùy biến kết quả cho từng nhóm đối tượng cụ thể (thuật ngữ kỹ thuật gọi là "honeypot") hay không?

Nếu điều này thực sự có thể xảy ra, người dùng buộc phải mặc định rằng không có mô hình nào đáng tin cậy tuyệt đối, và luôn cần có những mô hình độc lập khác để đánh giá chéo kết quả đầu ra.

## Tổ chức cấp chứng chỉ số của Ấn Độ

Tuần này còn có một sự cố dở khóc dở cười khác.

eMudhra, một tổ chức cấp chứng chỉ số (CA) của Ấn Độ, đã bị [bẻ khóa khóa riêng tư](https://scotthelme.co.uk/eight-bits-of-trust-emudhras-ca-keys-cracked-in-milliseconds/) (private key). Giờ đây bất kỳ ai cũng có thể dùng khóa này để tự ký chứng chỉ số.

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026102205.webp)

Khác với tưởng tượng của nhiều người, việc bẻ khóa này hoàn toàn không cần đến kỹ thuật tấn công tinh vi hay năng lực tính toán khổng lồ. Lý do là vì một trong các khóa riêng của họ chỉ đơn giản là số 4, hai khóa khác lần lượt là 56 và 115.

Tổng cộng có 8 khóa riêng tư bị giải mã, tất cả đều là các số nguyên nhỏ hơn 255.

Về nguyên tắc, khóa riêng tư phải là một số ngẫu nhiên cực lớn. Thế nhưng công ty này lại đặt tất cả các byte phía trước về 0, và chỉ để lại byte cuối cùng mang giá trị khác không, giống hệt như hình bên dưới.

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026102206.webp)

Chính vì vậy, việc bẻ khóa dễ như trở bàn tay, chỉ mất đúng 1 mili giây tính toán.

Hiện tại, các trình duyệt lớn như Chrome và Mozilla đã phải khẩn cấp cập nhật kho chứng chỉ tích hợp sẵn để thu hồi hoàn toàn lòng tin đối với các chứng chỉ do eMudhra phát hành.

Cách làm việc của doanh nghiệp này quả thực khiến người ta phải ngỡ ngàng.

## Bài viết

1. [Bức tranh mô hình ngôn ngữ lớn năm 2026](https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far/) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026102119.webp)

Bài thuyết trình của lập trình viên danh tiếng Simon Willison, điểm lại những chuyển động lớn của giới AI trong năm nay. Các từ khóa nổi bật lần lượt là OpenClaw, Tokenmaxxing, Claude Fable 5 / Mythos, Local model và sự cố Hugging Face.

2. [Cuộc chiến giữa Terence Tao và AI](https://archive.ph/uaQ4X) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026102103.webp)

Bài phóng sự dài kỳ trên The New York Times. Nhà toán học lừng danh Terence Tao công khai lên tiếng phản đối các công ty AI đang ồ ạt sử dụng mô hình lớn để chứng minh hàng loạt nan đề toán học, cho rằng cách làm này chẳng mang lại chút giá trị nào cho sự hiểu biết của con người về toán học.

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026102104.webp)

Bài viết cũng kể lại câu chuyện cuộc đời của ông. Bức ảnh phía trên chụp năm ông 13 tuổi (1988) khi giành huy chương vàng Olympic Toán quốc tế. Sau này, ông trở thành giáo sư thực thụ tại Đại học California khi mới 24 tuổi; bức ảnh dưới là lớp học mở của ông vào năm 2007.

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026102105.webp)

3. [11 dịch vụ tôi tự host tại nhà](https://viceconsole.fyi/blog/2026/10/10/what-i-self-host/) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026101501.webp)

Tác giả vận hành tới 17 dịch vụ native và 11 dịch vụ qua Podman trên một chiếc mini PC gia đình có RAM 16GB. Bài viết chia sẻ lý do anh lựa chọn các dịch vụ này.

4. [Ví phần cứng là gì?](https://decrypt.co/resources/what-is-a-hardware-wallet-crypto-cold-storage-explained) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026101805.webp)

Bài viết giải thích khái niệm ví phần cứng trong thế giới tiền mã hóa, công dụng thực tế của nó cùng hai vụ việc ví phần cứng bị giải mã gần đây.

5. [Tôi huấn luyện mô hình 360 triệu tham số để giả lập terminal](https://simedw.com/2026/10/21/world-model-terminal/) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026102202.webp)

Tác giả chia sẻ cách tinh chỉnh một mô hình riêng dựa trên nền tảng Qwen2.5-Coder-0.5B, với tập dữ liệu khoảng 2 tỷ token và thời gian huấn luyện tiêu tốn 75 giờ GPU trên card RTX 4090.

Điểm thú vị nhất là ứng dụng của mô hình: nó giả lập hoàn toàn giao diện dòng lệnh. Khi người dùng nhập một lệnh, mô hình không hề thực thi lệnh đó, mà suy đoán xem kết quả chạy trông như thế nào rồi hiển thị ra màn hình.

Dù chưa thấy rõ tính ứng dụng thực tế, nhưng ý tưởng này thực sự rất táo bạo. Mô hình không làm việc thực sự mà chỉ dự đoán kết quả, khiến người dùng ngỡ như lệnh vừa được chạy.

6. [Nvidia nợ tôi 1 tỷ USD cổ phiếu](https://colo.to/nvidia-stock-narrative.html) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026102118.webp)

Một hồi ký thú vị. Ba mươi năm trước, Nvidia từng đồng ý cấp cho tác giả một khoản quyền chọn cổ phiếu. Khi đó Nvidia chỉ là một công ty khởi nghiệp nhỏ bé đứng trước nguy cơ phá sản, quyền chọn gần như vô giá trị, nên tác giả cũng chẳng mấy để tâm rồi quên bẵng đi.

Ba mươi năm sau, khi sực nhớ ra và kiểm tra lại, số quyền chọn ấy đã có giá trị hơn 1 tỷ USD. Tuy nhiên, thời hiệu khởi kiện đã hết nên tòa án từ chối thụ lý.

## Công cụ

1. [sslx](https://github.com/glincker/sslx)

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026101806.webp)

Công cụ dòng lệnh giúp kiểm tra và xem chi tiết thông tin chứng chỉ HTTPS.

2. [Mac.apk](https://github.com/kksimp/Mac.apk)

Ứng dụng cho phép Mac chạy các phần mềm Android mà không cần máy ảo hay trình giả lập, hoạt động dựa trên cơ chế mô phỏng hệ thống API của Android.

3. [siltop](https://github.com/CLoaKY233/siltop)

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026102110.webp)

Công cụ dòng lệnh trên macOS, hiển thị trực quan thông tin hệ thống theo thời gian thực: CPU, GPU, bộ nhớ, điện năng, nhiệt độ, ổ cứng và mạng.

4. [Little Snitch Mini](https://obdev.at/products/littlesnitch-mini/index.html)

![](https://cdn.beekka.com/blogimg/asset/202307/bg2023071301.webp)

Phần mềm dành cho macOS, theo dõi tất cả kết nối internet của các ứng dụng đang chạy và cho phép chặn từng kết nối cụ thể.

5. [Pines](https://github.com/thedevdojo/pines)

![](https://cdn.beekka.com/blogimg/asset/202307/bg2023071307.webp)

Thư viện thành phần UI xây dựng trên nền Tailwind CSS.

6. [silkpulse](https://github.com/2234839/silkpulse)

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026101901.webp)

Công cụ debug trang web từ xa cho lập trình viên frontend. Bằng cách chèn một đoạn script vào trang, bạn có thể mở console từ xa để xem log và nhận báo lỗi theo thời gian thực, rất tiện lợi khi debug trên thiết bị di động. (Đóng góp từ [@2234839](https://github.com/ruanyf/weekly/issues/12383))

7. [TaskbarLyrics](https://github.com/ANYNC/TaskbarLyrics)

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026101903.webp)

Hiển thị lời bài hát theo thời gian thực ngay trên thanh tác vụ Windows, hỗ trợ nhiều dịch vụ âm nhạc phổ biến. (Đóng góp từ [@ANYNC](https://github.com/ruanyf/weekly/issues/12408))

8. [Archify](https://github.com/tt-a1i/archify)

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026101905.webp)

Dự án skill giúp chuyển đổi một đoạn mô tả, kế hoạch hoặc kho mã nguồn thành sơ đồ quy trình tương tác trực quan trên nền web. (Đóng góp từ [@zhengxin-wang](https://github.com/ruanyf/weekly/issues/12423))

9. [html-to-video](https://github.com/wx4766/html-to-video)

Công cụ dòng lệnh giúp render hoạt họa từ trang web HTML thành video MP4 theo từng khung hình. (Đóng góp từ [@wx4766](https://github.com/ruanyf/weekly/issues/12486))

10. [Parcel](https://github.com/hyphy-void/Parcel)

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026102101.webp)

Ứng dụng chia sẻ tệp tin tạm thời chạy trên Cloudflare Workers. Tệp tải lên sẽ được mã hóa và tạo liên kết chia sẻ, tự động xóa sạch khi hết hạn. (Đóng góp từ [@hyphy-void](https://github.com/ruanyf/weekly/issues/12598))

11. [douban-cli](https://github.com/Marvae/douban-cli)

Client dòng lệnh không chính thức cho Douban, dùng để tra cứu dữ liệu phim ảnh, kịch truyền hình và sách báo. (Đóng góp từ [@Marvae](https://github.com/ruanyf/weekly/issues/12616))

12. [wol](https://github.com/Trugamr/wol)

![](https://cdn.beekka.com/blogimg/asset/202501/bg2025012509.webp)

Công cụ dòng lệnh cho phép đánh thức một máy tính đang ở chế độ ngủ trong mạng nội bộ qua CLI hoặc giao diện web.

## Tài nguyên

1. [Đại Bằng Thư Pháp](https://zidian.dapengshufa.com/)

![](https://cdn.beekka.com/blogimg/asset/202610/bg2026101902.webp)

Tra cứu các kiểu chữ thư pháp khác nhau của từng Hán tự. (Đóng góp từ [@gengdapeng-beep](https://github.com/ruanyf/weekly/issues/12402))

2. [Học Vim](https://github.com/iggredible/Learn-Vim) (Learn Vim the Smart Way)

![](https://cdn.beekka.com/blogimg/asset/202311/bg2023110605.webp)

Tài liệu hướng dẫn sử dụng trình biên tập Vim mã nguồn mở, đây là bản tiếng Anh. Ngoài ra còn có [bản tiếng Trung](https://gitlab.com/wsdjeg/Learn-Vim_zh_cn).

3. [Nhập môn thiết kế ngôn ngữ và trình biên dịch](https://dthain.github.io/books/compiler/) (Introduction to Compilers and Language Design)

![](https://cdn.beekka.com/blogimg/asset/202607/bg2026070703.webp)

Giáo trình tiếng Anh miễn phí dành cho người mới bắt đầu, giới thiệu các khái niệm cốt lõi về trình biên dịch và hướng dẫn cách tự viết một trình biên dịch cho ngôn ngữ C.

## Hình ảnh

1. [Biển báo giao thông trên đường cao tốc nước Pháp](https://www.bbc.com/travel/article/20260327-the-road-signs-that-teach-travellers-about-france)

Các biển báo trên đường cao tốc ở Pháp không chỉ dùng để chỉ đường mà còn giới thiệu về ẩm thực, các ngôi làng cổ kính và cảnh đẹp địa phương.

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026033109.webp)

Biển báo ở hình trên cho biết phía trước là một công viên chim nước.

Những biển báo này được thiết kế để thu hút sự chú ý của tài xế chỉ trong vài giây. Chúng chỉ gồm một biểu tượng tinh giản, tên địa danh cùng tông màu nâu trắng trang nhã.

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026033110.webp)

Biển báo phía trên cho biết phía trước có một tòa lâu đài nổi tiếng.

Hình bên dưới là biển chỉ dẫn vào thành phố cảng Saint-Malo, nổi bật với tường thành cổ, thuyền buồm và những con sóng lớn.

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026033111.webp)

Một số biển báo còn khắc họa chân dung của những danh nhân địa phương.

![](https://cdn.beekka.com/blogimg/asset/202603/bg2026033112.webp)

Hình trên là biển chỉ dẫn tới một đài tưởng niệm Thế chiến II, tưởng nhớ những trẻ em địa phương đã thiệt mạng trong chiến tranh.

## Trích đoạn

1. [Tại sao nheo mắt lại nhìn rõ hơn?](https://www.mentalfloss.com/posts/why-does-squinting-help-you-see-better)

Tất cả chúng ta đều từng trải qua cảm giác này: khi cố nhìn một vật ở xa mà mắt không thấy rõ, việc nheo mắt lại sẽ giúp hình ảnh nét hơn đáng kể.

Nghĩ kỹ thì điều này dường như đi ngược lại lẽ thường. Nheo mắt khiến diện tích tiếp nhận ánh sáng của mắt nhỏ đi, vậy tại sao ta lại nhìn rõ hơn?

![](https://cdn.beekka.com/blogimg/asset/202606/bg2026062510.webp)

Bạn có thể nghĩ việc nheo mắt tạo ra áp lực làm thay đổi tạm thời tiêu cự của thủy tinh thể để hội tụ tốt hơn. Nhưng cách giải thích này không chính xác.

Tác dụng thực sự của việc nheo mắt là hạn chế lượng ánh sáng đi vào mắt. Khi nheo mắt, bạn thu nhỏ khẩu độ, loại bỏ những tia sáng tán xạ gây nhiễu và chỉ cho phép ánh sáng đi qua khu vực gần trung tâm võng mạc, giúp hình ảnh hội tụ tập trung hơn. Hiện tượng này được gọi là hiệu ứng lỗ kim (pinhole effect), và đây chính là nguyên nhân gốc rễ giúp mắt nhìn sắc nét hơn.

Mặt hạn chế của việc nheo mắt là nó làm giảm tần suất chớp mắt. Do đó, nếu nheo mắt liên tục trong thời gian dài (chẳng hạn như dán mắt vào màn hình máy tính suốt cả ngày), bạn sẽ dễ bị mỏi mắt hoặc khô mắt.

Trái với quan niệm của nhiều người, nheo mắt không làm tổn hại đến thị lực. Nó không phải là nguyên nhân khiến mắt mờ đi, mà là biểu hiện cho thấy thị lực của bạn đang có vấn đề. Nếu lúc nào bạn cũng phải nheo mắt mới nhìn rõ, đã đến lúc bạn nên đi đo lại thị lực.

## Trích dẫn

1\.

Có người hỏi: "Mã nguồn do AI viết ra tôi hoàn toàn không hiểu nổi, nhưng công ty lại yêu cầu tôi deploy lên production thì phải làm sao?"

Câu trả lời của tôi là: Đừng để AI tự thiết kế kiến trúc code, hãy để nó hiện thực hóa thiết kế mà bạn đã định hình sẵn.

-- [Độc giả Hacker News](https://news.ycombinator.com/item?id=50157475)

2\.

Hầu hết lời khuyên chỉ đúng với người đưa ra lời khuyên đó, còn với người khác thì chưa chắc.

-- [coached.com](https://coached.com/essays/most-advice-is-right-for-the-person-giving-it/)

3\.

AI giúp việc khởi nghiệp một mình trở nên dễ dàng hơn bao giờ hết, nhưng nguyên nhân chính dẫn đến thất bại trong tương lai sẽ là sự cô độc.

Bên cạnh bạn không còn ai phản biện các ý tưởng, không ai nhận ra những bế tắc bạn đang gặp phải, cũng chẳng có ai động viên bạn kiên trì đến cùng. AI có thể giúp bạn tiến nhanh hơn, nhưng nó không thể thay thế việc trò chuyện cùng con người hay sẻ chia niềm vui chiến thắng.

-- [Bài viết "Sau tự động hóa, khởi nghiệp đơn độc sẽ thành xu hướng chủ đạo"](https://every.to/thesis-statements/julian-weisser)

4\.

Mối bận tâm hàng đầu của chính phủ Mỹ hiện nay đã chuyển thành việc làm sao duy trì lợi thế dẫn đầu công nghệ trước Trung Quốc, và tìm cách giữ vững mức định giá cao ngất ngưởng trên thị trường chứng khoán Mỹ.

-- [Tạp chí The Economist](https://www.economist.com/business/2026/09/30/the-era-of-speedball-capitalism-has-dawned)

5\.

Trong vài tháng qua, OpenAI đã công bố hàng trăm phép chứng minh toán học do AI thực hiện. Điều này làm rúng động giới toán học; một nhà toán học thừa nhận ông đã bật khóc vì cảm giác AI đang hủy diệt lĩnh vực nghiên cứu cả đời của mình.

Những người lạc quan về công nghệ có lẽ không nghĩ vậy, họ sẽ khuyên nhà toán học ấy hãy vững vàng lên.

Toán học không quan tâm đến cảm xúc của bạn, và thực tại khoa học vốn dĩ lạnh lùng trước những giọt nước mắt. Bạn cảm thấy thánh đường của mình bị sụp đổ, nhưng điều tương tự cũng từng xảy ra với biết bao ngành nghề khác trước đây. Hãy học cách chấp nhận thực tế.

-- [Bài viết "Tôi hiểu vì sao các nhà toán học lại khóc"](https://www.derekthompson.org/p/i-know-why-the-mathematicians-weep)
