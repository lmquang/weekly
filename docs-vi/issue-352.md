---
date: 2026-05-05
tags: ["bug tracking", "github issues", "dự án", "project management", "huawei", "ai", "startup", "lập trình", "phần mềm", "backend"]
---

# Một hệ thống theo dõi Bug đúng nghĩa

## Ảnh bìa

![](https://cdn.beekka.com/blogimg/asset/202506/bg2025060801.webp)

Rạng sáng ngày 6/6, tên lửa Trường Chinh 6 được phóng từ căn cứ Thái Nguyên đã bay ngang qua tường thành Tây An.

## Một hệ thống theo dõi Bug đúng nghĩa

Tuần trước chúng ta đã bàn về [GitHub Issues](https://github.com/features/issues) và thấy nó là một công cụ ghi chú rất mạnh mẽ.

Tuy nhiên, có một điều chưa kịp nói: **Công việc chính của nó—theo dõi Bug—lại không hề tốt.**

![](https://cdn.beekka.com/blogimg/asset/202506/bg2025060805.webp)

Nếu dùng nó để quản lý Bug một cách chuyên nghiệp, bạn sẽ nhận ra những khiếm khuyết trong thiết kế khiến trải nghiệm không hề suôn sẻ.

![](https://cdn.beekka.com/blogimg/asset/202506/bg2025060806.webp)

[Bugzilla](https://www.bugzilla.org/) hiện là hệ thống theo dõi Bug lâu đời nhất còn hoạt động. Một kỹ sư kỳ cựu của dự án này gần đây đã viết [một bài báo](https://www.bozemanpass.com/everythings-a-bug-or-an-issue/) chia sẻ về bốn nguyên tắc thiết kế của Bugzilla. Ông cho rằng một hệ thống tốt cần đáp ứng đủ bốn tiêu chí sau:

**(1) Mọi nhiệm vụ đều phải được coi là một Bug.** Không chỉ là lỗi code, mà cả các tính năng mới cần phát triển, tài liệu còn thiếu, trải nghiệm người dùng gây bối rối, hay hiệu năng kém... Tất cả nên được quản lý tập trung. Về bản chất, hệ thống theo dõi Bug chính là hệ thống quản lý dự án.

**(2) Trạng thái của Bug cần đa dạng, không chỉ có "Mở" và "Đóng".** Trong các công ty lớn, quy trình xử lý Bug có thể rất phức tạp.

![](https://cdn.beekka.com/blogimg/asset/202506/bg2025060807.webp)

Hệ thống cần đủ linh hoạt để tùy chỉnh mức độ ưu tiên, độ nghiêm trọng, người chịu trách nhiệm, hay các phụ thuộc (dependencies) để phù hợp với từng quy trình cụ thể.

**(3) Mỗi Bug chỉ được phép có một người chịu trách nhiệm duy nhất.** Điều này giúp làm rõ trách nhiệm, dễ dàng theo dõi khối lượng công việc của từng cá nhân và tạo cảm giác sở hữu cho lập trình viên.

**(4) Hỗ trợ chế độ xem tùy chỉnh (Custom Views).** Hệ thống phải cho phép người dùng lọc và lưu lại các chế độ xem dựa trên trạng thái Bug, mức độ ưu tiên hoặc phiên bản phần mềm.

Nhìn lại GitHub Issues, nó gần như không đáp ứng được tiêu chí nào trong số này một cách triệt để:
- Chức năng quản lý dự án còn quá yếu.
- Trạng thái chỉ có thể dựa vào nhãn (label).
- Nhiệm vụ có thể giao cho nhiều người.
- Chế độ xem mặc định sắp xếp theo thời gian tạo, rất khó để quản lý theo độ ưu tiên.

Thậm chí ở khía cạnh này, GitHub còn thua cả Gitea. GitHub không có cách nào để các Bug quan trọng nhất (P0) tự động nhảy lên đầu danh sách trừ khi bạn ghim (pin) chúng thủ công.

![](https://cdn.beekka.com/blogimg/asset/202506/bg2025060809.webp)

Trong khi đó, Gitea (và bản fork Forgejo) cung cấp tính năng "[Label Set](https://docs.gitea.com/administration/customizing-gitea#labels)", cho phép một nhãn có nhiều giá trị và sắp xếp danh sách dựa trên các giá trị đó.

![](https://cdn.beekka.com/blogimg/asset/202506/bg2025060810.webp)

## Phần mềm tuần này: PandaWiki

Làm thế nào để các nhóm nhỏ hoặc cá nhân quản lý lượng lớn tài liệu và xây dựng kho tri thức riêng?

Hãy thử [PandaWiki](https://github.com/chaitin/PandaWiki)—một hệ thống quản lý tri thức nguồn mở vừa ra mắt.

![](https://cdn.beekka.com/blogimg/asset/202506/bg2025060601.webp)

PandaWiki hoạt động theo mô hình Wiki, cho phép sắp xếp tài liệu linh hoạt để làm trang FAQ, blog hoặc trang hướng dẫn. Điểm mạnh của nó là tích hợp sẵn AI: bạn có thể dùng ngôn ngữ tự nhiên để đặt câu hỏi hoặc tìm kiếm tài liệu liên quan thông qua các mô hình embedding.

![](https://cdn.beekka.com/blogimg/asset/202506/bg2025060602.webp)

Backend của PandaWiki viết bằng Go cho tốc độ phản hồi cực nhanh. Bạn có thể triển khai dễ dàng qua Docker chỉ với một câu lệnh. Dự án hiện đã nhận được hơn 600 sao trên GitHub.

## Phỏng vấn Nhậm Chính Phi

Dưới đây là một số đoạn trích đáng chú ý từ bài phỏng vấn ông Nhậm Chính Phi (Huawei) trên tờ *Nhân dân Nhật báo*:

(1) Vấn đề chip thực ra không đáng lo ngại. Chúng ta có thể tụt hậu một thế hệ so với Mỹ về chip đơn lẻ, nhưng chúng ta có thể dùng toán học để bù đắp vật lý, dùng tính toán cụm để bù đắp cho chip đơn. Kết quả cuối cùng vẫn đạt được hiệu quả thực tế.

(2) Phần mềm không phải là thứ có thể "bóp nghẹt" được. Đó là các ký hiệu toán học, mã nguồn, các thuật toán được bồi đắp lên, không có rào cản vật lý nào cả. Khó khăn nằm ở giáo dục và xây dựng đội ngũ kế cận.

(3) Khi có tiềm lực kinh tế, chúng ta phải coi trọng nghiên cứu lý thuyết cơ bản. Nếu không có gốc, cây dù có tươi tốt đến đâu cũng dễ dàng gục ngã trước gió bão.

(4) Chúng ta cần kiên trì và tôn trọng các nhà khoa học lý thuyết. Họ thường cô độc vì thế giới chỉ có rất ít người hiểu được những công thức và tư duy trong đầu họ.

(5) Huawei dành khoảng 180 tỷ nhân dân tệ mỗi năm cho R&D, trong đó 60 tỷ dành riêng cho nghiên cứu lý thuyết cơ bản mà không áp dụng các chỉ số KPI khắt khe. Không có lý thuyết sẽ không có đột phá.

(6) AI có lẽ là cuộc cách mạng kỹ thuật cuối cùng của nhân loại (bên cạnh năng lượng hạt nhân). Để phát triển AI cần có năng lượng điện dồi dào, và Trung Quốc đang làm rất tốt mảng truyền tải điện năng.

(7) Đừng quá bận tâm đến những lời khen chê, hãy chỉ quan tâm xem mình có đang làm tốt việc của mình hay không.

## Điểm tin công nghệ

(1) Các nhà khoa học Trung Quốc đề xuất giải pháp "Pin sao Hỏa" giúp lưu trữ năng lượng mặt trời ban ngày để sử dụng vào ban đêm trên hành tinh đỏ. Nguyên lý là điện phân CO2 trong khí quyển sao Hỏa thành oxy và methane, sau đó đốt cháy chúng để phát điện khi cần.

![](https://cdn.beekka.com/blogimg/asset/202506/bg2025060705.webp)

(2) Công ty Yinwang (thuộc Huawei) vừa nộp bằng sáng chế cho mẫu vô lăng có thể thu gọn vào bên trong bảng điều khiển.

![](https://cdn.beekka.com/blogimg/asset/202506/bg2025061003.webp)

![](https://cdn.beekka.com/blogimg/asset/202506/bg2025061004.webp)

(3) Thụy Sĩ vừa khánh thành công trình in 3D cao nhất thế giới: một ngọn tháp ngắm cảnh cao 30 mét. Để đảm bảo khả năng chịu lực, họ đã sử dụng bê tông đặc chế và gia cố bằng thép sau mỗi 20cm in.

![](https://cdn.beekka.com/blogimg/asset/202505/bg2025052704.webp)

![](https://cdn.beekka.com/blogimg/asset/202506/bg2025060104.webp)

(4) Apple vừa có một thay đổi nhỏ nhưng gây tò mò trong bản cập nhật macOS mới: Icon của Finder đã được lật ngược lại (phần mặt cười quay sang hướng khác). Hiện vẫn chưa rõ mục đích của sự thay đổi này.

![](https://cdn.beekka.com/blogimg/asset/202506/bg2025061104.webp)

## Bài viết

1\. [Nhìn lại 6 tháng của LLM](https://simonwillison.net/2025/Jun/6/six-months-in-llms/) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202506/bg2025060804.webp)

Simon Willison điểm lại những sự kiện quan trọng nhất của thế giới AI nửa đầu năm nay. Tốc độ phát triển nhanh đến mức các mô hình cuối năm ngoái giờ đã bị coi là "thế hệ cũ".

2\. [Trải nghiệm sử dụng Claude Code Max](https://steipete.me/posts/2025/claude-code-is-my-computer) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202506/bg2025060405.webp)

Tác giả chi 200 USD/tháng cho gói Max của Claude Code và kết luận rằng nó hoàn toàn xứng đáng với số tiền bỏ ra.

3\. [Hướng dẫn tương tác về Rate Limiting](https://blog.sagyamthapa.com.np/interactive-guide-to-rate-limiting) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202506/bg2025060701.webp)

Bài viết giải thích bốn thuật toán giới hạn tốc độ truy cập phổ biến: Token Bucket, Leaky Bucket, Fixed Window và Sliding Window qua các ví dụ trực quan.

4\. [Giải mã Amazon VPC qua hình vẽ](https://www.ducktyped.org/p/why-is-it-called-a-cloud-if-its-not) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202506/bg2025060903.webp)

Hiểu một cách đơn giản về mạng riêng ảo trong đám mây (Virtual Private Cloud) qua các hình minh họa sinh động.

5\. [Năm dịch vụ lưu dấu trang tự host](https://www.xda-developers.com/replacements-for-pocket-that-are-self-hosted/) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202506/bg2025061002.webp)

Giới thiệu các phần mềm nguồn mở giúp bạn tự xây dựng kho lưu trữ link bài viết thay thế cho Pocket hay Instapaper.

6\. [Thí nghiệm cắm trại tại Hồng Kông](https://corentin.trebaol.com/Blog/8.+The+Homelessness+Experiment) (Tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202506/bg2025060802.webp)

Câu chuyện thú vị về một sinh viên nước ngoài tại Hồng Kông đã chọn cách sống trong lều bên bờ biển để tiết kiệm tiền thuê nhà đắt đỏ.

## Công cụ

1\. [Cap.js](https://github.com/tiagorangel1/cap): Công cụ nhận diện bot trên nền web sử dụng thuật toán Proof-of-Work SHA-256 thay cho CAPTCHA truyền thống.

![](https://cdn.beekka.com/blogimg/asset/202506/bg2025060116.webp)

2\. [Quartz](https://github.com/jackyzha0/quartz): Bộ tạo trang tĩnh từ tài liệu Markdown, một lựa chọn thay thế tuyệt vời cho Obsidian Publish.

![](https://cdn.beekka.com/blogimg/asset/202506/bg2025060803.webp)

3\. [somo](https://github.com/theopfr/somo): Công cụ dòng lệnh giúp kiểm tra các cổng (port) đang bị chiếm dụng trên Linux.

![](https://cdn.beekka.com/blogimg/asset/202506/bg2025061001.webp)

4\. [OOMOL Studio](https://github.com/ruanyf/weekly/issues/7029): IDE sáng tạo cho phép biến các hàm thành các nút (node) và kết nối chúng thành quy trình công việc qua giao diện đồ họa.

![](https://cdn.beekka.com/blogimg/asset/202506/bg2025061108.webp)

5\. [JiceSys](https://www.jicesys.com/): Trợ lý gỡ lỗi truyền tin miễn phí, hỗ trợ các giao thức UDP, TCP, Serial, WebSocket, ZeroMQ.

![](https://cdn.beekka.com/blogimg/asset/202506/bg2025061109.webp)

6\. [container](https://github.com/apple/container): Công cụ từ Apple giúp chạy các container Linux trực tiếp trên Mac mà không cần cài đặt Docker.

7\. [DarkFlare](https://github.com/doxx/darkflare): Công cụ dòng lệnh giúp ngụy trang lưu lượng TCP thành HTTPS để vượt qua các bộ lọc mạng.

8\. [JDownloader](https://jdownloader.org/): Trình quản lý tải xuống đa nền tảng mạnh mẽ. Có thể kết hợp với Raspberry Pi để làm server tải phim/tài liệu 24/7.

![](https://cdn.beekka.com/blogimg/asset/202506/bg2025060901.webp)

9\. [Pydoll](https://github.com/autoscrape-labs/pydoll): Thư viện Python điều khiển Chrome qua giao thức DevTools.

10\. [Chili3D](https://github.com/xiangechen/chili3d): Phần mềm thiết kế 3D CAD chạy ngay trên trình duyệt, mã nguồn mở.

![](https://cdn.beekka.com/blogimg/asset/202506/bg2025061103.webp)

## Liên quan đến AI

1\. [Page Magic](https://github.com/khaledh/pagemagic): Plugin AI cho Chrome giúp bạn sửa đổi giao diện hoặc nội dung trang web hiện tại chỉ bằng cách mô tả yêu cầu.

![](https://cdn.beekka.com/blogimg/asset/202506/bg2025060402.webp)

2\. [WallEcho](https://wallecho.com/): Tạo hình nền điện thoại và máy tính miễn phí từ văn bản.

![](https://cdn.beekka.com/blogimg/asset/202506/bg2025060702.webp)

3\. [AI Insight Daily](https://github.com/justlovemaki/CloudFlare-AI-Insight-Daily): Sử dụng Cloudflare Workers để tổng hợp tin tức AI hàng ngày từ các nguồn chỉ định.

![](https://cdn.beekka.com/blogimg/asset/202506/bg2025060703.webp)

4\. [zenfeed](https://github.com/glidea/zenfeed): Trợ lý thông minh giúp tự động thu thập, sàng lọc và tóm tắt các bài báo về chủ đề bạn quan tâm.

![](https://cdn.beekka.com/blogimg/asset/202506/bg2025060704.webp)

5\. [Wenyan MCP Server](https://github.com/caol64/wenyan-mcp): Kết nối AI với MCP này để tự động dàn trang và đăng bài lên các nền tảng mạng xã hội.

## Tài nguyên

1\. [Danh sách 3000 trường đại học Trung Quốc](https://laosheng.top/fuwu/yuanxiao): Tổng hợp địa chỉ website của các cơ sở giáo dục đại học tại Trung Quốc.

![](https://cdn.beekka.com/blogimg/asset/202506/bg2025061201.webp)

2\. [Mullvad Leta](https://leta.mullvad.net/): Công cụ tìm kiếm từ Mullvad giúp lấy kết quả từ Google/Brave nhưng bảo vệ quyền riêng tư tuyệt đối, không quảng cáo và tốc độ rất nhanh.

![](https://cdn.beekka.com/blogimg/asset/202505/bg2025053003.webp)

3\. [DNS4EU](https://www.joindns4.eu/): Hệ thống DNS công cộng của EU, tích hợp sẵn tính năng lọc quảng cáo.

![](https://cdn.beekka.com/blogimg/asset/202506/bg2025060902.webp)

## Hình ảnh

1\. **Tay nắm cửa tại nhà của Marie Curie**

Nhà vật lý nổi tiếng Marie Curie đã tiếp xúc với các nguyên tố phóng xạ trong thời gian dài. Sau 100 năm, tay nắm cửa tại ngôi nhà cũ của bà ở Paris vẫn có thể đo được bức xạ nhẹ do các bụi radium còn bám lại.

![](https://cdn.beekka.com/blogimg/asset/202506/bg2025061106.webp)

![](https://cdn.beekka.com/blogimg/asset/202506/bg2025061107.webp)

2\. **Bãi đỗ xe trong hang động**

Tại Missouri (Mỹ), những hang động khổng lồ để lại sau quá trình khai thác đá vôi đã được Ford tận dụng làm bãi đỗ xe từ những năm 1950. Không gian này có thể chứa tới 5.000 xe, luôn khô ráo và giữ nhiệt độ ổn định quanh năm. Đây có lẽ là cơ sở thương mại ngầm lớn nhất lịch sử.

![](https://cdn.beekka.com/blogimg/asset/202411/bg2024111103.webp)

![](https://cdn.beekka.com/blogimg/asset/202411/bg2024111104.webp)

![](https://cdn.beekka.com/blogimg/asset/202411/bg2024111105.webp)

![](https://cdn.beekka.com/blogimg/asset/202411/bg2024111106.webp)

## Trích đoạn

**Mô hình ngôn ngữ nhỏ (SLM)**

Ngày nay, bất kỳ mô hình nào có thể chạy được mà không cần đến các cụm GPU A100 khổng lồ đều có thể được coi là "mô hình nhỏ". Thậm chí những mô hình 30 tỷ tham số (30B) cũng nằm trong nhóm này vì chúng chỉ cần một GPU duy nhất để vận hành.

Sự khác biệt lớn nhất hiện nay không nằm ở quy mô tham số mà là ở **khả năng triển khai**. Nếu bạn có thể chạy nó trên thiết bị cá nhân, đó là một mô hình nhỏ.

SLM có những ưu thế riêng: chính xác hơn trong các lĩnh vực chuyên biệt, dễ dàng tinh chỉnh (fine-tune) và triển khai cục bộ với chi phí thấp. Việc một chiếc card đồ họa 4090 có thể chạy mượt mà mô hình 70B với tốc độ phản hồi tốt là điều mà vài năm trước chúng ta chỉ thấy trong phim viễn tưởng. SLM chính là chìa khóa để mỗi cá nhân có thể sở hữu một trí tuệ nhân tạo riêng ngay tại nhà.

## Trích dẫn

1\. Nhiều người thường trì hoãn và phàn nàn rằng họ thiếu động lực. Nhưng thực tế, động lực lại sinh ra từ hành động. Chỉ cần bạn bắt đầu làm một việc gì đó, dù là nhỏ nhất, động lực sẽ tự tìm đến. Khi đối mặt với nhiệm vụ khổng lồ, đừng đặt mục tiêu hoàn thành nó, hãy đặt mục tiêu "bắt đầu" nó.

-- [Vượt qua sự trì hoãn](https://spectrum.ieee.org/getting-past-procastination)

2\. Mã nguồn an toàn nhất không phải là mã nguồn hoa mỹ hay thông minh, mà là mã nguồn... nhàm chán. Go tuân thủ triết lý này bằng cách loại bỏ những cách viết bóng bẩy, chỉ giữ lại sự đơn giản và dễ đọc. Điều này giúp mã nguồn dễ dàng được kiểm duyệt và khó bị lạm dụng cho các lỗ hổng bảo mật.

-- [Sự nhàm chán đánh bại vẻ đẹp](https://blog.asymmetric.re/boredom-over-beauty-why-code-quality-is-code-security/)

3\. Con người luôn khao khát cái mới. Theo thống kê, gần 80% lượt nghe nhạc trực tuyến tại Mỹ năm 2024 dành cho các bài hát phát hành từ năm 2010 trở lại đây. Bài hát càng cũ, càng ít người nghe.

-- [AP News](https://apnews.com/article/taylor-swift-sabrina-carpenter-luminate-2024-report-9d3436e71d481a07d88aa13940a68c76)

4\. Tốc độ áp dụng các API mới sẽ chậm lại đáng kể. Vì các mô hình AI lớn chỉ có thể học từ những gì đã tồn tại trên Internet. Với những API mới ra mắt, dữ liệu để AI học tập là quá ít, khiến các lập trình viên phụ thuộc vào AI sẽ do dự khi thay đổi vì AI làm việc với các API cũ nhanh hơn nhiều.

-- Một độc giả trên Hacker News.
