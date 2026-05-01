# Thiết kế giao diện phần mềm như thế nào?

## Ảnh bìa

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025110503.webp)

Đại sảnh tự học tại Thư viện Quốc gia Bắc Kinh vào một ngày mùa đông. ([via](https://www.xinhuanet.com/photo/20251103/d338bbe8a8104730816261a553dd7b9a/c.html))

## Thiết kế giao diện phần mềm như thế nào?

(1)

Giao diện người dùng (UI) là một lĩnh vực nghiên cứu sâu rộng. Có hẳn một ngành nghề chuyên về nó gọi là "UI Design".

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025110511.webp)

Tôi thấy nhiều lập trình viên dường như không có cảm giác về thiết kế UI. Họ không biết thế nào là một giao diện vừa đẹp vừa dễ dùng. Cách làm phổ biến là cứ nhồi nhét mọi tính năng lên màn hình, miễn là chạy được, còn người dùng có hiểu hay không thì mặc kệ.

Có rất nhiều ví dụ như vậy, điển hình là cái tôi vừa thấy dưới đây.

(2)

Có một phần mềm rất nổi tiếng tên là [Handbrake](https://handbrake.fr/), chuyên dùng để chuyển đổi định dạng video.

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025103103.webp)

Nó cực kỳ mạnh mẽ, nhận diện được gần như mọi định dạng video, đáp ứng mọi nhu cầu, lại còn miễn phí và đa nền tảng. Thế nhưng, khi bạn mở phần mềm này ra, một cảm giác sợ hãi sẽ ập đến ngay lập tức, trừ khi bạn là một chuyên gia.

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025103104.webp)

Đây là giao diện chính của nó. Đủ loại thiết lập nằm san sát nhau, đi kèm là những dòng chữ giải thích mà người ngoại đạo chẳng thể hiểu nổi. Nếu không phải chuyên gia, người dùng sẽ lúng túng: Bắt đầu từ đâu? Có bấm nhầm không? Có phải tốn hàng giờ để xem hướng dẫn không?

Những người kiên trì nhất có lẽ sẽ thử mở menu "Settings" để tìm gợi ý, nhưng đó lại là một cú giáng mạnh hơn vào hy vọng của họ.

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025103105.webp)

Giao diện dày đặc thuật ngữ chuyên môn này khiến người dùng cảm thấy trình độ của mình quá thấp, không đủ tiêu chuẩn để sử dụng công cụ. Bạn thấy đấy, người dùng chỉ muốn tìm một công cụ nhỏ để đổi đuôi video, kết quả lại bị công cụ đó nhắc nhở rằng "năng lực của bạn không đủ".

Đây chính là một giao diện tồi. Nó không chỉ khó dùng mà còn gây ức chế.

(3)

[Một lập trình viên nước ngoài](https://danieldelaney.net/normal/) đã không thể chịu đựng nổi. Tại sao giao diện của một phần mềm phổ thông lại phải phức tạp đến vậy? Anh ta tự tay thiết kế lại một UI mới.

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025103106.webp)

Trông thuận mắt hơn hẳn phải không?

Giao diện này nhìn cái hiểu ngay, hoàn toàn không gây áp lực tâm lý. Thao tác duy nhất là tải video lên. Bạn không thể làm sai vì chẳng còn chỗ nào khác để bấm. Chỉ khi thêm file xong, nút bấm duy nhất mới sáng lên để nhấp vào.

Bạn có tin được không, giao diện này và giao diện trước đó thuộc về cùng một phần mềm, thực hiện cùng một công việc?

Đây chính là bí mật của thiết kế UI xuất sắc: **Tránh quá nhiều lối vào thao tác, tránh bắt người dùng phải lựa chọn, và cố gắng cung cấp giá trị mặc định cho mọi thiết lập.** Có vậy người dùng mới không bối rối và có thể "cứ thế mà Enter".

Chắc chắn nhiều chuyên gia sẽ không đồng tình:
> - Tại sao lại bỏ đi những tính năng mạnh mẽ của Handbrake?
> - Nếu ai đó muốn tùy chỉnh khác thì sao?
> - Bạn đã tính đến các nhu cầu đặc biệt hay trường hợp cực đoan chưa?

Giải pháp rất đơn giản: Hãy làm thêm một giao diện phiên bản "Pro", có thể chính là giao diện hiện tại của Handbrake. Khi người dùng muốn nhiều tính năng hơn, họ có thể tự chuyển đổi.

(4)

