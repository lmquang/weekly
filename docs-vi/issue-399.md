---
date: 2026-06-05
tags: ["ai", "trí tuệ nhân tạo", "lập trình", "programming", "trung quốc", "china", "gpu", "startup", "mã nguồn mở", "open source"]
---

# Chuyến thăm các "ông lớn" AI Trung Quốc

## Ảnh bìa

![](https://cdn.beekka.com/blogimg/asset/202606/bg2026060402.webp)

Bảo tàng Mỹ thuật Quốc tế Thâm Quyến vừa khánh thành trong tuần này. ([via](https://sa.trip.com/moments/detail/shenzhen-26-146282837?locale=en-SA))

## Nhật ký thăm các đại gia AI Trung Quốc

Đầu tháng 5 năm nay, một phái đoàn từ Mỹ đã đến Trung Quốc để thăm 14 công ty AI và robot hàng đầu.

![](https://cdn.beekka.com/blogimg/asset/202606/bg2026060104.webp)

Danh sách bao gồm những cái tên đình đám như DeepSeek, Moonshot (Kimi), MiniMax, Zhipu AI, ByteDance, Alibaba, Ant Group, Xiaomi, 01.AI, Unitree, ModelScope và nhiều đơn vị khác.

Các thành viên trong đoàn đều là những nhà phân tích công nghệ dày dạn kinh nghiệm. Sau khi trở về Mỹ, họ đã chia sẻ những góc nhìn sâu sắc: [Kevin Xu](https://interconnect.substack.com/p/chinai-mood-april-26-may-4-2026), [afra Wang](https://afraw.substack.com/p/mandate-of-ai), [Florian Brand](https://florianbrand.com/posts/china-trip), [Nathan Lambert](https://www.interconnects.ai/p/notes-from-inside-chinas-ai-labs), [ Azeem Azhar](https://www.exponentialview.co/p/inside-chinese-ai-labs-efficiency-moat), [Lily Ottinger and Kai Williams](https://archive.md/myA7R), [Jasmine Sun](https://jasmi.news/p/party-in-the-permanent-underclass), [Lingua Sinica](https://linguasinica.substack.com/p/notes-from-a-trip-to-chinas-ai-labs), [Caithrin](https://www.caithrin.com/p/searching-for-amanda-askell-with).

Dưới đây là những ghi chép thú vị nhất mà tôi đã tổng hợp lại. Để đảm bảo mạch đọc trôi chảy, tôi sẽ không trích dẫn cụ thể nguồn của từng đoạn.

### Khoảng cách về năng lực tính toán

Điểm chung lớn nhất mà chúng tôi nghe được ở mọi công ty là lời phàn nàn về việc thiếu hụt năng lực tính toán (compute). Điều này buộc họ phải giảm số lượng thử nghiệm và thu nhỏ quy mô mô hình.

Nguyên nhân chính đến từ các lệnh kiểm soát xuất khẩu chip của Mỹ. Chúng tôi thực sự tò mò muốn tận mắt chứng kiến cách các công ty bản địa xoay xở với tình thế này.

Dù không phải là hoàn toàn bế tắc (họ vẫn có thể sở hữu các dòng card đồ họa như H100, B200 hay B300 của Nvidia), nhưng số lượng họ có ít hơn ít nhất một bậc so với các đối thủ tại Mỹ.

Hãy nhìn vào hệ thống GB300 NVL72 mới nhất của Nvidia (với 72 GPU kết hợp lại). Tốc độ suy luận thời gian thực của nó nhanh gấp 30 lần so với cụm H100 cách đây 3 năm, dung lượng bộ nhớ trên mỗi chip cao gấp 3,6 lần và mức tiêu thụ điện năng cho mỗi lần suy luận giảm tới 25 lần. Trong khi các công ty Mỹ đang đặt hàng hàng loạt các hệ thống này, các công ty Trung Quốc lại không thể làm điều tương tự.

Các tập đoàn công nghệ Trung Quốc, đặc biệt là Huawei, đã có những bước tiến dài trong việc tự nghiên cứu chip AI. Tuy nhiên, ngay cả dòng chip Ascend 950PR mới nhất vừa ra mắt hồi tháng 3 năm nay cũng chỉ có hiệu năng tương đương với H100 vốn đã ra đời từ năm 2022. Thêm vào đó, sản lượng của chúng còn rất hạn chế. Ước tính Nvidia sẽ xuất xưởng khoảng 7 triệu GPU Hopper và Blackwell tính đến tháng 10 năm 2025 và con số này vẫn đang tăng tốc. Huawei dự kiến chỉ giao được 750.000 chip Ascend 950PR trong năm nay, tức là chỉ bằng 1/10 sản lượng năm ngoái của Nvidia.

Hệ quả là Mỹ đang nắm giữ ưu thế áp đảo về compute. Ước tính đến cuối năm 2025, tổng năng lực tính toán của ngành AI Mỹ sẽ gấp khoảng 8 lần Trung Quốc. Toàn bộ hạ tầng compute của các công ty AI Trung Quốc hiện nay chỉ xấp xỉ quy mô của Mỹ vào năm 2023.

Khi chúng tôi chia sẻ số lượng GPU trung bình mà mỗi nghiên cứu viên tại OpenAI đang sở hữu, các đồng nghiệp Trung Quốc đã thực sự bị sốc. Dù vậy, chúng ta đều biết rằng ngay cả những người ở OpenAI hay bất kỳ công ty AI phương Tây nào vẫn luôn than phiền rằng họ không có đủ tài nguyên tính toán.

### Cách phân bổ tài nguyên

Tại Mỹ, phần lớn compute được ưu tiên cho việc huấn luyện mô hình thay vì phục vụ người dùng cuối. Ở Trung Quốc, câu chuyện lại khác hoàn toàn. Tài nguyên vừa phải dùng để huấn luyện, vừa phải gánh vác hàng trăm triệu người dùng cá nhân cùng lượng khách hàng doanh nghiệp đang tăng trưởng chóng mặt.

Việc dành tới một nửa năng lực tính toán để phục vụ khách hàng đồng nghĩa với việc quá trình huấn luyện sẽ bị chậm lại.

Còn một yếu tố khác cần xem xét. Tại Mỹ, compute tập trung chủ yếu vào tay "ngũ đại gia": OpenAI, Anthropic, Google, Meta và xAI. Trong khi đó ở Trung Quốc, mọi công ty công nghệ lớn đều đang ráo riết phát triển mô hình riêng, khiến nguồn tài nguyên vốn đã hạn hẹp lại càng bị chia nhỏ hơn.

### Hiệu quả tính toán

Nếu suy luận theo logic thông thường, khi năng lực tính toán của Trung Quốc tụt hậu so với Mỹ khoảng hai năm, thì các mô hình của họ cũng phải chậm hơn hai năm. Nhưng thực tế không phải vậy.

Nhiều phân tích chỉ ra rằng các mô hình Trung Quốc chỉ kém Mỹ vài tháng. Thậm chí trong một số khía cạnh, hai bên dường như đang chạy song mã.

Lý do là chính các lệnh cấm vận chip đã buộc các công ty Trung Quốc phải tối ưu hóa hiệu quả tính toán đến mức cực đoan. Chúng tôi nhận thấy trí tuệ nhân tạo được tạo ra trên mỗi đơn vị compute của họ cao gấp 4 đến 7 lần so với việc mở rộng quy mô thông thường. Đây chính là cách họ bù đắp cho sự thiếu hụt về phần cứng.

### Sự chia rẽ về mã nguồn mở

Hiện nay, những mô hình mã nguồn mở tốt nhất đều do các công ty Trung Quốc phát hành. Thế nhưng, ngay trong lòng các công ty này cũng đang tồn tại những luồng ý kiến trái chiều về việc có nên tiếp tục mở hay không.

Áp lực về tài chính và doanh thu đang dần thay đổi quan điểm của họ. Hiện nay, một ranh giới đang dần định hình: ngưỡng 1 nghìn tỷ tham số.

Một số công ty cho rằng việc mở nguồn các mô hình từ 1 nghìn tỷ tham số trở lên là một sự lãng phí tài nguyên. Lý do là chẳng ai có thể chạy nổi một mô hình khổng lồ như vậy trên máy cục bộ, trong khi đó lại là kịch bản sử dụng phổ biến nhất của open source. Cách tốt hơn để phát hành những mô hình này là đặt chúng trên hạ tầng đám mây của chính công ty và cung cấp qua API.

Ngược lại, với một số công ty khác, mã nguồn mở gần như là một đức tin. Việc xây dựng những mô hình nghìn tỷ tham số chính là "tấm vé thông hành" để họ gia nhập cuộc chơi mã nguồn mở toàn cầu.

### Tây hóa hay nội địa hóa

Một số công ty AI Trung Quốc mang đậm phong cách phương Tây với bầu không khí năng động, "cool ngầu" kiểu Thung lũng Silicon. Điều này thể hiện ngay cả qua những món quà lưu niệm họ tặng khách.

Ngược lại, một số khác lại đang "Trung Quốc hóa" mạnh mẽ. Họ coi việc xây dựng một phòng trưng bày lộng lẫy là ưu tiên hàng đầu để đón tiếp khách mời, thường là CEO của các doanh nghiệp nhà nước hoặc quan chức địa phương. Sau mỗi buổi tham quan thường là những bữa tiệc chiêu đãi linh đình.

Tôi nghĩ đây vừa là sự lựa chọn, vừa là sự thích nghi dựa trên nền tảng của nhà sáng lập và phân khúc khách hàng mà họ nhắm tới.

### Cái nhìn về đối thủ

Chúng tôi thấy rằng mọi công ty AI tại Trung Quốc đều e dè trước bộ phận Seed của ByteDance. Đây là đội ngũ phát triển AI đóng (closed-source) hàng đầu tại nước này. Họ giống như một "con voi trong phòng" nhưng lại nhảy múa rất điêu luyện. Ứng dụng Doubao của họ gần như độc chiếm lưu lượng người dùng AI, và khả năng đưa mô hình đến với lượng người dùng khổng lồ của họ là điều mà không đối thủ nào bì kịp.

Trong khi đó, DeepSeek lại là cái tên được giới chuyên môn kính trọng nhất. Họ ngày càng đóng vai trò quan trọng trong việc xử lý các tầng nền phảng: từ kiến trúc, hiệu quả, tối ưu hóa suy luận cho đến việc tương thích với hệ sinh thái của Huawei.

### Những thực tập sinh tài năng

Nhân lực tại các công ty AI Trung Quốc phần lớn là những thực tập sinh xuất sắc, độ tuổi trung bình khoảng 25, 26. Hầu hết họ đang là nghiên cứu sinh tiến sĩ và có thể trao đổi kỹ thuật bằng tiếng Anh một cách lưu loát. Đáng chú ý là đa số họ tốt nghiệp tại các trường đại học trong nước và không có trải nghiệm du học.

Họ thực tập từ một đến hai năm, hưởng mọi chế độ và quyền hạn như nhân viên chính thức, được tự do đề xuất ý tưởng và thực hiện các thí nghiệm. Điều này hoàn toàn trái ngược với các công ty AI hàng đầu phương Tây. OpenAI, Anthropic hay Cursor gần như không nhận thực tập sinh. Những nơi khác như Google dù có nhận thực tập cho dự án Gemini nhưng hiếm khi giao cho họ những nhiệm vụ trọng tâm.

Các công ty Trung Quốc đánh giá cao sức trẻ vì họ mang lại những ý tưởng mới mẻ và trí lực dồi dào. Để cải thiện mô hình cuối cùng, các thực tập sinh sẵn sàng làm những công việc âm thầm, ít hào nhoáng. Hơn nữa, những người mới tiếp cận phát triển AI thường không bị gò bó bởi các tư duy cũ.

Từ góc độ các đại học Trung Quốc, tài nguyên tính toán ở trường không đủ để sinh viên phát huy hết tài năng. Việc gửi họ đến các công ty lớn có hạ tầng mạnh mẽ, cùng nhau công bố các công trình nghiên cứu là một hướng đi đôi bên cùng có lợi.

### Thái độ đối với an toàn AI

Khi tôi hỏi các nghiên cứu viên trẻ về trí tuệ nhân tạo tổng quát (AGI), họ đều đưa ra một câu trả lời giống hệt nhau: "AGI là khi AI có thể thay thế tôi!"

Tôi nhận thấy họ không hề lo lắng. Thay vì sợ hãi việc bị chiếm mất công việc, họ lại tò mò xem liệu máy móc có thực sự vượt qua được con người hay không. Nếu điều đó xảy ra, họ sẵn lòng đi làm việc khác.

Đây là sự khác biệt lớn so với các đồng nghiệp phương Tây, những người luôn trăn trở về vấn đề an toàn AI và các tác động xã hội. Các nhà nghiên cứu Trung Quốc cũng coi trọng sự an toàn (ai cũng đồng ý rằng AI không nên làm điều xấu), nhưng họ tin rằng việc thiết lập các quy tắc nên được giao cho chính phủ xử lý.

### Nhu cầu AI của doanh nghiệp

Liệu các doanh nghiệp Trung Quốc có sẵn sàng trả tiền cho dịch vụ AI nội địa?

Có một quan điểm phổ biến rằng thị trường AI Trung Quốc sẽ khó phát triển vì các doanh nghiệp ở đây vốn ít khi chi tiền cho phần mềm.

Tuy nhiên, nhận định này chỉ đúng với mô hình phần mềm dịch vụ (SaaS). Trung Quốc thực tế lại có một thị trường điện toán đám mây cực kỳ khổng lồ.

Các công ty AI đang tranh luận liệu doanh nghiệp sẽ coi AI là một sản phẩm SaaS (thị trường hẹp) hay là hạ tầng đám mây (thị trường rộng). Hiện tại, xu hướng đang nghiêng hẳn về phía điện toán đám mây.

### Ngành công nghiệp dữ liệu còn non trẻ

Chúng tôi nghe nói rằng các công ty như Anthropic hoặc OpenAI chi hơn 10 triệu USD mỗi năm chỉ để mua dữ liệu huấn luyện, với tổng chi phí có thể lên tới hàng trăm triệu USD. Chúng tôi tò mò liệu ở Trung Quốc có như vậy không.

Câu trả lời là ngành công nghiệp dữ liệu thương mại tại đây gần như chưa tồn tại. Nhiều công ty thấy rằng chất lượng dữ liệu mua ngoài rất thấp, nên họ thà tự mình chuẩn bị dữ liệu còn hơn.

Các nghiên cứu viên dành rất nhiều thời gian để xây dựng môi trường huấn luyện học tăng cường (RL). Những ông lớn như ByteDance hay Alibaba thậm chí còn có đội ngũ gán nhãn dữ liệu nội bộ khổng lồ để hỗ trợ công việc này.

### Vai trò của Chính phủ

Ai mới là người đứng sau thúc đẩy lĩnh vực AI tại Trung Quốc, tương tự như Sequoia hay a16z tại Silicon Valley?

Câu trả lời của một người bạn của tôi là: Chính quyền các thành phố như Thượng Hải, Bắc Kinh và Hàng Châu. Những vị quan chức mẫn cán nhưng cũng đầy áp lực này đang bị thúc đẩy bởi tâm lý "sợ bỏ lỡ" (FOMO) và áp lực cạnh tranh gay gắt, từ đó dốc sức thúc đẩy ngành công nghiệp AI tại địa phương.

## [Sự kiện] Trại thực huấn sinh viên XEngineer

Dành cho các bạn sinh viên quan tâm đến việc phát triển năng lực trong kỷ nguyên AI để không bị chìm nghỉm giữa hàng ngàn hồ sơ và các bài kiểm tra tuyển dụng. Hãy thử tìm hiểu về Trại thực huấn XEngineer mùa hè năm nay.

![](https://cdn.beekka.com/blogimg/asset/202606/bg2026060404.webp)

Chương trình được sáng lập bởi **Xu Shiwei, người sáng lập và CEO của Qiniu Cloud**. Đối tượng tham gia là sinh viên tốt nghiệp các khóa 2025–2029, không giới hạn bằng cấp hay chuyên ngành. **Bạn chỉ cần nộp một phương án sản phẩm hoặc kết quả dự án là có thể ứng tuyển**.

Trại thực huấn tập trung rèn luyện năng lực sản phẩm và kiến trúc trong thời đại AI. Bạn sẽ được hướng dẫn bắt đầu từ nhu cầu thực tế, tư duy thấu đáo, rồi tự tay thiết kế, triển khai và đưa một dự án lên môi trường thực tế.

Đây là cơ hội để bạn trải nghiệm môi trường làm việc thực tế tại các công ty internet, tích lũy kinh nghiệm chiến đấu và mở ra cơ hội nghề nghiệp.

Truy cập ngay **hr.qiniu.com** hoặc quét mã QR bên dưới để đăng ký. Đăng ký càng sớm, cơ hội giữ chỗ càng cao cho kỳ khai mạc vào tháng 7 tới.

![](https://cdn.beekka.com/blogimg/asset/202606/bg2026060407.webp)

Sau khi đăng ký, bạn sẽ nhận được các chủ đề cụ thể và cần nộp phương án hoặc kết quả dự án trong vòng 72 giờ. Hội đồng chuyên môn sẽ đánh giá và tổ chức các buổi thuyết trình để chọn ra những tác phẩm xuất sắc nhất trước ngày khai mạc với tổng giá trị giải thưởng lên đến 200.000 Nhân dân tệ.

Trong suốt 2 tháng hè, các giảng viên giàu kinh nghiệm và trợ giảng sẽ đồng hành cùng bạn để hoàn thành một dự án thực tế.

## Bài viết

1. [Trải nghiệm dùng AI để săn Bug của tôi](https://newsletter.semianalysis.com/p/finding-miscompiles-for-fun-not-profit) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202605/bg2026053001.webp)

Tác giả đã thử dùng AI để tìm lỗi trong trình biên dịch và nhận ra rằng chi phí để chạy AI còn cao hơn cả tiền lương của anh ta. Thú vị là nếu chi nhiều tiền hơn, AI còn có thể tìm ra nhiều lỗi hơn nữa.

Lần đầu tiên, anh cảm nhận được giá trị của AI thực sự lớn hơn giá trị của chính mình.

2. [Kiểm tra sức khỏe nút mạng trong cân bằng tải](https://singh-sanjay.com/2026/01/12/health-checks-client-vs-server-side-lb.html) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202602/bg2026022403.webp)

Bài viết phân tích cách thực hiện cân bằng tải ở phía máy chủ hoặc phía máy khách, và cách kiểm tra các nút mạng gặp sự cố trong cả hai trường hợp này.

3. [Bốn kịch bản HTML có thể thay thế JS](https://www.htmhell.dev/adventcalendar/2025/27/) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202512/bg2025122902.webp)

HTML và CSS hiện nay đã đủ mạnh mẽ để thay thế JS trong nhiều tình huống, chẳng hạn như tạo các cửa sổ pop-up hay các lớp phủ (overlays).

4. [Cách chèn liên kết số điện thoại trên web](https://sethmlarson.dev/mobile-browsers-and-telephone-numbers) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025112601.webp)

Trình duyệt di động thường tự động thêm liên kết vào các dãy số giống số điện thoại. Bài viết này hướng dẫn bạn cách tùy biến hành vi đó, bao gồm cả việc hủy liên kết hoặc chuyển hướng cuộc gọi đến một số khác.

5. [Sử dụng các phần tử HTML tùy chỉnh](https://maurycyz.com/misc/make-up-tags/) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202512/bg2025122903.webp)

Bạn hoàn toàn có thể sử dụng các thẻ HTML tùy chỉnh thay vì chỉ dùng `div` để tăng tính ngữ nghĩa cho trang web.

6. [Vực thẳm Challenger sâu đến mức nào?](https://storymaps.arcgis.com/stories/0d389600f3464e3185a84c199f04e859) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202511/bg2025112404.webp)

Một bài viết đồ họa sinh động giải thích về điểm sâu nhất trên Trái Đất, sâu khoảng 11.000 mét dưới mực nước biển.

## Công cụ

1. [Breathe CLI](https://github.com/marekkowalczyk/breathe-cli)

![](https://cdn.beekka.com/blogimg/asset/202605/bg2026053103.webp)

Một ứng dụng dòng lệnh cho macOS hiển thị thanh tiến trình giúp bạn tập thở chậm (khoảng 6 lần mỗi phút) để cải thiện chức năng tim mạch.

2. [NMLinux](https://github.com/thongor77/nmlinux)

![](https://cdn.beekka.com/blogimg/asset/202606/bg2026060201.webp)

Bảng điều khiển giao diện đồ họa để quản lý mạng trên hệ điều hành Linux.

3. [Penpot](https://github.com/penpot/penpot)

![](https://cdn.beekka.com/blogimg/asset/202404/bg2024041001.webp)

Công cụ thiết kế mã nguồn mở có thể thay thế Figma, cho phép chuyển đổi các bản thiết kế trực quan thành mã CSS và HTML.

4. [sky adb](https://github.com/sky22333/skyadb)

![](https://cdn.beekka.com/blogimg/asset/202605/bg2026052901.webp)

Công cụ quản lý ADB chạy trên điện thoại Android, giúp quản lý điện thoại, máy tính bảng hay TV box qua WiFi ADB.

5. [readNeo](https://github.com/extrastu/readneo)

![](https://cdn.beekka.com/blogimg/asset/202605/bg2026052903.webp)

Bảng dữ liệu cho WeChat Reading, kết nối với Skill API để trực quan hóa giá sách, thống kê đọc và các ghi chú, hỗ trợ xuất dữ liệu nhanh chóng.

6. [AppPorts](https://github.com/wzh4869/AppPorts)

![](https://cdn.beekka.com/blogimg/asset/202605/bg2026052904.webp)

Ứng dụng mã nguồn mở giúp di chuyển các phần mềm trên macOS sang ổ cứng ngoài mà vẫn đảm bảo chúng hoạt động bình thường, đồng thời có thể khôi phục bất cứ lúc nào.

7. [Game Đấu Địa Chủ](https://github.com/palemoky/fight-the-landlord)

![](https://cdn.beekka.com/blogimg/asset/202606/bg2026060101.webp)

Trò chơi Đấu Địa Chủ (Fight the Landlord) chạy trên terminal, viết bằng ngôn ngữ Go, hỗ trợ chơi trực tuyến, tự động kết nối lại và tích hợp robot thông minh.

8. [fuckssh](https://github.com/hczs/fuckssh)

Công cụ dòng lệnh hỗ trợ cấu hình khóa SSH cho máy chủ thông qua các bước hướng dẫn tương tác.

9. [StarGuard](https://github.com/m-ahmed-elbeskeri/Starguard)

Công cụ Python giúp kiểm tra xem các ngôi sao (stars) của một kho lưu trữ GitHub là thật hay giả.

10. [Nginx Proxy Manager](https://github.com/NginxProxyManager/nginx-proxy-manager)

![](https://cdn.beekka.com/blogimg/asset/202505/bg2025051008.webp)

Công cụ mã nguồn mở quản lý Nginx reverse proxy qua giao diện web, tự động kích hoạt chứng chỉ SSL.

## Liên quan đến AI

1. [Models.dev](https://github.com/anomalyco/models.dev)

![](https://cdn.beekka.com/blogimg/asset/202605/bg2026052303.webp)

Cơ sở dữ liệu mã nguồn mở tổng hợp thông số kỹ thuật và giá cả của các mô hình AI.

2. [pixtuoid](https://github.com/IvanWng97/pixtuoid)

![](https://cdn.beekka.com/blogimg/asset/202605/bg2026052902.webp)

Một công cụ sáng tạo sử dụng các nhân vật pixel để đại diện cho các AI Agent, hiển thị tiến độ công việc thông qua hoạt ảnh trên terminal.

3. [Flipbook Canvas](https://github.com/imcuttle/flipbook-app)

![](https://cdn.beekka.com/blogimg/asset/202606/bg2026060204.webp)

Sử dụng AI để tạo ra các tập ảnh có thể tương tác. Tùy thuộc vào vị trí bạn nhấp vào trên ảnh, hệ thống sẽ tự động chuyển sang trang ảnh tiếp theo tương ứng.

4. [album-assetizer](https://github.com/SeanWong17/album-assetizer)

![](https://cdn.beekka.com/blogimg/asset/202605/bg2026053101.webp)

Công cụ dòng lệnh quét album ảnh cá nhân và sử dụng AI để tạo mô tả cấu trúc cho từng bức ảnh, lưu trữ trong SQLite nội bộ và hỗ trợ xuất ra định dạng JSONL hoặc CSV.

## Tài nguyên

1. [Tổng hợp đề thi đại học Trung Quốc](https://t.urongda.com/)

![](https://cdn.beekka.com/blogimg/asset/202606/bg2026060401.webp)

Trang web tập hợp đề thi đại học qua các năm của các tỉnh thành tại Trung Quốc.

## Hình ảnh

1. [Phép chiếu hình trụ](https://liorsinai.github.io/mathematics/2020/08/27/secant-mercator.html)

Về cơ bản, việc vẽ bản đồ phẳng cho Trái Đất là quá trình chuyển đổi tọa độ mặt cầu sang tọa độ phẳng. Một phương pháp phổ biến là tưởng tượng một tờ giấy cuộn lại thành hình trụ bao quanh Trái Đất, sau đó chiếu mọi điểm từ mặt đất lên mặt trụ này theo hướng tự quay của Trái Đất.

![](https://cdn.beekka.com/blogimg/asset/202504/bg2025042106.webp)

## Trích đoạn

1. [Khi nào kỹ sư phần mềm nên nghỉ hưu?](https://thecodist.com/how-to-know-when-its-time-to-go/)

Sau một năm cân nhắc, tôi đã quyết định rời bỏ công việc lập trình viên để nghỉ hưu. Lý do không phải vì năng lực kém, mà đơn giản là tôi không còn muốn tiếp tục nữa.

Ai rồi cũng sẽ đến một điểm giới hạn, khi họ không còn đủ sức để làm công việc mà họ đã gắn bó cả đời. Điều này chẳng liên quan gì đến tuổi tác, tôi từng biết những người trẻ hơn mình rất nhiều nhưng cũng đã từ bỏ nghề lập trình.

Dưới đây là vài lý do nghỉ hưu phổ biến mà tôi từng chứng kiến:

(1) Năng lực không còn đáp ứng. Bạn không thể hoàn thành các nhiệm vụ được giao hoặc kỹ năng của bạn không còn phù hợp với yêu cầu của ngành.

(2) Mất đi khát khao và hứng thú với nghề.

(3) Thị trường việc làm khó khăn hoặc công ty phá sản và bạn không tìm được bến đỗ mới.

(4) Công nghệ thay đổi quá nhanh khiến kỹ năng của bạn trở nên lỗi thời.

(5) Bạn tìm thấy những việc khác ý nghĩa hơn để làm.

(6) Bạn đã kiếm đủ tiền và cảm thấy kiệt sức, không còn động lực để quan tâm đến công việc hiện tại.

Mọi lập trình viên cuối cùng rồi cũng sẽ rời bỏ công việc của mình vì một trong những lý do trên. Tôi cũng thấy có những người coi trọng đồng lương, họ sẽ bám trụ chừng nào còn được trả tiền dù có thích hay không. Đó cũng là một lựa chọn, nhưng tôi không muốn sống như vậy. Vừa làm việc vừa cảm thấy đau khổ thực sự không đáng chút nào.

Tôi thích tạo ra sự thay đổi và chấp nhận những thử thách quan trọng. Tiền bạc tất nhiên là tốt, nhưng được tạo ra sự khác biệt mới là điều tôi trân trọng.

Mọi hành trình rồi cũng sẽ đến lúc kết thúc, dù là một công việc, một công ty hay cả một sự nghiệp. Việc thành thật với bản thân và đưa ra quyết định sáng suốt vẫn tốt hơn nhiều so với việc thấy mình bị tụt lại phía sau và bị buộc phải rời cuộc chơi.

## Trích dẫn

1\. Tại sao con người lại có lòng trắng mắt? Đa số các loài động vật có vú khác như khỉ hay đười ươi đều không có. Một cách giải thích là điều này giúp chúng ta nhận biết được người khác đang nhìn về hướng nào.
-- [Tại sao con người có lòng trắng mắt](https://www.popsci.com/science/why-humans-have-white-part-eyes/)

2\. Một trong những lý do Satya Nadella thành công là ông đã "khai tử" Windows, hay chính xác hơn là chấm dứt vị thế hạt nhân của Windows trong hệ sinh thái Microsoft. Thay vào đó, ông tập trung phát triển các phần mềm hiện diện ở mọi nơi và một nền tảng đám mây bao phủ tất cả.
-- [Chiến lược AI của Microsoft](https://stratechery.com/2026/the-nvidia-ai-pc-project-solara-microsoft-ai/)

3\. Năm 1969, hai bác sĩ người Mỹ đã xây dựng một mô hình tâm lý phân tích bệnh nhân nan y với 5 giai đoạn: phủ nhận, giận dữ, mặc cả, trầm cảm và chấp nhận. Hiện nay, mô hình này cũng đang được dùng để phân tích tâm lý của những người bị mất việc do trí tuệ nhân tạo.
-- [Nỗi đau mất việc vì AI](https://jackmaguire.org/blog/ai-job-grief/)

4\. Lập trình theo "vibe" (vibe coding) tạo ra mã nguồn, còn kỹ thuật tạo ra hệ thống. Vibe coding không phải là kỹ thuật hệ thống.
-- [Vibe coding không phải là kỹ thuật](https://phroneses.com/articles/build/notes/vibe-coding-is-not-engineering.html)

5\. Có ba cách để kiếm sống: (1) Nói dối những người muốn nghe lời nói dối, bạn sẽ giàu to. (2) Nói thật với những người muốn nghe sự thật, bạn sẽ đủ ăn. (3) Nói thật với những người muốn nghe lời nói dối, bạn sẽ phá sản.
-- [Ba cách kiếm sống](https://jasonzweig.com/three-ways-to-get-paid/)
