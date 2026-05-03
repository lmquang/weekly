---
date: 2025-11-14
tags: [Data Model, Mô hình dữ liệu, Product Management, Quản lý sản phẩm, Database, Cơ sở dữ liệu, Programming, Lập trình, AI, Tech]
---

# Mô hình dữ liệu là cốt lõi của sản phẩm mới

## Ảnh bìa

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025111108.webp)

Khu di tích Huyền Tuyền Trí tại thành phố Tửu Tuyền, tỉnh Cam Túc mới mở cửa năm nay. Đây từng là một trạm dừng chân trên Con đường Tơ lụa thời nhà Hán, dành cho khách đi lại giữa vùng Tây Vực. Trong số hơn 80.000 thẻ tre nhà Hán còn tồn tại ở Trung Quốc, có tới hơn 30.000 thẻ được tìm thấy tại trạm dừng này. ([via](https://www.news.cn/culture/20250430/2dfefaf471ca46f48e70d1ab669ef6e9/c.html?page=5))

## Mô hình dữ liệu là cốt lõi của sản phẩm mới

(1)

Niklaus Wirth, nhà khoa học máy tính lỗi lạc và là cha đẻ của ngôn ngữ Pascal, từng để lại một câu nói kinh điển:

> Thuật toán + Cấu trúc dữ liệu = Chương trình

Ông thậm chí còn viết hẳn một cuốn sách lấy tên chính là câu nói này.

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025110804.webp)

Trong mắt Wirth, **cấu trúc dữ liệu quan trọng ngang hàng với thuật toán**, còn ngôn ngữ lập trình chỉ là thứ yếu. Nếu cấu trúc dữ liệu sai, chương trình cầm chắc thất bại. Ngược lại, khi cấu trúc dữ liệu đúng, cách giải quyết vấn đề thường sẽ tự hiện ra một cách rõ ràng.

(2)

Gần đây tôi có đọc được [một bài viết](https://notes.mtb.xyz/p/your-data-model-is-your-destiny) cũng ủng hộ quan điểm này. Tác giả còn tiến thêm một bước khi khẳng định rằng: **Mô hình dữ liệu không chỉ là cốt lõi của chương trình, mà còn là linh hồn của mọi sản phẩm mới.**

Cấu trúc dữ liệu quyết định hình thái của sản phẩm. Đôi khi chỉ cần thay đổi mô hình dữ liệu, bạn sẽ có ngay một sản phẩm hoàn toàn mới. Những ví dụ dưới đây thực sự rất gợi mở.

(3)

Ban đầu, các phần mềm chat đều lấy con người làm trung tâm. Hai hoặc nhiều người kết nối lại tạo thành một cuộc hội thoại.

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025110807.webp)

Mô hình dữ liệu này xoay quanh người dùng. Nếu mọi thành viên rời đi, cuộc hội thoại coi như kết thúc.

Thế rồi [Slack](https://slack.com/intl/zh-cn/) ra đời. Mô hình dữ liệu của nó đã thay đổi: Cốt lõi không còn là con người mà là chủ đề. Mỗi chủ đề là một "vỏ chứa" (container) chứa mọi cuộc thảo luận liên quan, hay còn gọi là các kênh (channel).

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025110805.webp)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025110806.webp)

Dù mọi người có rời đi, kênh đó vẫn tồn tại. Toàn bộ ngữ cảnh của chủ đề không hề mất đi. Thành viên mới tham gia có thể xem lại toàn bộ lịch sử thảo luận trước đó. Chính nhờ thay đổi nhỏ trong mô hình dữ liệu này, Slack đã đánh bại các đối thủ và trở thành lựa chọn hàng đầu cho giao tiếp nội bộ doanh nghiệp.

(4)

Hãy nhìn vào Notion và Google Docs. Cả hai đều dùng để soạn thảo văn bản, nhưng mô hình dữ liệu lại khác biệt hoàn toàn.

Google Docs dùng mô hình truyền thống, lấy từng tệp văn bản làm trung tâm.

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025110808.webp)

Trong khi đó, cốt lõi của Notion không phải là văn bản mà là Trang (Page). Một trang là một vỏ chứa, nơi bạn có thể kết hợp nhiều khối nội dung và tài liệu khác nhau để hiển thị cùng nhau.

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025110809.webp)

Figma và Photoshop cũng tương tự. Tâm điểm của Photoshop là hình ảnh, mọi chỉnh sửa đều thuộc về một bức ảnh cụ thể.

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025110810.webp)

Nhưng với Figma, cốt lõi chính là Không gian làm việc (Workspace). Một bản thiết kế là một không gian làm việc chứa được nhiều hình ảnh, nơi nhiều người có thể cùng tham gia và để lại bình luận.

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025110811.webp)