Nhiều đồ dùng trong cuộc sống cũng rơi vào tình trạng tương tự với những giao diện phức tạp. Hãy nhìn chiếc điều khiển tivi này, chi chít nút bấm, có thực sự cần thiết không?

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025103107.webp)

Đến mức có người phải dùng băng keo dán kín những nút không cần thiết lại.

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025103108.webp)

Thực tế là, sau khi dán băng keo, đó mới là giao diện mà một chiếc điều khiển tivi nên có! Chỉ để lại những nút thiết yếu. Những nút mà đa số mọi người không dùng đến nên được giấu dưới một nắp trượt, để những ai thực sự cần có thể tự tìm thấy.

## [Phần mềm tuần này] NocoBase

Làm sao để phát triển hệ thống nghiệp vụ một cách nhanh chóng?

Bạn có thể nghĩ đến việc giao cho mô hình lớn, nhưng có một cách đơn giản và đáng tin cậy hơn, đó là [NocoBase](https://github.com/nocobase/nocobase).

![AI-Employees](https://cdn.beekka.com/blogimg/asset/202511/bg2025110603.webp)

Đây là một nền tảng phát triển low-code/no-code nguồn mở, hiện đã đạt 17.000 sao trên GitHub. Ý tưởng của nó rất đơn giản: (1) Kết nối cơ sở dữ liệu, (2) Cấu hình giao diện theo kiểu kéo thả, (3) Cấu hình plugin (phân quyền, đăng nhập SSO, in ấn, tài liệu...).

![AI-Employees](https://cdn.beekka.com/blogimg/asset/202511/bg2025110604.webp)

Phiên bản 2.x mới nhất còn giới thiệu khái niệm [Nhân viên AI](https://www.nocobase.com/cn/blog/nocobase-2-0), giúp đưa năng lực của mô hình lớn vào hệ thống nghiệp vụ một cách mượt mà, chẳng hạn như điều tra bối cảnh khách hàng, phân tích dữ liệu hay thu thập báo giá từ nền tảng của nhà cung cấp.

Sau hơn 4 năm ra mắt, phiên bản thương mại của họ đã có người dùng tại hơn 50 quốc gia và đạt doanh thu hàng chục triệu tệ. Bạn có thể dùng thử bản demo trên trang chủ hoặc lấy mã nguồn từ GitHub về tự triển khai.

## Tin tức công nghệ

1. **Đám cưới được tài trợ**

Một nhà khởi nghiệp nước ngoài vì chưa thành công nên lo lắng về chi phí đám cưới. Anh ta đăng bài lên mạng hỏi xem có công ty nào sẵn lòng tài trợ không, đổi lại anh sẽ trưng bày tên họ trong hôn lễ. Kết quả là có 26 công ty đồng ý tài trợ. Dưới đây là hình ảnh trong ngày cưới.

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025103005.webp)

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025103006.webp)

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025103007.webp)

2. **Vụ án bản quyền Prompt AI đầu tiên tại Thượng Hải vừa được tuyên án.**

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025110607.webp)

Năm 2022, một công ty đã soạn 6 nhóm Prompt để tạo ra các tác phẩm hội họa trên Midjourney rồi đăng lên mạng. Sau đó, họ phát hiện hai bị cáo sử dụng các Prompt này để tạo tranh và công khai đăng tải nên đã khởi kiện đòi bồi thường 9.900 tệ. Tòa án cho rằng Prompt chỉ là sự liệt kê đơn giản các yếu tố, thiếu sự liên kết logic về ngữ pháp và không thể hiện sự đầu tư trí tuệ cá nhân của tác giả, nên không được công nhận là tác phẩm. Vì vậy, tòa bác bỏ quyền tác giả đối với các Prompt này.

3. **Robot làm việc nhà chính thức mở bán**

Một công ty Mỹ thông báo Robot làm việc nhà đầu tiên trên thế giới chính thức mở bán với giá 20.000 USD. Tạo hình của nó trông hơi đáng sợ.

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025110608.webp)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025110609.webp)

Mặc dù giá không quá đắt, nhưng khả năng tự vận hành của nó rất hạn chế. Phần lớn các động tác vẫn cần con người điều khiển từ xa, và tốc độ làm việc rất chậm, lấy một chai nước mất tới 1 phút.

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025110610.webp)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025110611.webp)

4. **Sửa lỗi menu "Cập nhật và tắt máy" của Windows sau 20 năm**

