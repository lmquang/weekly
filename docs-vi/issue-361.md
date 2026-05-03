---
date: 2025-08-15
tags: ["tor", "dark web", "bảo mật", "security", "an ninh mạng", "android", "linux", "ai", "css", "startup"]
---

# Darknet Tor có thực sự an toàn?

## Ảnh bìa

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081404.webp)

Tháp Thời gian Yên Đài mới hoàn thành năm ngoái là một công trình văn hóa ven biển độc đáo. Tầng dưới là nhà hát ngoài trời, giữa là đài quan sát biển, còn tầng trên là thư viện, phòng triển lãm và quán cà phê. ([via](https://www.archiposition.com/items/20241105014028))

## Darknet Tor có thực sự an toàn?

Chắc hẳn bạn đã nghe nói về trình duyệt Tor, đúng không? Nó vốn là công cụ chính để truy cập vào "dark web" (web tối).

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081008.webp)

Hiểu một cách đơn giản, dark web là những phần của internet mà trình duyệt thông thường không thể mở được. Bạn bắt buộc phải dùng công cụ chuyên dụng.

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081007.webp)

Lý do dark web cần công cụ riêng là vì nó được thiết kế đặc biệt để đảm bảo tính ẩn danh cực cao cho người dùng. Nếu bạn muốn thực hiện những thao tác bí mật trên mạng, dark web là nơi dành cho bạn. Tương tự, những trang web ngầm không muốn bị lộ diện sẽ tạo ra phiên bản dark web với tên miền .onion, thứ mà chỉ Tor mới có thể mở được.

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081310.webp)

Tôi từng tin rằng Tor vô cùng an toàn. Thiết kế của nó chống lại việc truy vết bằng cách không kết nối trực tiếp đến trang web mục tiêu, mà đi qua các nút trung gian ngẫu nhiên.

Quy định là phải qua ít nhất 3 nút trung gian. Mỗi nút chỉ biết nút trước và nút sau nó, nên dù một nút có bị hack, hacker cũng không thể thấy được toàn bộ lộ trình. Về lý thuyết, chỉ khi cả 3 nút đều bị chiếm quyền điều khiển thì danh tính người dùng mới bị lộ. Mà các nút này lại nằm rải rác khắp thế giới, khả năng cả 3 cùng bị hack là cực kỳ thấp.

Thiết kế này được gọi là "định tuyến hành" (onion routing). Giống như bóc một củ hành, bạn phải bóc từng lớp vỏ mới biết được lõi bên trong. Thực tế, Tor chính là từ viết tắt của "The Onion Router".

Thế nhưng, tuần trước tôi đọc được [một bài viết](https://thereader.mitpress.mit.edu/the-secret-history-of-tor-how-a-military-project-became-a-lifeline-for-privacy/) khiến niềm tin đó bị lung lay tận gốc. Tôi bàng hoàng nhận ra: Tor được phát triển bởi chính phủ Mỹ.

Năm 1997, Phòng Thí nghiệm Nghiên cứu Hải quân Mỹ (NRL) đã phát minh ra Tor. Động cơ ban đầu là để ngăn chặn chính phủ nước ngoài theo dõi các liên lạc nhạy cảm của Mỹ.

Các nhân viên tình báo Mỹ ở nước ngoài cần gửi tin mật về trụ sở mà không muốn bị chính phủ sở tại phát giác, nhưng họ buộc phải dùng hạ tầng mạng dân dụng của nước đó. Giải pháp chính là Tor. Thông qua định tuyến hành, các nhà cung cấp internet nước ngoài không thể biết được vị trí người gửi hay địa chỉ người nhận.

Năm 2004, chính phủ Mỹ công khai mã nguồn dự án. Tổ chức Electronic Frontier Foundation (EFF) tiếp quản và phát triển thành Tor ngày nay, nhưng thiết kế lõi vẫn giữ nguyên.

Đáng chú ý là sau khi mở mã nguồn, chính phủ Mỹ vẫn không hề buông tay. Suốt nhiều năm, họ vẫn tài trợ rất lớn cho dự án này. Năm 2012, 80% ngân sách 2 triệu đô của dự án Tor đến từ chính phủ Mỹ. Theo báo cáo tài chính mới nhất 2023-2024, trong tổng doanh thu 7,9 triệu đô, vẫn có hơn 2 triệu đô đến từ các cơ quan chính phủ.

Tại sao chính phủ Mỹ lại đổ tiền vào đây? Đơn giản vì nó có giá trị sử dụng cho họ.

Tôi tin rằng mã nguồn của Tor là đáng tin cậy vì nó được các lập trình viên khắp thế giới soi xét. Nhưng chính phủ Mỹ hiểu rõ từng chi tiết nhỏ nhất trong đó. Họ hoàn toàn có thể triển khai các phiên bản tùy chỉnh của riêng mình.

Nhiều nguồn tin tiết lộ rằng một phần lớn các nút trung gian của Tor là do chính phủ Mỹ thiết lập. Vì vậy, đừng bao giờ mặc định rằng Tor là an toàn tuyệt đối trước sự giám sát của các cơ quan tình báo Mỹ.

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081009.webp)