(5)

Tóm lại, chỉ cần một thay đổi nhỏ trong mô hình dữ liệu là có thể tạo ra một sản phẩm mới, mở ra một thị trường hoàn toàn khác. Nếu sản phẩm của bạn đang quá giống với những gì đã có, hãy thử suy nghĩ xem liệu có thể thay đổi mô hình dữ liệu hay không.

## Tin tức công nghệ

1. **Điện miễn phí tại Úc**

Úc đã lắp đặt một lượng khổng lồ các tấm pin năng lượng mặt trời, dẫn đến một rắc rối mới: Điện dư thừa quá nhiều vào ban ngày. Chính phủ đang dự định tung ra kế hoạch [miễn phí tiền điện](https://electrek.co/2025/11/04/australia-has-so-much-solar-that-its-offering-everyone-free-electricity-3h-day/) vào buổi trưa, khi ánh nắng mạnh nhất. Các công ty điện lực sẽ phải cung cấp ít nhất 3 giờ dùng điện miễn phí mỗi ngày cho mọi người. Nếu bạn có pin lưu trữ, bạn thậm chí có thể dùng điện miễn phí cả ngày.

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025110902.webp)

2. **Quảng cáo AI phủ kín tàu điện ngầm New York**

Gần đây, các ga tàu điện ngầm ở New York đồng loạt xuất hiện [quảng cáo về một thiết bị AI](https://archive.ph/HyMHm). Đó là một chiếc dây chuyền AI có giá 129 USD, cho phép người đeo trò chuyện trực tiếp với nó.

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025101402.webp)

![](https://cdn.beekka.com/blogimg/asset/202510/bg2025101403.webp)

Công ty này đã chi gần 1 triệu USD mỗi tháng cho quảng cáo, nhưng sau một tháng rưỡi chỉ bán được 3.100 sản phẩm, thu về chưa đầy 400.000 USD. Một khoản đầu tư lỗ nặng, nhưng CEO của họ vẫn rất lạc quan. Anh tin rằng khi sản phẩm lên kệ tại Walmart, doanh số sẽ tăng vọt vì mọi người đều cần một "người bạn đồng hành AI" để cải thiện trí tuệ cảm xúc.

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025111305.webp)

3. **"Ô bắt gió" khổng lồ tại Nội Mông**

Một chiếc "ô bắt gió" lớn nhất thế giới vừa thử nghiệm thành công việc bung và thu ô tại Nội Mông. Với diện tích lên tới 5.000 mét vuông, nó hoạt động giống như một chiếc diều khổng lồ bay ở độ cao trên 300 mét để thu hoạch năng lượng gió rồi truyền qua dây cáp kéo máy phát điện dưới mặt đất.

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025111211.webp)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025111212.webp)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025111213.webp)

4. **Spatial Personas trên Vision Pro**

Hệ điều hành VisionOS 2 mới của Apple vừa bổ sung tính năng [Spatial Personas](https://www.cnet.com/tech/computing/apple-talks-to-me-about-vision-pro-personas-where-is-our-virtual-presence-headed/). Bằng cách sử dụng camera bên trong và thuật toán Gaussian Splatting, hệ thống có thể biến ảnh chân dung 2D thành một hình đại diện 3D sống động.

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025110508.webp)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025110509.webp)

Khi gọi điện, bạn sẽ thấy đối phương như đang lơ lửng trước mặt với biểu cảm và cử động thời gian thực. Tính năng này hỗ trợ tới 5 người cùng lúc, mở ra viễn cảnh chúng ta có thể thực sự "gặp mặt" nhau trong không gian ảo.

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025110510.webp)

## Bài viết