Trong menu tắt máy của Windows có tùy chọn "Update and shut down". Tuy nhiên, có một bug là sau khi cập nhật hệ thống thường không tắt máy mà lại khởi động lại, đúng ra phải gọi là "Cập nhật và khởi động lại". Microsoft đã để mặc bug này suốt 20 năm qua. Cuối cùng, bản cập nhật 25H2 mới nhất đã sửa đổi hành vi này, máy sẽ tự động tắt sau khi cập nhật xong.

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025110402.webp)

5. **Mũ bảo hiểm thông minh "EagleEye"**

Công ty công nghệ quốc phòng Anduril Industries vừa ra mắt mũ bảo hiểm thông minh EagleEye. Khi sử dụng, mặt nạ có thể hạ xuống để bao bọc hoàn toàn phần đầu.

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025103008.webp)

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025103009.webp)

Chiếc mũ này hiển thị một màn hình ngay trước mắt, chồng lớp hình ảnh hiện trường với bản đồ, dữ liệu từ drone và cảm biến, giúp binh sĩ nắm bắt toàn bộ tình hình chiến trường. Dự kiến mũ sẽ được giao cho quân đội Mỹ vào năm tới. Trông nó khá giống một chiếc "mũ bảo hiểm VR" của tương lai.

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025103010.webp)

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025103011.webp)

## Bài viết