Hãy nhìn vào trường hợp của "Silk Road" (Con đường tơ lụa), thị trường ngầm lừng lẫy một thời hoạt động hoàn toàn trên Tor. Năm 2013, nó bị đánh sập và nhà sáng lập bị bắt. Đó là một minh chứng sống cho thấy Tor không hề "bất khả xâm phạm".

## Tin tức công nghệ

1. Tại huyện Hoài Lai, tỉnh Hà Bắc, Trung Quốc đã thực hiện thử nghiệm cất cánh và hạ cánh cho tàu đổ bộ mặt trăng có người lái "Lanyue".

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081401.webp)

Nó được treo dưới một đĩa thép lớn điều khiển bằng dây cáp để mô phỏng trọng lực yếu trên Mặt Trăng.

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081402.webp)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081403.webp)

2. Đại học Pennsylvania vừa công bố một nghiên cứu cho thấy có thể khôi phục nội dung cuộc gọi chỉ bằng cách theo dõi các rung động cực nhỏ của điện thoại.

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081102.webp)

Khi đàm thoại, loa điện thoại sẽ rung. Sử dụng radar laser từ khoảng cách 3 mét, các nhà nghiên cứu có thể cảm nhận những rung động này và khôi phục lại giọng nói. Sau đó, họ dùng mô hình Whisper để chuyển giọng nói thành văn bản với độ chính xác khoảng 60%.

3. Một lập trình viên người Mỹ đã chế tạo một màn hình pixel bằng gỗ.

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081115.webp)

Mỗi điểm ảnh là một khối gỗ nhỏ với một mặt được sơn đen.

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081116.webp)

Bộ điều khiển là một chiếc Raspberry Pi. Khi nhận được hình ảnh, nó sẽ tính toán xem khối gỗ nào cần xoay, sau đó điều khiển một cánh tay cơ học thực hiện việc đó.

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081118.webp)

Kết quả trông rất nghệ thuật.

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081117.webp)

4. Google tiết lộ hệ thống cảnh báo động đất toàn cầu được tích hợp sẵn trong Android.