1. [Lời kêu cứu của một lập trình viên Iran](https://gist.github.com/EchenD/8b211ebfa4941d2c5df7b526790b31aa#the-current-situation-being-completely-honest) (Tiếng Anh)

Một lập trình viên Iran tạo ra công cụ tạo avatar AI nhưng không thể bán ra quốc tế vì lệnh trừng phạt của Mỹ. Anh chia sẻ trên GitHub về hoàn cảnh bế tắc khi không thể sử dụng Stripe, PayPal hay các dịch vụ đám mây như AWS, GCP, Azure, khiến sản phẩm của anh không thể mang lại thu nhập dù vợ anh phải làm việc vất vả từ sáng sớm đến tối muộn.

2. [Tôi ghét việc chụp ảnh màn hình code](https://parkscomputing.com/page/i-hate-screenshots-of-text) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025111201.webp)

Một lập trình viên kêu gọi khách hàng đừng gửi ảnh chụp màn hình khi gặp lỗi nữa. Việc này khiến anh không thể copy code để kiểm tra, thay vào đó hãy gửi link dẫn đến mã nguồn.

3. [Dùng ảnh thay chữ có giúp tiết kiệm Token không?](https://pagewatch.ai/blog/post/llm-text-as-image-tokens/) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025110802.webp)

Bài viết kiểm chứng xem liệu việc chuyển Prompt từ văn bản sang hình ảnh có giúp tiết kiệm Token không. Kết quả là bản thân Prompt thì tiết kiệm được, nhưng mô hình lại tốn nhiều Token hơn để hiểu ngữ cảnh, nên tổng cộng không hề rẻ hơn.

4. [Hình minh họa chi tiết về thuật toán Dijkstra](https://github.com/trekhleb/javascript-algorithms/blob/master/src/algorithms/graph/dijkstra/README.zh-CN.md) (Tiếng Trung)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025111207.webp)

Dijkstra là thuật toán kinh điển để tìm đường đi ngắn nhất giữa hai điểm. Bài viết giải thích từng bước một cách trực quan qua hình ảnh.

5. [Trải nghiệm Web Monetization API](https://blog.tomayac.com/2025/11/07/using-the-web-monetization-api-for-fun-and-profit/) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025110803.webp)

Trình duyệt có một API thử nghiệm cho phép khách truy cập quyên góp trực tiếp cho chủ trang web. Đây là bài báo cáo về quá trình dùng thử nó.

6. [So sánh chi phí các plugin AI cho lập trình](https://blog.kilocode.ai/p/testing-augment-codes-new-credit) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025111306.webp)

Bài viết so sánh chi phí thực tế giữa [Augment Code](https://www.augmentcode.com) (dùng Claude Sonnet 4.5 cố định) và [Kilo Code](https://kilocode.ai/) (cho phép tự cấu hình mô hình riêng).

## Công cụ

1. [MagicMirror²](https://github.com/MagicMirrorOrg/MagicMirror)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025110901.webp)

Ứng dụng bảng thông tin có thể dùng cho màn hình hiển thị hoặc gương thông minh.

2. [btop](https://github.com/aristocratos/btop)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025111208.webp)

Bản nâng cấp của lệnh htop, hiển thị thông tin hệ thống một cách chi tiết và đẹp mắt trong Terminal.

3. [DroidDock](https://github.com/rajivm1991/DroidDock)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025111206.webp)

Ứng dụng Mac giúp kết nối và quản lý file trên điện thoại Android.

4. [RedisFX](https://github.com/tanhuang2016/RedisFX)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025110801.webp)

Giao diện đồ họa (GUI) nhẹ nhàng cho Redis, viết bằng JavaFX chạy trên JVM.

5. [Pingap](https://github.com/vicanso/pingap)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025111007.webp)

Server Reverse Proxy viết bằng Rust tương tự nginx, tích hợp sẵn nhiều plugin bảo mật và quản lý lưu lượng.

6. [Alle](https://github.com/bestruirui/Alle)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025111008.webp)

Nền tảng quản lý email tập trung, triển khai trên Cloudflare Workers và hỗ trợ xử lý email bằng AI.

7. [gocron](https://github.com/gocronx-team/gocron)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025111010.webp)

Hệ thống quản lý tác vụ định kỳ (cron job) cho Linux viết bằng Go, có giao diện web để thay thế crontab truyền thống.

8. [markdown-it-ts](https://github.com/Simon-He95/markdown-it-ts)

Bản viết lại bằng TypeScript của thư viện parse Markdown nổi tiếng markdown-it.

9. [TUIOS](https://github.com/Gaurav-Gosain/tuios)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025111109.webp)

Một trình quản lý cửa sổ ngay bên trong Terminal, cho phép quản lý nhiều phiên làm việc cùng lúc.

10. [XMSLEEP](https://github.com/Tosencen/XMSLEEP)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025111215.webp)

Ứng dụng tạo tiếng ồn trắng (white noise) nguồn mở cho Android.

## Liên quan đến AI

1. [Davia](https://github.com/davialabs/davia)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025111203.webp)

Công cụ nguồn mở dùng AI để biến toàn bộ kho mã nguồn thành một bộ tài liệu trực quan.

2. [VoidMuse](https://github.com/voidmuse-dev/voidmuse)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025111009.webp)

Plugin AI hỗ trợ IDEA và VS Code, mã nguồn mở phục vụ mục đích giảng dạy cách phát triển trợ lý lập trình.

3. [UPage](https://github.com/halo-dev/upage)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025111012.webp)

Nền tảng xây dựng website trực quan dựa trên mô hình lớn, một lựa chọn thay thế nguồn mở cho Lovable.

4. [Pair Translate](https://github.com/Cookee24/PairTranslate)

Plugin trình duyệt hỗ trợ dịch thuật bằng cách kết nối với các mô hình AI hoặc dịch vụ bên thứ ba.

5. [DatasetLoom](https://github.com/599yongyang/DatasetLoom)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025111216.webp)

Ứng dụng Web giúp xây dựng dữ liệu huấn luyện cho các mô hình đa phương thức.

6. [Cordys CRM](https://github.com/1Panel-dev/CordysCRM)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025111011.webp)

Hệ thống quản lý khách hàng (CRM) tích hợp AI nguồn mở.

## Tài nguyên

1. [stickertop.art](https://stickertop.art/main/)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025111204.webp)

Trang web tổng hợp những bức ảnh chụp laptop được dán đầy sticker.

2. [Trực quan hóa kiểu dữ liệu TypeScript](https://types.kitlangton.com/)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025111301.webp)

Giải thích các kiểu dữ liệu trong TypeScript bằng hình ảnh sinh động.

3. [Tỷ lệ sử dụng tiền mặt của các quốc gia](https://www.voronoiapp.com/economy/Who-Still-Uses-Cash-7090)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025111302.webp)

Thống kê tỷ lệ dùng tiền mặt năm 2025. Trung Quốc là một trong những nước thấp nhất với chỉ 10%.

## Hình ảnh

1. **Đề thi đầu vào của MIT**

Đây là đề thi môn đại số trong kỳ thi nhập học của MIT năm 1869 (năm Đồng Trị thứ 8 thời nhà Thanh).

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025111210.webp)

2. **Chữ tượng hình Ai Cập cổ đại**

Một lập trình viên Iceland nhờ chuyên gia dịch câu "hello world" sang chữ tượng hình Ai Cập cổ. Vì người Ai Cập cổ không có khái niệm "thế giới" (world), câu này được dịch sát nghĩa thành "Chào mừng toàn bộ lục địa".

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025111202.webp)

## Trích dẫn

**Công ty càng lớn, sản phẩm càng dễ trở nên phức tạp**

Có hai lý do chính khiến các công ty lớn thường tạo ra những sản phẩm cực kỳ phức tạp.

Thứ nhất, càng nhiều người tham gia, sản phẩm càng rắc rối vì ai cũng muốn để lại dấu ấn cá nhân. Ở các tập đoàn lớn, việc đóng góp tính năng mới là con đường dẫn đến thăng tiến. Ngay cả khi tính năng đó là thừa thãi và vô dụng chỉ sau vài tháng, người tạo ra nó vẫn được khen thưởng. Vì thế, mọi người luôn sốt sắng thêm thắt các tính năng mới.

Thứ hai, quy mô càng lớn, khách hàng càng nhiều, công ty càng phải đối mặt với vô vàn yêu cầu cụ thể. Nhân viên bán hàng hay hỗ trợ khách hàng sẽ liên tục thúc giục bạn thêm tính năng này, yêu cầu kia. Trừ khi bạn có tầm nhìn cực kỳ vững vàng để từ chối những gì không phù hợp với triết lý sản phẩm, nếu không bạn sẽ bị cuốn vào vòng xoáy thêm thắt vô tận.

Trong thực tế, lập trình viên tại các công ty lớn chịu nhiều áp lực và hiếm khi có lập trường riêng. Họ phải làm hài lòng cấp trên và cân bằng giữa các bộ phận, kết quả cuối cùng là một phần mềm khổng lồ và rối rắm.

## Phát ngôn

1. Khác với API thông thường là một cam kết không thể dễ dàng thay đổi, giao diện MCP chỉ dành cho mô hình lớn gọi. Vì mô hình lớn sẽ đọc quy tắc sử dụng một cách linh hoạt mỗi lần, nên chúng ta có thể thay đổi server MCP bất cứ lúc nào mà không gặp vấn đề gì. -- Steve Krouse

2. Nếu bạn chỉ cho mọi người thấy vấn đề, đồng thời đưa ra giải pháp, họ sẽ cảm động và bắt tay vào hành động. -- Bill Gates

3. 25% đá trên bề mặt Trái Đất là đá cacbonat, phần lớn hình thành từ xác các sinh vật hữu cơ. Điều này có nghĩa là rất nhiều khối đá hiện nay từng là những sinh thể sống. -- Suy nghĩ về cái chết

4. Những người đang tung hô lập trình bằng AI liệu có nhận ra rằng AI chắc chắn sẽ mang lại một lượng khổng lồ mã nguồn rác và những khoản "nợ hiểu biết" không? -- Độc giả Hacker News

5. Gần đây tôi tự hỏi, nếu AI có thể dịch ngôn ngữ của chúng ta thành mã nguồn có thể chạy được, liệu chúng ta còn cần đến các ngôn ngữ lập trình nữa không? -- Lập trình không phụ thuộc ngôn ngữ

(Hết)