1. [Cách thiết lập một trang web dark web](https://flower.codes/2025/10/23/onion-mirror.html) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025103015.webp)

Các trang web dark web (có đuôi .onion) chỉ có thể truy cập qua trình duyệt Tor. Tác giả ghi lại quá trình tự thiết lập của mình, trông có vẻ không quá khó khăn.

2. [Cách đơn giản để lọc crawler](https://fxgn.dev/blog/anubis/) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025110403.webp)

Tác giả đề xuất một phương pháp đơn giản giúp website lọc các yêu cầu từ crawler mà không cần tường lửa, chỉ cần cấu hình lại Web server (tác giả dùng Caddy).

3. [Bạn có biết về HTML Table API không?](https://christianheilmann.com/2025/10/08/abandonware-of-the-web-do-you-know-that-there-is-an-html-tables-api/) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025110404.webp)

Có một API cổ xưa cho phép dùng JS thao tác với bảng. Dù ít người dùng nhưng các trình duyệt vẫn luôn hỗ trợ nó.

4. [Tình hình phát triển của trình biên dịch](https://abhinavsarkar.net/notes/2025-compiler-backend-survey/) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025110612.webp)

Bài viết tổng quan về sự phát triển chung của các công cụ biên dịch hiện nay.

5. [Cách tốt nhất cho Raspberry Pi là boot qua mạng](https://www.xda-developers.com/booting-raspberry-pi-network-huge-performance-difference/) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025103101.webp)

Raspberry Pi thường boot từ thẻ nhớ SD, nhưng tác giả khuyên nên chuyển sang boot qua mạng. Cách này rất tiện nếu bạn thường xuyên đổi hệ điều hành hoặc cần quản lý nhiều máy cùng lúc.

6. [Loạt tác phẩm "Xiao Xiao"](https://animationobsessive.substack.com/p/when-stick-figures-fought) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025110401.webp)

Giai đoạn 1999-2006, loạt hoạt hình Flash "Xiao Xiao" (hay còn gọi là "người que") của Chu Chí Cường đã làm mưa làm gió trên Internet. Bài viết hồi tưởng lại câu chuyện về một huyền thoại giờ ít người còn nhớ.

## Công cụ

1. [Zensical](https://github.com/zensical/zensical)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025110613.webp)

Phiên bản nâng cấp của [Material for MkDocs](https://github.com/squidfunk/mkdocs-material/) giúp giải quyết nhiều điểm yếu của MkDocs mà vẫn giữ tính tương thích hoàn toàn.

2. [Affinity](https://www.affinity.studio/)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025110203.webp)

Phần mềm đồ họa chuyên nghiệp thay thế cho Photoshop. Sau khi được Canva mua lại, giờ đây nó có thể được tải về và sử dụng miễn phí.

3. [FileBrowser Quantum](https://github.com/gtsteffaniak/filebrowser)

![](https://cdn.beekka.com/blogimg/asset/202506/bg2025062610.webp)

Trình quản lý file chạy trên nền Web tự host cực kỳ mạnh mẽ.

4. [Texo](https://github.com/alephpi/Texo)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025110202.webp)

Engine OCR cho công thức toán học nguồn mở, chuyển ảnh chụp công thức thành mã LaTeX ngay trên trình duyệt.

5. [TDesign uniapp](https://github.com/novlan1/tdesign-uniapp)

Bản chuyển đổi không chính thức của bộ component TDesign (Tencent) sang uniapp, hỗ trợ H5, WeChat Mini Program, App...

6. [GreenWall](https://github.com/zmrlft/GreenWall)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025110201.webp)

Công cụ giúp "vẽ" các hình thù chỉ định lên lịch commit của GitHub.

7. [BakLab](https://github.com/biliqiqi/baklab-web)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025110502.webp)

Nền tảng cộng đồng nguồn mở kết hợp tính năng diễn đàn và chat thời gian thực.

8. [Ngày lễ Trung Quốc](https://github.com/vsme/chinese-days)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025110512.webp)

Kho lưu trữ cung cấp hàm tra cứu ngày lễ, tiết khí của Trung Quốc, dữ liệu tự động cập nhật hàng ngày qua Action.

9. [QiLuo](https://github.com/chelunfu/qiluo_admin)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025110605.webp)

Trang quản trị viết bằng Rust sử dụng framework Axum và Sea ORM.

10. [navsite](https://github.com/wubh2012/navsite)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025110606.webp)

Chuyển đổi bảng đa chiều của Lark/Feishu thành một trang web điều hướng (navigation).

## Liên quan đến AI

1. [Jta](https://github.com/hikanner/jta)

Công cụ dòng lệnh dùng AI để dịch các file JSON ngôn ngữ ứng dụng, hỗ trợ 27 ngôn ngữ.

2. [Smart Excalidraw](https://github.com/liujuntao123/smart-excalidraw-next)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025110405.webp)

Phiên bản AI của Excalidraw, dùng ngôn ngữ tự nhiên để AI tạo ra các sơ đồ kiểu vẽ tay.

3. [VibeVoiceFusion](https://github.com/zhao-kun/VibeVoiceFusion)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025110406.webp)

Ứng dụng Web nguồn mở giúp tổng hợp giọng nói và clone giọng nói của nhiều người cùng lúc.

4. [Mini-Kode](https://github.com/minmaxflow/mini-kode)

Trợ lý lập trình AI dùng cho mục đích giảng dạy, giúp bạn hiểu cách phát triển những công cụ kiểu này.

5. [SQLBot](https://github.com/dataease/SQLBot)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025110407.webp)

Dịch vụ Web hỗ trợ truy vấn cơ sở dữ liệu bằng ngôn ngữ tự nhiên (text2sql).

6. [Docutranslate](https://github.com/xunbu/docutranslate)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025110408.webp)

Công cụ viết bằng Python dùng AI để dịch tài liệu ở nhiều định dạng khác nhau.

7. [Paper Burner X](https://github.com/Feather-2/paper-burner-x)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025110501.webp)

Dịch vụ Web hỗ trợ đọc tài liệu khoa học, cung cấp tính năng dịch, đối thoại thông minh.

## Tài nguyên

1. [Apple App Store (Web version)](https://apps.apple.com/)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025110504.webp)

Apple cuối cùng đã ra mắt phiên bản Web cho App Store. Dù không thể cài App từ đây nhưng ít nhất nó cung cấp một lối vào để tìm kiếm và khám phá ứng dụng qua trình duyệt. Mã nguồn frontend của nó được phát hiện là dùng Svelte.

2. [ASCIIMoon](https://asciimoon.com/)

![](https://cdn.beekka.com/blogimg/asset/202507/bg2025070313.webp)

Trang web hiển thị tuần trăng trong ngày bằng mã ASCII.

## Hình ảnh

**Khinh khí cầu Hindenburg**

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025110614.webp)

Hindenburg là khinh khí cầu khổng lồ do Đức chế tạo vào thập niên 1930, từng thực hiện các chuyến bay chở khách vượt Đại Tây Dương từ Châu Âu sang Mỹ.

![](https://cdn.beekka.com/blogimg/asset/202409/bg2024090801.webp)

Nó dài 245 mét, tựa như một tàu sân bay trên không, chở được từ 50 đến 70 hành khách. Nội thất bên trong cực kỳ xa hoa với phòng ngủ riêng và nhà hàng. Con người ngày nay khó có thể tưởng tượng được một chuyến bay dài ngày lại có thể thoải mái đến thế.

![](https://cdn.beekka.com/blogimg/asset/202409/bg2024090802.webp)

![](https://cdn.beekka.com/blogimg/asset/202409/bg2024090803.webp)

![](https://cdn.beekka.com/blogimg/asset/202409/bg2024090804.webp)

Túi khí của nó chứa khí hydro nên luôn tiềm ẩn rủi ro cháy nổ. Tháng 5 năm 1937, nó đột ngột bốc cháy khiến hơn 30 người thiệt mạng, và từ đó loại hình phương tiện này cũng biến mất khỏi lịch sử.

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025110615.webp)

## Trích dẫn

**Các công ty công nghệ sa thải hàng loạt để "nuôi AI"**

Tháng trước, Amazon thông báo sa thải 30.000 người, đợt cắt giảm lớn nhất lịch sử công ty. Trước đó, Microsoft sa thải 15.000 người, Meta là 3.600 người, Google cũng cắt giảm hàng trăm vị trí. Tính riêng năm 2025, đã có hơn 180.000 nhân sự ngành Internet mất việc.

Ngược lại, các công ty này đã đổ hơn 300 tỷ USD vào AI trong năm nay. Họ sa thải để "dành ngân sách đầu tư cho AI". Nhưng vấn đề là họ thực sự chẳng tiết kiệm được gì. Chi phí cho AI vượt xa số tiền tiết kiệm được từ việc cắt giảm nhân sự. Hơn nữa, những khoản đầu tư khổng lồ này vẫn chưa mang lại lợi nhuận tương xứng, phí sử dụng từ người dùng chẳng thấm tháp gì so với chi tiêu.

Vậy dòng tiền khổng lồ đó đi đâu? Câu trả lời là họ đang mua bán lẫn nhau. Apple trả tiền cho Google, Google trả tiền cho Nvidia, Nvidia trả tiền cho TSMC để sản xuất thiết bị. Việc mua bán chéo này đẩy doanh số và giá cổ phiếu của họ lên cao. Công chúng thấy giá tăng lại đổ xô vào mua, tạo nên một "Thất đại khổng lồ" (Apple, Microsoft, Nvidia, Amazon, Alphabet, Meta, Tesla) với tổng vốn hóa 17 nghìn tỷ USD.

Tại sao cổ phiếu của họ lại có giá trị cao như vậy? Vì mọi người tin rằng AI sẽ mang lại lợi nhuận khổng lồ trong tương lai. Nhưng thực tế là hiện tại họ chưa kiếm được tiền từ AI, họ chỉ đang tiêu tiền cho nhau để tạo ra ảo tưởng về sự tăng trưởng. Tệ hơn nữa là họ không thể dừng lại. Chỉ cần một bên ngừng đầu tư, giá cổ phiếu sẽ sụp đổ ngay lập tức. Cả hệ thống AI hiện nay đang được xây dựng trên những khoản đầu tư xoay vòng, và mọi người đang đánh cược rằng cuộc chơi này sẽ không dừng lại cho đến ngày gặt hái thành quả.

## Phát ngôn

1. Tôi từng nói sẽ không bao giờ có htmx phiên bản thứ 3, nhưng tôi chưa bao giờ nói là không có phiên bản thứ 4. -- Carson Gross, người sáng lập htmx, vừa thông báo nhảy thẳng lên bản 4.0.

2. Chúng tôi nhận được báo cáo từ Google về một lỗ hổng trong code của mình. Chúng tôi rất coi trọng bảo mật, nhưng việc một gã khổng lồ Internet dùng AI để quét mã nguồn của các tình nguyện viên rồi yêu cầu họ sửa lỗi miễn phí, liệu có thực sự công bằng không? -- Đội ngũ FFmpeg

3. Trong thập kỷ tới, hơn 70 nghìn tỷ USD tài sản thừa kế sẽ được chuyển giao trực tiếp cho những người kế vị trên toàn cầu, điều này sẽ làm trầm trọng thêm sự bất bình đẳng xã hội. -- Tờ The Guardian

4. Tại sao sự may mắn lại quan trọng? Vì nó rút ngắn thời gian tích lũy và đưa bạn đến gần những cơ hội lớn hơn. Giống như khi bạn đã có tiền, việc kiếm thêm nhiều tiền hơn nữa sẽ trở nên dễ dàng hơn nhiều. -- Cuộc đời là một trò chơi xác suất

5. Sau khi AI xuất hiện, định hướng phát triển của lập trình viên đã hoàn toàn thay đổi. Bạn phải tập trung vào việc hiểu hệ thống thay vì hiểu cú pháp. Kỹ năng của bạn phải chuyển từ viết code sang kiến trúc, bảo mật và hiệp tác giữa người và máy. Tương lai thuộc về những người có khả năng hình dung và duy trì các hệ thống phức tạp. -- Sự tiến hóa của phát triển phần mềm

(Hết)