![](https://cdn.beekka.com/blogimg/asset/202507/bg2025072804.webp)

Mọi điện thoại Android đều có gia tốc kế để xoay màn hình. Cảm biến này có thể phát hiện sự di chuyển của điện thoại. Nếu hệ thống thấy nhiều điện thoại trong cùng một khu vực cùng rung lên đột ngột, nó sẽ xác định có động đất và gửi cảnh báo ngay lập tức. Hệ thống này đã hoạt động tại 98 quốc gia và từng gửi cảnh báo chính xác trong các vụ động đất ở Philippines và Nepal năm 2023.

5. Tại sao chúng ta cần ngủ? Một bài báo gần đây chỉ ra rằng giấc ngủ liên quan đến ti thể trong tế bào.

![](https://cdn.beekka.com/blogimg/asset/202507/bg2025073012.webp)

Trong trạng thái hiếu khí, hoạt động liên tục của ti thể dẫn đến sự phân đôi, vì vậy cần một giai đoạn nghỉ ngơi (ngủ) để sửa chữa và nạp lại năng lượng. Kết luận là: chừng nào sinh vật còn cần oxy, chừng đó nó còn cần ngủ.

## Bài viết

1. [Nhập môn về định vị neo (Anchor Positioning)](https://webkit.org/blog/17240/a-gentle-introduction-to-anchor-positioning/) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081307.webp)

Cú pháp CSS mới giúp định vị các menu pop-up dựa trên một phần tử neo mà không cần dùng đến JavaScript.

2. [Sử dụng Rclone để gắn ổ đĩa đám mây vào máy tính](https://blog.fernvenue.com/archives/mount-cloud-drive-using-rclone/) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202312/bg2023121003.webp)

Hướng dẫn sử dụng công cụ Rclone để biến các dịch vụ như OneDrive thành một thư mục cục bộ trên máy.

3. [Cách lựa chọn phông chữ tiếng Anh](https://imperavi.com/books/ui-typography/basis/choosing-typeface/) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081309.webp)

Những lưu ý quan trọng để chọn được phông chữ phù hợp cho thiết kế giao diện.

4. [Cách tôi sử dụng NotebookLM](https://www.xda-developers.com/using-notebooklm-to-watch-a-show/) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081110.webp)

NotebookLM hiện được coi là công cụ ghi chú AI tốt nhất. Tác giả chia sẻ cách dùng nó để "xem" những bộ phim dài tập mà không tốn thời gian.

5. [Cách chạy phần mềm có giao diện trong Docker](https://github.com/hemashushu/docker-archlinux-gui) (Tiếng Anh)

Sử dụng giao thức Wayland để chạy các ứng dụng đồ họa ngay bên trong container Docker.

6. [Tại sao π² ≈ g?](https://roitman.io/blog/91) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202408/bg2024081406.webp)

π² bằng 9.86, rất gần với gia tốc trọng trường g (9.8). Đây không phải là sự trùng hợp ngẫu nhiên mà có liên quan đến cách định nghĩa đơn vị mét.

## Công cụ

1. [Battery](https://github.com/actuallymentor/battery)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081103.webp)

Công cụ nhỏ cho Macbook giúp giới hạn mức sạc pin ở 80% để bảo vệ tuổi thọ pin.

2. [Readeck](https://readeck.org)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081108.webp)

Ứng dụng web tự lưu trữ để quản lý dấu trang và tự động lưu nội dung trang web.

3. [missing.css](https://missing.style/)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081308.webp)

Thư viện CSS cung cấp giải pháp tạo kiểu tinh gọn và dễ mở rộng.

4. [My idlers](https://github.com/cp6/my-idlers)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081109.webp)

Ứng dụng web tự lưu trữ giúp quản lý tập trung các VPS, hosting và tên miền của bạn.

5. [Kimu](https://trykimu.com/)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081113.webp)

Trình chỉnh sửa video dựa trên web, hỗ trợ tích hợp AI và hoàn toàn mã nguồn mở.

6. [vYinn](https://github.com/shanleiguang/vYinn)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025080901.webp)

Công cụ tạo các họa tiết con dấu theo phong cách cổ điển.

7. [Call-Me](https://github.com/miroslavpejic85/call-me)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025080902.webp)

Trang web mã nguồn mở hỗ trợ gọi video trực tiếp trên trình duyệt.

8. [Modern MD Editor](https://github.com/xiaobox/mdeditor)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081101.webp)

Trình chỉnh sửa Markdown hỗ trợ tạo mã HTML trực quan tương thích tốt với các nền tảng mạng xã hội.

9. [FluentRead](https://github.com/Bistutu/FluentRead)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081202.webp)

Tiện ích trình duyệt mã nguồn mở, một lựa chọn thay thế cho Immersive Translate, hỗ trợ nhiều công cụ dịch và AI.

10. [Diff Excel](https://github.com/zbuzhi/diff-excel)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081204.webp)

Ứng dụng máy tính mã nguồn mở viết bằng Go dùng để so sánh sự khác biệt giữa hai bảng tính Excel.

## AI

1. [LLM from URL](https://818233.xyz/)

Một cách thú vị để đặt câu hỏi cho AI trực tiếp qua thanh địa chỉ URL.

2. [AI Short Video Factory](https://github.com/YILS-LIN/short-video-factory)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081203.webp)

Ứng dụng web mã nguồn mở giúp tự động tạo video ngắn và kịch bản từ các tài liệu tải lên.

3. [Mapedia.cc](https://mapedia.cc/)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081305.webp)

Bản đồ AI giúp người dùng tìm kiếm một chủ đề và hiển thị các bản đồ liên quan kèm bài giải thích chi tiết.

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081306.webp)

## Tài nguyên

1. [One Million Screenshots](https://onemillionscreenshots.com)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081104.webp)

Một trang web tập hợp 1 triệu ảnh chụp màn hình từ internet, bạn có thể phóng to thu nhỏ để khám phá.

2. [Engineering.fyi](https://engineering.fyi/)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081105.webp)

Nơi tổng hợp các bài viết kỹ thuật chất lượng từ các công ty công nghệ lớn trên thế giới.

3. [Touch Mapper](https://touch-mapper.org/en/)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081011.webp)

Một ý tưởng tuyệt vời: bạn nhập địa chỉ, trang web sẽ xuất ra file bản đồ 3D để in ra cho người khiếm thị sử dụng.

4. [Pricing Pages Design](https://pricingpages.design/)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081205.webp)

Bộ sưu tập các thiết kế trang bảng giá (pricing page) đa dạng.

## Hình ảnh

1. [Tượng cổ điển và Thời trang hiện đại](https://www.itsnicethat.com/articles/leo-caillard-hipster-in-stone)

Một nhiếp ảnh gia người Pháp đã khoác lên mình các bức tượng cổ điển những bộ trang phục thời thượng nhất ngày nay.

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081001.webp)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081002.webp)

Sự kết hợp này mang lại một cảm giác vô cùng mới mẻ và thú vị.

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081003.webp)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081004.webp)

Nó cho thấy phong thái của một người phụ thuộc rất nhiều vào cách ăn mặc.

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081005.webp)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025081006.webp)

## Trích đoạn

1\. Kỹ năng của tôi đã thụt lùi

Năm năm trước, khi mới tốt nghiệp đại học, tôi cực kỳ say mê phát triển phần mềm và tham gia vào hàng loạt dự án mã nguồn mở. Tôi đã dành hàng ngàn giờ cho chúng mà không cần thù lao, đơn giản vì tôi tận hưởng quá trình đó và người dùng cũng đánh giá rất cao công việc của tôi.

Ra trường, tôi cứ ngỡ các công ty sẽ săn đón mình nhờ những đóng góp đó. Nhưng tôi đã nhầm. Tôi nộp hơn 600 hồ sơ và chỉ nhận được 3 lời mời làm việc. Cuối cùng, tôi chọn một startup. Ban ngày tôi làm việc 9 tiếng cho công ty, tối về lại cày dự án mã nguồn mở đến tận khuya. Lương thấp, nhưng tôi thấy vui vì kỹ năng và tầm ảnh hưởng trong cộng đồng tăng nhanh.

Thế rồi một ngày, tôi nhận ra thực tế phũ phàng: dự án ở công ty chẳng thể hiện được giá trị của tôi, còn những người biết giá trị thực sự của tôi thì lại không phải người trả lương. Tôi bắt đầu chuyển sang luyện LeetCode.

Tôi không còn dành thời gian cho mã nguồn mở nữa, và cộng đồng quanh dự án của tôi cũng dần tan rã. Việc từ bỏ khiến tôi đau lòng, nhưng nhờ thế tôi vào được một tập đoàn lớn với mức lương gấp 5 lần. Tôi dành toàn bộ thời gian cho các dự án của công ty và được sếp khen ngợi. Các email mời gọi nhảy việc bắt đầu gửi đến dồn dập.

Nhưng sâu thẳm trong lòng, tôi biết kỹ năng của mình đang thụt lùi. Các dự án ở công ty rất nhàm chán, không có tính thử thách và chỉ dùng những công nghệ nội bộ cũ kỹ. Hơn nữa, tôi cũng không còn thấy hạnh phúc như trước. Có lẽ tôi sẽ tích cóp một khoản tiền rồi nghỉ hưu sớm sau vài năm nữa, hy vọng lúc đó thế giới mã nguồn mở vẫn còn rộng mở như xưa.

## Trích dẫn

1\.

Cơn cuồng tài trợ cho các công ty AI thật điên rồ. Ilya Sutskever, cựu khoa học gia trưởng của OpenAI, đã huy động được 1 tỷ đô vào năm 2024, và vài tháng trước lại thêm 2 tỷ đô nữa, định giá công ty lên tới 32 tỷ đô. Theo tôi biết, sản phẩm duy nhất của họ chỉ là 370 từ trên trang web, tính ra mỗi từ trị giá hơn 80 triệu đô. Mà trong đó 148 từ còn là để nói về việc các cộng sự rời bỏ công ty. Nhưng ít nhất ông ấy còn có cái trang web, chứ nhiều nhà sáng lập khác cầm tiền xong là biến mất hút luôn.

-- [Substack Weekly](https://theahura.substack.com/p/tech-things-genies-lamp-openai-cant)

2\.

Các công ty bảo hiểm đang cực kỳ lo ngại. Khi Trái đất nóng lên và các hiện tượng thời tiết cực đoan ngày càng nhiều, rủi ro mất mát tài sản tăng vọt đến mức thế giới sắp trở thành nơi "không thể bảo hiểm" được nữa.

-- [Thế giới sẽ sớm không thể tham gia bảo hiểm](https://www.cnbc.com/2025/08/08/climate-insurers-are-worried-the-world-could-soon-become-uninsurable-.html)

3\.

Các gói cập nhật của Windows 11 ban đầu được gọi là gói mùa Xuân và mùa Thu. Sau đó, vì có phản hồi rằng điều này không phù hợp với người dân ở Nam bán cầu, Microsoft đã đổi tên chúng thành H1 và H2.

-- [Tại sao các bản cập nhật Windows lại gọi là H1 và H2](https://devblogs.microsoft.com/oldnewthing/20250805-00/?p=111435)

4\.

Trong hơn một thập kỷ, các trại huấn luyện lập trình (coding bootcamps) là trụ cột của Thung lũng Silicon. Giờ đây, AI khiến các công ty giảm tuyển dụng nhân sự cấp thấp, cộng thêm việc sinh viên có thể tự học qua AI, khiến các trung tâm này đang dần biến mất.

-- [Reuters](https://www.reuters.com/lifestyle/bootcamp-bust-how-ai-is-upending-software-development-industry-2025-08-09/)

5\.

Nhiều người tưởng rằng mình đang suy nghĩ, nhưng thực chất họ chỉ đang sắp xếp lại những thành kiến của chính mình.

-- [William James](https://quoteinvestigator.com/2017/05/10/merely/), triết gia người Mỹ
