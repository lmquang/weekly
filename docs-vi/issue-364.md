---
date: 2025-09-05
tags: ["ai", "trí tuệ nhân tạo", "lập trình", "programming", "startup", "internet", "bảo mật", "khởi nghiệp", "mã nguồn mở", "công nghệ"]
---

# Khối Rubik khó giải nhất

## Ảnh bìa

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025083002.webp)

Một khay dưa hấu cắt lát tại một siêu thị ở Hạ Môn. ([via](https://www.facebook.com/hxdb1234/posts/pfbid0z2PutGZHD3tWu9BDMTmYP8fqFcySML1K8PRvURUvj8QzpPN1zCtEDwrw9e5yhQnCl))

## Khối Rubik khó giải nhất

Có một điều khá lạ lùng là nhiều lập trình viên tôi quen biết, dù thoạt nhìn chẳng có điểm chung nào, nhưng hễ cứ hỏi đến là y như rằng họ đều mê Rubik.

Thậm chí, trình độ của họ còn rất đáng nể, thường thì chẳng mất quá 3 phút để đưa mọi thứ về vị trí cũ.

![](https://cdn.beekka.com/blogimg/asset/202509/bg2025090405.webp)

Đã có một dạo, văn phòng chúng tôi lúc nào cũng có sẵn vài khối Rubik, cứ rảnh tay là mọi người lại xoay xoay vặn vặn.

Lúc đó tôi chợt nảy ra một câu hỏi: **Liệu khối Rubik nào là khó giải nhất?**

Rõ ràng là mỗi cách xáo trộn sẽ có độ khó khác nhau, nhưng làm sao để định lượng được cái sự "khó" đó?

Gần đây, tôi tình cờ phát hiện ra vấn đề này thực tế đã được [nghiên cứu](https://www.solutionslookingforproblems.com/post/the-rubik-s-cube-perfect-scramble) từ lâu.

Tác giả đã đưa ra một bộ tiêu chuẩn để xác định một khối Rubik khó giải nhất, cụ thể là nó phải thỏa mãn đồng thời 6 điều kiện sau:

> 1. Mỗi mặt đều phải chứa đủ 6 màu.
> 1. Trên mỗi mặt, không có màu nào xuất hiện quá hai lần.
> 1. Không có hai ô cùng màu nào nằm cạnh nhau trên cùng một mặt.
> 1. Không có hai ô cùng màu nào nằm trên cùng một đường chéo của một mặt.
> 1. Tám ô ở góc không được có màu trùng nhau.
> 1. Mẫu hình trên mỗi mặt phải là duy nhất.

Đáng khâm phục hơn, tác giả còn viết cả một [chương trình C++](https://github.com/telemath/PerfectScramble) để săn tìm khối Rubik này.

Với tổng cộng 43.252.003.274.489.856.000 cách sắp xếp khả thi, chiếc máy tính cá nhân của anh ấy đã phải miệt mài chạy trong suốt 5 ngày đêm mới quét hết được mọi kịch bản.

Kết quả cuối cùng thật bất ngờ: **Chỉ có duy nhất một cách sắp xếp thỏa mãn cả 6 yêu cầu trên.**

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025080310.webp)

Hình ảnh trên chính là diện mạo của khối Rubik "bất khả thi" nhất.

Mẫu hình này bao gồm cả 6 mặt của khối Rubik. Vì các mặt này có thể kết hợp ngẫu nhiên nên thực tế có tổng cộng 48 biến thể hình thái khác nhau.

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025080311.webp)

## [Phần mềm tuần này] GeeLark: Trợ lý AI cho marketing xuyên biên giới

Hiện nay, nhu cầu sử dụng các nền tảng mạng xã hội quốc tế (Facebook, Instagram, X/Twitter, TikTok, YouTube, Reddit...) của các doanh nghiệp và cá nhân là rất lớn.

Hôm nay, tôi muốn giới thiệu đến các bạn một phần mềm máy tính mang tên [GeeLark](https://t.wangbase.com/pYrpV), giúp **quản lý tập trung các nền tảng này** một cách đơn giản và hiệu quả. Đây thực sự là một trợ thủ đắc lực cho những ai đang làm marketing xuyên biên giới hay thương mại điện tử quốc tế.

![](https://cdn.beekka.com/blogimg/asset/202509/bg2025090403.webp)

![](https://cdn.beekka.com/blogimg/asset/202509/bg2025090401.webp)

**Điểm mạnh của nó là tích hợp sẵn điện thoại đám mây (Cloud Phone) và trình duyệt vân tay (Fingerprint Browser)**. Bạn có thể khởi tạo các máy điện thoại ảo trên mây chỉ với một cú click để truy cập mạng xã hội.

Việc dùng điện thoại đám mây mang lại nhiều lợi ích: (1) Mỗi tài khoản có một môi trường chạy độc lập, giúp đăng nhập nhiều tài khoản cùng lúc mà không lo bị phát hiện; (2) Trải nghiệm mượt mà như dùng điện thoại thật, nhưng mọi thao tác đều thực hiện trên máy tính; (3) Mỗi máy ảo có một vân tay trình duyệt riêng biệt, giúp tránh tình trạng bị các nền tảng bóp tương tác.

![](https://cdn.beekka.com/blogimg/asset/202509/bg2025090402.webp)

Trong phiên bản mới nhất, GeeLark đã bổ sung thêm rất nhiều tính năng thú vị:

(1) **Tích hợp mô hình AI lớn**, hỗ trợ giải đáp thắc mắc, tạo và chỉnh sửa video, "nuôi" tài khoản bằng AI, viết nội dung... Đặc biệt là tính năng tạo video từ ảnh (hình trên) với nhiều mô hình phổ biến, giúp biến ảnh sản phẩm thành video quảng cáo nhanh chóng.

(2) **Tự động hóa các thao tác thường dùng**. Ví dụ, trên TikTok, nó có các chức năng như nuôi nick bằng AI, tự động đăng video/ảnh, tự động gắn link sản phẩm (giỏ hàng), trợ lý dữ liệu AI, tự động like và comment. Với xu hướng phim ngắn đang hot, nó còn cung cấp tính năng "neo" (anchor) bằng AI để dẫn dắt người xem.

(3) **Tự động hóa Reddit**. Một điểm đáng chú ý là cửa hàng mẫu tự động hóa của nó đã cập nhật tính năng cho Reddit, giúp quản lý tài khoản và đăng bài tự động bằng AI. Điều này rất có lợi cho việc tối ưu hóa công cụ tạo nội dung (GEO), vì các engine AI hiện nay lấy dữ liệu từ Reddit rất nhiều.

(4) **Tùy biến nhiệm vụ**. Nếu các kịch bản có sẵn chưa đủ, bạn hoàn toàn có thể tự định nghĩa nhiệm vụ để phù hợp với nhu cầu riêng. Chẳng hạn, bạn có thể tích hợp một mô hình nhận diện hình ảnh vào quy trình làm việc để AI tự đọc màn hình điện thoại ảo và đưa ra hành động tương ứng.

(5) **Cung cấp API**. GeeLark hỗ trợ [API](https://t.wangbase.com/LeK9D) để bạn tự lập trình, khởi tạo máy ảo và các tác vụ tự động, mở ra không gian ứng dụng rộng lớn hơn rất nhiều.

Nhìn chung, nếu bạn đang cần quản lý nhiều tài khoản mạng xã hội quốc tế thì GeeLark rất đáng để thử. Mô hình tính phí của họ cũng khá linh hoạt, dựa trên mức độ sử dụng thực tế chứ **không thu phí theo số lượng thành viên trong nhóm**.

Bạn có thể truy cập trang chủ [geelark.cn](https://www.geelark.cn/?utm_source=ruanyifeng.com&utm_medium=post&utm_campaign=campaign20250905) để tải về dùng thử, hoặc tham khảo [hướng dẫn chính thức](https://t.wangbase.com/XdBPV).

## Tin tức công nghệ

1. Hàn Quốc đã triển khai "[cảnh sát hologram](https://www.scmp.com/week-asia/lifestyle-culture/article/3322654/south-korea-deploys-hologram-police-officer-fight-crime-and-its-working)" tại các công viên ở Seoul vào ban đêm.

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025083011.webp)

Bạn sẽ thấy một viên cảnh sát có kích thước như người thật, đứng giữa những bụi cỏ, có thể nói chuyện và thực hiện các động tác. Nếu nhìn từ xa, gần như không thể nhận ra đó chỉ là hình ảnh trình chiếu. Cảnh sát cho biết kể từ khi thiết bị này hoạt động, tỷ lệ tội phạm trong công viên đã giảm khoảng 22%.

2. Một lập trình viên người Mỹ đã biến một chiếc máy pha cà phê cũ thành một chiếc "[máy tính pha cà phê](https://www.dougmacdowell.com/coffeematic-pc.html)".

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025080201.webp)

Thiết bị này vừa là máy tính, vừa là máy pha cà phê, và cả hai chức năng đều hoạt động hoàn hảo.

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025080202.webp)

Thách thức lớn nhất ở đây là máy pha cà phê thì tạo ra hơi nước nóng, trong khi máy tính lại kỵ nước và cần tản nhiệt. Việc đặt cả hai ở cạnh nhau khiến máy tính rất khó vận hành ổn định.

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025080203.webp)

3. [Meta](https://www.nytimes.com/2025/07/23/science/meta-computer-wristband-reardon.html) vừa giới thiệu một loại vòng đeo tay có thể điều khiển máy tính.

![](https://cdn.beekka.com/blogimg/asset/202507/bg2025072802.webp)

Chiếc vòng này nhỏ gọn như một chiếc đồng hồ, được cho là có thể thay thế chuột hay thậm chí là bút cảm ứng. Nguyên lý của nó khá mới lạ: khi ngón tay và bàn tay cử động, chúng sẽ tạo ra các tín hiệu điện cơ. Chiếc vòng sẽ đọc các tín hiệu này và đoán định được ý định hành động của người dùng.

4. [Tích năng năng lượng bằng mỏ khai thác](https://www.independent.co.uk/tech/gravity-battery-mine-renewable-energy-b2492087.html)

Tại Phần Lan, có một mỏ khai thác cũ sâu tới 1.400 mét. Một công ty Anh đang lên kế hoạch biến nó thành một "viên pin" khổng lồ.

![](https://cdn.beekka.com/blogimg/asset/202402/bg2024021102.webp)

Ý tưởng rất đơn giản: lắp đặt các cần cẩu treo vật nặng trong hầm mỏ. Khi dư thừa điện, hệ thống sẽ dùng điện để kéo vật nặng lên cao. Khi cần dùng điện, vật nặng sẽ được thả xuống từ từ, giải phóng thế năng trọng trường để làm quay tuabin phát điện.

![](https://cdn.beekka.com/blogimg/asset/202402/bg2024021103.webp)

Nếu phương pháp này khả thi, chúng ta có thể tận dụng hàng loạt hầm mỏ bỏ hoang để làm trạm lưu trữ năng lượng.

5. [Quảng cáo trên bản đồ](https://www.androidauthority.com/google-maps-pop-up-ad-3458170/)

Google Maps gần đây đã xuất hiện một kiểu quảng cáo mới. Khi bạn đang dùng định vị, một cửa sổ sẽ bất ngờ hiện ra (hình dưới), gợi ý bạn có thể ghé vào một địa điểm nào đó trên đường đi.

![](https://cdn.beekka.com/blogimg/asset/202407/bg2024070902.webp)

Hãy thử tưởng tượng, trong tương lai, lộ trình của bạn có thể xuất hiện hàng loạt điểm "check-in". Chỉ cần bạn ghé vào cửa hàng và check-in trên điện thoại, bạn sẽ nhận được phần thưởng hoặc voucher giảm giá.

## Trích đoạn

1. [Cơ chế xác thực bot của Cloudflare](https://developers.cloudflare.com/bots/reference/bot-verification/web-bot-auth/) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025083001.webp)

Cloudflare, nhà cung cấp dịch vụ CDN lớn nhất thế giới, vừa ra mắt cơ chế xác thực bot. Nếu bạn muốn crawl dữ liệu từ các trang web mà họ quản lý, bạn buộc phải đăng ký public key, và sau đó mỗi request gửi đi đều phải kèm theo chữ ký.

2. [Tôi làm kỹ sư tại Anduril](https://joincolossus.com/article/the-amusement-park-for-engineers/) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025083102.webp)

Anduril là một công ty công nghệ quốc phòng mới nổi của Mỹ, chuyên về ứng dụng quân sự của drone. Người sáng lập công ty này cũng chính là cha đẻ của kính Oculus. Bài viết này do một kỹ sư của công ty chia sẻ về môi trường nghiên cứu và phát triển bên trong, rất nhiều chi tiết thú vị.

3. [Dùng database để thay thế cache](https://avi.im/blag/2025/db-cache/) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202509/bg2025090101.webp)

Tác giả chia sẻ quan điểm cá nhân về việc khi nào nên truy vấn trực tiếp vào database và khi nào thì nên dùng cache, đồng thời phân tích ưu nhược điểm của cache so với database.

4. [Chúng tôi đưa AI vào một vòng lặp while](https://github.com/repomirrorhq/repomirror/blob/main/repomirror.md) (tiếng Anh)

Tác giả đã viết một bộ chỉ thị để AI tự viết code, và nếu có lỗi thì tự tạo PR để sửa. Anh ấy ném bộ chỉ thị đó vào một vòng lặp `while` rồi đi ngủ. Sáng hôm sau tỉnh dậy xem kết quả ra sao. (Tiết lộ: Chỉ sau một đêm, AI đã "đốt" sạch 800 USD).

5. [Hộp công cụ Python của tôi](https://www.cesarsotovalero.net/blog/i-am-switching-to-python-and-actually-liking-it.html) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202507/bg2025071711.webp)

Tác giả vốn là người mới bắt đầu với Python. Bài viết giới thiệu các công cụ phát triển cơ bản mà anh ấy đang dùng, như uv, ruff, ty...

6. [Sự khác biệt giữa CPU AMD và Intel](https://www.xda-developers.com/differences-between-amd-and-intel-cpus/) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202507/bg2025071709.webp)

Cả AMD và Intel đều sản xuất CPU x86. Dù sản phẩm có vẻ giống nhau về bản chất, bài viết này sẽ đi sâu vào sự khác biệt trong kiến trúc của hai "ông lớn" này.

## Công cụ

1. [sping](https://dseltzer.gitlab.io/sping/)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025083006.webp)

Một phiên bản nâng cấp của lệnh ping, hiển thị độ trễ của từng gói tin dưới dạng đồ họa ngay trong terminal.

2. [Beszel](https://github.com/henrygd/beszel)

![](https://cdn.beekka.com/blogimg/asset/202505/bg2025052102.webp)

Công cụ giám sát máy chủ nhẹ nhàng với giao diện web.

3. [WinApps](https://github.com/winapps-org/winapps)

![](https://cdn.beekka.com/blogimg/asset/202509/bg2025090411.webp)

Công cụ giúp chạy các ứng dụng Windows trên Linux. Nó sẽ tự động khởi tạo một máy ảo để chạy ứng dụng, khác với nguyên lý của Wine (vốn là mô phỏng Windows API). Ngoài ra còn có một công cụ tương tự là [WinBoat](https://github.com/TibixDev/winboat).

![](https://cdn.beekka.com/blogimg/asset/202509/bg2025090412.webp)

4. [YouTube TUI](https://github.com/Siriusmart/youtube-tui)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025083010.webp)

Client YouTube trên terminal, giúp bạn thao tác với YouTube hoàn toàn bằng dòng lệnh.

5. [LabPlot](https://labplot.org/)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025083012.webp)

Phần mềm máy tính để trực quan hóa dữ liệu, giúp chuyển các tập dữ liệu thành nhiều loại biểu đồ khác nhau, được đánh giá là rất mạnh mẽ.

6. [gitlab-to-github](https://github.com/wuuashen/gitlab-to-github)

Một script Python giúp bạn chuyển toàn bộ kho lưu trữ (repo) từ GitLab sang GitHub chỉ với một cú click.

7. [Telegram Spam Sniper](https://github.com/ramsayleung/bayes_spam_sniper)

![](https://cdn.beekka.com/blogimg/asset/202509/bg2025090201.webp)

Một bot Telegram nguồn mở sử dụng thuật toán Bayes để tự động chặn các tin nhắn quảng cáo trong nhóm.

8. [Foxel](https://github.com/DrizzleTime/Foxel)

![](https://cdn.beekka.com/blogimg/asset/202509/bg2025090202.webp)

Nền tảng lưu trữ đám mây cá nhân nguồn mở, có hỗ trợ tìm kiếm ngữ nghĩa bằng AI.

9. [StoryMotion](https://storymotion.video/)

![](https://cdn.beekka.com/blogimg/asset/202509/bg2025090406.webp)

Trình chỉnh sửa hoạt ảnh trên web, dùng để tạo các hoạt ảnh phong cách vẽ tay Excalidraw nhúng vào trang web, rất phù hợp để demo sản phẩm.

10. [Website Screenshot Online](https://websitescreenshot.online/zh-CN)

![](https://cdn.beekka.com/blogimg/asset/202509/bg2025090413.webp)

Trang web chụp ảnh màn hình miễn phí. Người dùng chỉ cần nhập URL và nhận lại ảnh chụp trang web đó. Ngoài ra còn có công cụ quay video cuộn trang web.

## AI Liên quan

1. [Công cụ tóm tắt sách AI](https://github.com/SSShooter/ebook-to-mindmap)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025082901.webp)

Ứng dụng web này có thể chia nhỏ sách điện tử (định dạng epub và pdf) theo từng chương, sau đó dùng AI để tạo tóm tắt văn bản và sơ đồ tư duy cho chương đó. Người dùng cần tự cung cấp API Key của mô hình ngôn ngữ.

2. [VIVY](https://github.com/liriliri/vivy)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025083101.webp)

Một ứng dụng desktop (client) cho mô hình tạo ảnh Stable Diffusion.

3. [ApeRAG](https://github.com/apecloud/ApeRAG)

![](https://cdn.beekka.com/blogimg/asset/202509/bg2025090203.webp)

Nền tảng RAG (Retrieval-Augmented Generation) nguồn mở, kết hợp đồ thị RAG, tìm kiếm vector và tìm kiếm toàn văn với các tác nhân AI (AI Agents).

4. [AI Video Transcriber](https://github.com/wendy7756/AI-Video-Transcriber)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025083104.webp)

Công cụ trích xuất văn bản, dịch thuật và tóm tắt video bằng AI, hỗ trợ hơn 30 nền tảng như YouTube, TikTok... Mã nguồn mở hoàn toàn, bạn cần tự triển khai cả backend và frontend.

## Tài nguyên

1. [OpenAnimation](https://github.com/orispok/OpenAnimationApp)

![](https://cdn.beekka.com/blogimg/asset/202508/bg2025083103.webp)

Kho lưu trữ chuyên sưu tập các hoạt ảnh dựa trên Lottie.

2. [Hướng dẫn sử dụng Jujutsu](https://jj-for-everyone.github.io/)

![](https://cdn.beekka.com/blogimg/asset/202509/bg2025090102.webp)

Jujutsu là một hệ thống quản lý mã nguồn mới nổi, tự nhận là dễ dùng và dễ hiểu hơn Git. Tài liệu tiếng Anh này dành cho những người hoàn toàn chưa biết gì về Git.

3. [Bộ sưu tập 50 bàn phím của tôi](https://aresluna.org/50-keyboards-from-my-collection/)

![](https://cdn.beekka.com/blogimg/asset/202509/bg2025090407.webp)

Một nhà sưu tầm bàn phím liệt kê 50 mẫu bàn phím độc lạ nhất trong bộ sưu tập của mình. Chẳng hạn như mẫu bàn phím sử dụng theo chiều dọc và có cả gương để bạn soi phím, hay bàn phím dạng găng tay để nhập liệu bằng tay còn lại.

![](https://cdn.beekka.com/blogimg/asset/202509/bg2025090408.webp)

![](https://cdn.beekka.com/blogimg/asset/202509/bg2025090409.webp)

![](https://cdn.beekka.com/blogimg/asset/202509/bg2025090410.webp)

## Hình ảnh

1. [Bên trong các nhạc cụ](https://www.dpreview.com/photography/5400934096/probe-lenses-and-focus-stacking-the-secrets-to-incredible-photos-taken-inside-instruments)

Một nhạc sĩ đã nảy ra ý tưởng: chúng ta hàng ngày chỉ nhìn thấy vẻ ngoài của nhạc cụ, vậy bên trong chúng trông như thế nào? Anh ấy đã chụp một loạt ảnh bên trong các nhạc cụ, mang lại một trải nghiệm thị giác hoàn toàn khác biệt, như thể đang bước vào những tòa kiến trúc kỳ lạ.

Đàn Organ ống

![](https://cdn.beekka.com/blogimg/asset/202506/bg2025060110.webp)

Đàn Violin

![](https://cdn.beekka.com/blogimg/asset/202506/bg2025060111.webp)

Đàn Piano

![](https://cdn.beekka.com/blogimg/asset/202506/bg2025060112.webp)

Đàn Cello

![](https://cdn.beekka.com/blogimg/asset/202506/bg2025060113.webp)

## Trích đoạn

1. [Tại sao Facebook không giữ chân được các nhà khoa học](https://www.facebook.com/InvestYourLifes/posts/pfbid02ZaxVs6ES9UaRcUYddE2P1YSqAfVFYQe59AoZdfHUy8Uy3BZk7dt3rf3d3zH8hP7fl)

Gần đây, Facebook đã đổ rất nhiều tiền để chiêu mộ nhân tài AI, nhưng không ít người trong số đó chỉ ở lại một thời gian ngắn rồi rời đi. Tại sao lại vậy?

Một cựu nhân viên đã đưa ra lời giải thích, cho rằng điều này liên quan trực tiếp đến sứ mệnh của công ty. Sứ mệnh của Facebook là "kết nối mọi người", và điều này vốn không có mối liên hệ trực tiếp nào với AI. Dù bên trong có lượng lớn nghiên cứu viên, nhưng hướng nghiên cứu chính vẫn là thuật toán xếp hạng và phân tích dữ liệu lớn. Họ không có nền tảng nghiên cứu AI từ trong lịch sử.

Hơn nữa, những người làm nghiên cứu thực thụ không được coi trọng đúng mức tại Facebook. Nhiều nghiên cứu viên vốn đến từ môi trường học thuật hoặc Google/DeepMind, nơi họ có không gian tự do để khám phá những nghiên cứu dài hạn và tiên phong. Khi sang Facebook, các nghiên cứu AI của họ bị yêu cầu phải phục vụ cho các mục tiêu kinh doanh ngắn hạn như quảng cáo, hệ thống gợi ý hay kiểm duyệt nội dung. Điều này khiến họ cảm thấy thiếu tầm nhìn dài hạn.

Bản chất Facebook là một công ty internet tiêu dùng vận hành theo kiểu "move fast", nhấn mạnh vào việc ra mắt sản phẩm nhanh để thúc đẩy kết quả kinh doanh. Cái "gene" này khiến các nhà khoa học cảm thấy thiếu môi trường học thuật và khó duy trì danh tiếng trong giới chuyên môn. Đồng thời, sự chia tách giữa bộ phận nghiên cứu và sản phẩm khiến các thành quả nghiên cứu khó có thể trực tiếp đi vào đời sống sản phẩm. Nhiều nhà khoa học nhận ra rằng tại Facebook, họ không thể tạo ra những đột phá thực sự mà chỉ xoay quanh các bài toán kinh doanh, và thế là họ chọn cách ra đi.

Điều này cho thấy các ông lớn chưa chắc đã có thể dùng tiền để độc quyền nhân tài. Nếu các công ty nhỏ thực sự làm ra những sản phẩm mang tính cách mạng, họ vẫn có cơ hội rất lớn để thu hút nhân tài.

## Trích dẫn

1\. Một nghiên cứu tại Mỹ chỉ ra rằng AI đang tác động mạnh nhất đến cơ hội việc làm của sinh viên tốt nghiệp từ các trường không danh tiếng, trong khi hầu như không ảnh hưởng đến sinh viên từ các trường hàng đầu như Harvard hay MIT. AI đang làm gia tăng sự mất giá của các bằng cấp phổ thông.

2\. Chạy các ứng dụng AI trên máy tính cá nhân có ba mối nguy lớn: nó có thể truy cập dữ liệu riêng tư, có thể tải các nội dung không đáng tin cậy và có thể thực hiện liên lạc ra bên ngoài.

3\. Ở Trung Quốc có khái niệm "ăn khổ" (chịu khó chịu khổ), nhưng ở Mỹ thì không có khái niệm tương đương như vậy.

4\. Lập trình kiểu "vibe coding" thực sự rất thú vị, bạn chỉ cần đưa ra ý tưởng mà không cần tự mình viết code. Sau khi trải nghiệm, tôi mới nhận ra đây mới chính là điều tôi thực sự thích.

5\. Trò chơi SEO (tối ưu hóa công cụ tìm kiếm) đã kết thúc từ lâu rồi. Đa số mọi người vẫn mải miết theo đuổi thứ hạng trên Google, nhưng người dùng thực tế đã rời bỏ Google rồi. Hiện nay chỉ còn khoảng 27% lượt tìm kiếm diễn ra ở đó, 73% còn lại nằm ở TikTok, Amazon, Reddit, YouTube hay thậm chí là ChatGPT.
