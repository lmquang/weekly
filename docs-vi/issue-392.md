# axios bị cài mã độc và chiêu trò lừa đảo kiểu Hollywood

Bản tin này ghi lại những nội dung công nghệ đáng chia sẻ hàng tuần, phát hành vào thứ Sáu.

Tạp chí này [mã nguồn mở](https://github.com/ruanyf/weekly), hoan nghênh [đóng góp](https://github.com/ruanyf/weekly/issues). Ngoài ra còn có dịch vụ ["Ai đang tuyển dụng"](https://github.com/ruanyf/weekly/issues/9454), đăng tin tuyển dụng lập trình viên. Hợp tác vui lòng [liên hệ qua email](mailto:yifeng.ruan@gmail.com) (yifeng.ruan@gmail.com).

## Ảnh bìa

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040203.webp)

Cơ sở trụ sở chính của Tencent sẽ đi vào hoạt động trong năm nay, thường được gọi là "Đảo Cánh Cụt". Nơi đây không chỉ bao gồm các tòa nhà văn phòng mà còn có nhiều tòa nhà chung cư. ([via](https://www.nfnews.com/content/0oXLNmjJo9.html))

## axios bị cài mã độc và chiêu trò lừa đảo kiểu Hollywood

Tuần trước, thư viện phần mềm nổi tiếng axios đã bị [cài mã độc](https://cloud.tencent.com/announce/detail/2249). Hacker đã chiếm được token phát hành và trực tiếp tung ra một phiên bản mới có chứa mã độc Trojan.

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040703.webp)

Việc phần mềm bị cài mã độc không phải là chuyện mới, nhưng điều mới mẻ ở đây là cách mà token phát hành bị rò rỉ. Câu chuyện đằng sau nó ly kỳ như một bộ phim Hollywood, thực sự là không thể phòng bị.

axios là một trong những thư viện JS được sử dụng rộng rãi nhất với gần 100 triệu lượt tải xuống mỗi tuần. Vì vậy, phạm vi ảnh hưởng của đợt tấn công này là rất lớn.

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040704.webp)

Hơn nữa, mức độ độc hại của Trojan này rất cao. Theo [hướng dẫn gỡ bỏ chính thức](https://github.com/axios/axios/issues/10636#issue-4195231282), nếu chẳng may bị nhiễm mã độc, **tất cả các khóa, token và chứng chỉ trên máy đều phải bị hủy bỏ**. Con Trojan này sẽ quét tất cả các thư mục để thu thập khóa và gửi chúng đi.

Mọi người nên biết rằng, với một thư viện phần mềm siêu phổ biến như axios, mọi mắt xích đều được bảo vệ nghiêm ngặt và từng dòng mã đều được kiểm tra kỹ lưỡng. **Cuộc tấn công lần này hoàn toàn là một chiến dịch kỹ thuật xã hội (social engineering) được dàn dựng công phu** để phá vỡ các lớp phòng thủ đó.

Mục tiêu tấn công được nhắm vào Jason Saayman, người duy trì chính. Theo [tiết lộ của chính ông](https://github.com/axios/axios/issues/10636#issuecomment-4180237789), diễn biến sự việc như sau.

> Họ đã thiết kế quy trình này riêng cho trường hợp của tôi, cụ thể là:
> 
> 1. Họ mạo danh người sáng lập của một công ty nào đó để liên lạc với tôi. Không chỉ giả mạo ngoại hình của người sáng lập mà họ còn giả mạo cả công ty đó.
> 1. Sau đó họ mời tôi tham gia vào một không gian làm việc Slack thực thụ. Không gian này sử dụng bộ nhận diện thương hiệu của công ty đó và tên gọi cũng rất đáng tin. Không gian Slack được thiết kế rất tinh vi, họ có các kênh riêng để chia sẻ bài đăng trên LinkedIn. Tôi đoán những bài đăng LinkedIn này cuối cùng sẽ được đăng lên tài khoản thật của công ty đó, hiệu ứng tổng thể rất chân thực. Thậm chí họ còn tạo ra một số tài khoản giả mà tôi đoán là thành viên nhóm của công ty đó cũng như một số người duy trì phần mềm mã nguồn mở khác.
> 1. Họ sắp xếp một cuộc họp với tôi để trao đổi. Cuộc họp được thực hiện trên Microsoft Teams. Thành phần tham dự có vẻ là một nhóm người.
> 1. Trong cuộc họp, họ chỉ ra rằng một số thứ trên hệ thống của tôi đã lỗi thời. Tôi cứ ngỡ là liên quan đến Teams nên đã cài đặt các thành phần còn thiếu, kết quả hóa ra đó là Trojan truy cập từ xa (RAT).
> 1. Mọi thứ đều được sắp xếp ngăn nắp, trông rất chính quy và cách làm việc cũng rất chuyên nghiệp.

Có thể thấy cuộc tấn công này có kịch bản hẳn hoi. Mỗi bước đều được lên kế hoạch, chuẩn bị và diễn tập kỹ lưỡng, **hoàn toàn được "đo ni đóng giày" cho bạn**, chỉ chờ bạn sập bẫy.

Kẻ lừa đảo rất kiên nhẫn và đã đầu tư chi phí ban đầu rất lớn. Đầu tiên là giả mạo người sáng lập công ty để liên lạc. Để tăng độ tin cậy, họ còn làm trang web công ty giả. Sau đó là mời bạn tham gia Slack của họ với đủ loại thảo luận, tài liệu dự án, tài liệu quảng bá trông như thật. Tuyệt nhất là họ còn để bạn tham gia họp video trên phần mềm Teams, **một nhóm lừa đảo lộ diện trực tiếp để họp cùng bạn**.

Sau khi cuộc họp bắt đầu không lâu, người chủ trì bỗng nói: "Lạ nhỉ, sao hệ thống của anh không giống của chúng tôi, có phải plugin của Microsoft lỗi thời rồi không, tôi gửi anh bản mới nhất nhé." Thế là bạn nhận được gói cài đặt được gửi qua. Thấy những người dự họp khác đang đợi mình, bạn cũng không nghĩ ngợi nhiều mà nhấp đúp để thực thi. Ôi thôi, thế là trúng kế, token phát hành bị rò rỉ chỉ trong một giây.

Làm giả đến mức độ này thực sự khiến người ta phải thán phục.

Điều này làm tôi liên tưởng đến một [tin tức từ Ấn Độ](https://www.wsj.com/world/fake-cops-fake-judges-the-hollywood-style-scam-poised-to-go-global-e1e339a3?st=fXpKE6&mod=1440&user_id=66c4c9305d78644b3ac5df9c) mà tôi đọc được cách đây không lâu. Mức độ làm giả còn kinh khủng hơn nhiều, cũng chẳng khác gì phim Hollywood.

Giáng sinh năm ngoái, một bà cụ 77 tuổi ở New Delhi, Ấn Độ đã nhận được cuộc gọi video qua Whatsapp từ "đồn cảnh sát". Góc dưới bên phải video thậm chí còn có cả phiên dịch ngôn ngữ ký hiệu.

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040405.webp)

Cảnh sát bảo bà rằng ngân hàng phát hiện tài khoản của bà có lịch sử rửa tiền, phải tiến hành điều tra bà. Nếu không hợp tác, tiền trong tài khoản sẽ bị tịch thu. Họ thông báo bà phải tham dự phiên điều tra từ xa của tòa án.

Truyền thông sau đó đã công bố những bức ảnh về bối cảnh của "đồn cảnh sát", mọi người xem xem nó chân thực đến mức nào.

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040406.webp)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040407.webp)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040408.webp)

Ba bức ảnh đầu tiên là đồn cảnh sát Ấn Độ, bức cuối cùng là đồn cảnh sát Pakistan. Chúng nằm trong cùng một tòa nhà, các phòng sát vách nhau. Nên biết rằng hai quốc gia này ngoài đời thực là đối lập, nhưng điều đó không ngăn cản bọn lừa đảo lừa cả hai bên.

Quay lại vụ án, vài ngày sau bà cụ tham gia phiên điều trần trực tuyến được tổ chức tại một tòa án do đích thân "thẩm phán" chủ trì. Ông ta xem xét hồ sơ tài chính, nghe lời khai của "cảnh sát" và đặt một số câu hỏi cho bà cụ.

Cuối cùng, "thẩm phán" bảo bà cụ rằng chính quyền cần xác minh xem tất cả tài sản của bà có hợp pháp hay không. Bà phải kết nối với đồn cảnh sát hàng ngày để trả lời câu hỏi cho đến khi mọi chuyện sáng tỏ.

Dưới đây là phần kịch tính nhất của vụ án này. Trong suốt 16 ngày liên tục, bà cụ hàng ngày mở camera kết nối, hãy xem bọn lừa đảo đã diễn đến mức nào.

> Trong 16 ngày này, bà cụ dần nảy sinh tình cảm với các sĩ quan cảnh sát trực tại đồn giả. Bà bắt đầu gọi họ là con của mình. Và họ cũng gọi bà là "mẹ".
> 
> Buổi tối, bà cùng sĩ quan trẻ nhất đọc kinh điển tôn giáo Ấn Độ giáo. Sĩ quan này còn nhờ bà gửi cho anh ta những đoạn mà bà thấy đặc biệt cảm động.
>
> "Họ giống như người nhà vậy," bà cụ nhớ lại. "Họ nói: 'Thưa bà, chúng con muốn giải quyết xong chuyện này càng sớm càng tốt. Chúng con làm việc ngày đêm vì bà.'"

Trời đất, bọn lừa đảo đã diễn suốt 16 ngày từ sáng đến tối, tâm sự cùng bà cụ, đọc kinh điển cùng nhau, thỉnh giáo các vấn đề nhân sinh cho đến tận đêm khuya. Nếu chuyện này mà dựng thành phim thì sẽ cảm động biết bao.

Bà cụ không hề mảy may nghi ngờ, tự nguyện bán hết các khoản đầu tư của mình và chuyển tổng cộng 1,6 triệu USD qua chín lần vào tài khoản của đồn cảnh sát giả.

Ngày hôm sau, bà kết nối lại với "những đứa con ở đồn cảnh sát" thì không còn liên lạc được nữa.

Từ hai ví dụ trên, mọi người có thể thấy các vụ lừa đảo Internet hiện nay có thể diễn đến mức độ nào. Đó hoàn toàn là những "kịch bản giết người" được nhắm mục tiêu chính xác với tỷ lệ thành công cực cao. Nếu có thêm sự hỗ trợ của AI thì hầu như không thể phân biệt thật giả.

Phát triển web có một quy tắc: Mọi yêu cầu từ phía máy khách đều không thể tin cậy, phải giả định đó là yêu cầu độc hại. Sau này, đời thực có lẽ cũng sẽ như vậy: Mọi người lạ đều không thể tin cậy, phải giả định đó là một trò lừa đảo độc hại.

## Năng lực tính toán vẫn còn thiếu hụt

Gần đây có ba sự kiện xảy ra cho thấy năng lực tính toán hiện nay vẫn đang rất căng thẳng.

Sự kiện thứ nhất, OpenAI [đóng cửa](https://finance.sina.cn/stock/jdts/2026-04-07/detail-inhtsezc7221412.d.html) dịch vụ tạo video Sora, nguyên nhân chính là không đủ năng lực tính toán. Công ty phải dành tài nguyên tính toán cho các mảng kinh doanh cốt lõi.

Sự kiện thứ hai, công ty Anthropic chính thức cấm sử dụng các gói đăng ký tháng cho dịch vụ của bên thứ ba (như OpenClaw, OpenCode, v.v.).

Nguyên nhân là nếu các gói tháng được sử dụng tối đa công suất, năng lực tính toán tiêu tốn sẽ vượt xa phí gói. Năng lực tính toán của công ty rất quý giá, phải ưu tiên đảm bảo cho sản phẩm của chính mình (như Claude Code), không thể để sản phẩm bên ngoài làm tăng gánh nặng cho phòng máy.

Sự kiện thứ ba, có [bài viết](https://martinalderson.com/posts/what-next-for-the-compute-crunch/) cho rằng số lượng mã nguồn được gửi lên GitHub trong ba tháng đầu năm nay gấp 14 lần so với cùng kỳ năm ngoái!

Nguyên nhân rõ ràng là do lập trình AI bùng nổ. Đầu năm ngoái làm gì đã có Claude Code. Tài nguyên của GitHub hoàn toàn không đủ để đối phó với mức tăng trưởng này, dẫn đến việc [liên tục xảy ra sự cố](https://mrshu.github.io/github-statuses/).

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040810.webp)

Hình trên cho thấy thời gian hoạt động bình thường của GitHub trong ba tháng qua chỉ đạt 89,47%, trong khi con số đạt chuẩn phải là 99,99%.

Ba sự kiện trên cho thấy tài nguyên tính toán của các công ty dịch vụ AI lớn đều đang rất căng thẳng, phần cứng vẫn còn thiếu hụt.

Điều này có nghĩa là đà tăng giá phần cứng vẫn chưa dừng lại, sẽ còn tiếp tục tăng. Và GitHub rất có thể sẽ siết chặt các dịch vụ miễn phí để chuyển sang thu phí hoàn toàn.

## Phải chăng Frontend là công việc lặp đi lặp lại?

Tôi thấy một nhà phát triển [nói rằng](https://jonno.nz/posts/what-if-your-browser-built-the-ui-for-you/), Frontend về bản chất là những công việc giống nhau: Hiển thị dữ liệu cho người dùng và để người dùng xử lý dữ liệu đó.

Anh ấy cảm thấy không cần thiết phải lặp lại việc giải quyết cùng một vấn đề.

Thế là anh ấy đã tạo ra một "[trình duyệt tự thích ứng](https://github.com/jonnonz1/adaptive-browser)". Nó tự động tạo giao diện UI qua AI, phía backend chỉ cần cung cấp dữ liệu và mô tả mục đích của trang web.

Không biết liệu đây có phải là cái kết cho Frontend?

## Adobe chỉnh sửa tệp hosts

Sản phẩm chính của công ty Adobe là bộ "Creative Cloud" bao gồm nhiều phần mềm nổi tiếng như Photoshop, Illustrator, Premiere.

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040404.webp)

Một cư dân mạng sau khi cài đặt đã sốc khi phát hiện chương trình cài đặt đã [chỉnh sửa](https://www.reddit.com/r/webdev/comments/1sb6hzk/comment/oe1ap9h/) tệp hosts của mình.

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040403.webp)

Trong hình có thể thấy Adobe đã thêm một bản ghi DNS cục bộ vào tệp hosts.

Tại sao một ứng dụng lại phải chỉnh sửa tệp hệ thống?

Theo những người thạo tin tiết lộ, đây là để kiểm tra xem người dùng có cài đặt Creative Cloud hay không. Khi người dùng truy cập trang web chính thức, trang web sẽ gửi một yêu cầu đến tên miền trong hình. Vì bản ghi DNS của tên miền đó chỉ có ở cục bộ, nên nếu máy chủ nhận được yêu cầu thì có nghĩa là người dùng đã cài đặt Creative Cloud.

Một phần mềm danh tiếng như vậy mà lại nghĩ ra cách giải quyết kiểu "cửa sau" này, hơn nữa đối tượng lại là những người trả tiền cho họ, thật khiến người ta không biết nói gì hơn.

## Bài viết

1、[Cấu trúc lớp dưới của giao diện MDN mới](https://developer.mozilla.org/en-US/blog/mdn-front-end-deep-dive/) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040801.webp)

MDN là trang web tài liệu lớn nhất Internet. Bài viết này giới thiệu kiến trúc Frontend của trang web này, không ngờ nó lại phức tạp đến thế.

2、[Giết chết kẻ viết mã đó đi](https://windliang.wang/2026/03/31/%E6%9D%80%E6%AD%BB%E9%82%A3%E4%B8%AA%E5%86%99%E4%BB%A3%E7%A0%81%E7%9A%84%E4%BA%BA/) (tiếng Trung)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040813.webp)

Tác giả là một lập trình viên Frontend tại một công ty lớn, nhìn lại một năm qua của mình từ việc viết mã bằng tay chuyển sang lập trình bằng AI. AI đã thay đổi mọi thứ, xóa tan nỗi lo "nghỉ hưu ở tuổi 35". ([@wind-liang](https://github.com/ruanyf/weekly/issues/9545) đóng góp)

3、[Tôi đã xây dựng cổng tin nhắn SMS bằng điện thoại Android như thế nào](https://jonno.nz/posts/built-an-sms-gateway-with-a-20-dollar-android-phone/) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040302.webp)

Tác giả giới thiệu cách cài đặt một cổng tin nhắn SMS trên một chiếc điện thoại Android cũ để thu phát tin nhắn qua mạng (sử dụng gói cước của chính bạn).

4、[Sử dụng QEMU để kiểm tra thứ tự byte Big-Endian](https://www.hanshq.net/big-endian-qemu.html) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040402.webp)

Một bài hướng dẫn sơ cấp về ngôn ngữ C, thông qua máy ảo QEMU trên máy tính để chạy một chương trình chưa đầy mười dòng mã là có thể xem được một kiến trúc là Big-Endian hay Little-Endian.

6、[Tính năng importtime của Python](https://simonwillison.net/2025/Jun/20/python-importtime-graph/) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202506/bg2025062101.webp)

Python sử dụng lệnh import để nạp mô-đun, việc này tốn tài nguyên hiệu năng. Bài viết giới thiệu tính năng importtime tích hợp sẵn, có thể hiển thị thời gian tiêu tốn để nạp từng mô-đun.

7、[Thảm họa tàu ngầm hạt nhân Kursk năm 2000](https://rarehistoricalphotos.com/kursk-submarine-disaster-photos/) (tiếng Anh)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040808.webp)

Tháng 8 năm 2000, tàu ngầm hạt nhân "Kursk" của Nga đã bị nổ và chìm trong một buổi diễn tập, toàn bộ 118 thành viên thủy thủ đoàn tử nạn. Tai nạn này diễn ra rất chậm chạp, hiện trường hỗn loạn, công tác cứu hộ liên tục bị trì hoãn. Bài viết sử dụng nhiều bức ảnh để tái hiện lại toàn bộ quá trình.

## Công cụ

1、[Google AI Edge Gallery](https://apps.apple.com/nl/app/google-ai-edge-gallery/id6749645337)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040601.webp)

Tuần này, Google đã chính thức ra mắt một ứng dụng iPhone để cung cấp mô hình Gemma 4 sử dụng ngoại tuyến cho điện thoại. Không cần lên mạng, điện thoại cũng có thể sử dụng mô hình lớn.

2、[apfel](https://apfel.franzai.com/)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040401.webp)

Máy tính Mac có tích hợp sẵn một mô hình lớn có thể dùng ngoại tuyến. Tuy nhiên mặc định chỉ có Siri của Apple mới gọi được. Sau khi cài đặt công cụ này, bạn có thể tự gọi nó qua dòng lệnh.

3、[Docking](https://docking.cc/)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040701.webp)

Thêm thanh dock kiểu Apple cho desktop Linux.

4、[Tantivy](https://github.com/quickwit-oss/tantivy)

Thư viện công cụ tìm kiếm toàn văn viết bằng Rust, có thể thay thế Apache Lucene, xem thêm [bài giới thiệu](https://www.paradedb.com/blog/tantivy-interview).

5、[Open Screen](https://github.com/siddharthvaddem/openscreen)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040501.webp)

Ứng dụng desktop đa nền tảng dùng để quay màn hình sau đó tạo video giới thiệu, cung cấp nhiều tính năng chỉnh sửa đi kèm.

6、[epub-tts](https://github.com/rafael1mc/epub-tts)

Công cụ mã nguồn mở này chuyển tệp epub thành tệp âm thanh, tức là chuyển sách điện tử thành sách nói.

7、[NVTOP](https://github.com/Syllo/nvtop)

![](https://cdn.beekka.com/blogimg/asset/202403/bg2024031301.webp)

Một chương trình dòng lệnh cho hệ thống Linux dùng để giám sát trạng thái card đồ họa GPU, tương đương với lệnh top dành riêng cho card đồ họa.

8、[dmcheck](https://github.com/PlayerYK/dmcheck)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040812.webp)

Kiểm tra tình trạng chiếm dụng tên miền của một từ khóa chủ đề. ([@PlayerYK](https://github.com/ruanyf/weekly/issues/9542) đóng góp)

9、[Reze Studio](https://github.com/AmyangXYZ/reze-studio)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040901.webp)

Trang web chỉnh sửa đường cong hoạt ảnh mã nguồn mở. ([@AmyangXYZ](https://github.com/ruanyf/weekly/issues/9555) đóng góp)

10、[gitlogue](https://github.com/unhappychoice/gitlogue)

Công cụ này có thể tái hiện lịch sử gửi mã (commit) của kho Git dưới dạng hoạt ảnh trên terminal, thậm chí có thể hiển thị làm trình bảo vệ màn hình.

## Tài nguyên

1、[Phật Tân (Phật điển)](https://fojin.app/)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040301.webp)

Nền tảng hội tụ số hóa các cổ tịch Phật giáo toàn cầu. ([@xr843](https://github.com/ruanyf/weekly/issues/9507) đóng góp)

2、[Flight Viz](https://flight-viz.com/)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040811.webp)

Hiển thị 3D thời gian thực các chuyến bay trên toàn cầu. ([@haojiang99](https://github.com/ruanyf/weekly/issues/9538) đóng góp)

3、[Dòng thời gian GPU](https://sheets.works/data-viz/every-gpu)

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040809.webp)

Trang web này sử dụng hình ảnh để trình bày quá trình phát triển của card đồ họa GPU, từ card Voodoo năm 1996 đến card RTX 5090 năm 2025.

## Hình ảnh

1、[Cách đơn giản để xanh hóa núi trọc](https://www.sciencealert.com/how-12-000-tonnes-of-dumped-orange-peel-produced-something-nobody-imagined)

Costa Rica ở Trung Mỹ sản xuất nước cam và tạo ra một lượng lớn vỏ cam, trước đây đều được chôn lấp như rác thải.

Một tổ chức môi trường đã thuyết phục nhà máy đổ 12.000 tấn vỏ cam lên những ngọn núi trọc để làm phân bón.

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040802.webp)

Ngọn núi được phủ kín vỏ cam, ngoài ra không thực hiện bất kỳ xử lý nào khác.

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040803.webp)

Sau 6 tháng, vỏ cam thối rữa hoàn toàn trở thành đất đen và bắt đầu mọc cây cối.

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040804.webp)

16 năm sau, khi các nhà khoa học quay lại hiện trường, nơi đó đã là một khu rừng rậm rạp.

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040805.webp)

Đây thực sự là cách đơn giản nhất để phủ xanh núi trọc, chỉ cần chất đầy vỏ cam và để chúng tự thối rữa là xong.

2、[Cuộc thi nhiếp ảnh vật lý toàn cầu 2025](https://www.quantamagazine.org/global-physics-photowalk-2025-winners-revealed-20260401/)

16 phòng thí nghiệm vật lý hạt bao gồm Mỹ, Pháp, Nhật Bản... đã phối hợp tổ chức một cuộc thi nhiếp ảnh, mời các nhiếp ảnh gia chụp ảnh phòng thí nghiệm vật lý để quảng bá vật lý học đến công chúng.

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040806.webp)

Hình trên là phòng thí nghiệm máy dò nhiệt độ thấp của Viện Vật lý Hạt nhân Quốc gia Ý (INFN), nó có thể làm lạnh vật chất xuống mức chỉ hơi cao hơn độ không tuyệt đối một chút.

![](https://cdn.beekka.com/blogimg/asset/202604/bg2026040807.webp)

Hình trên được chụp tại Trung tâm Nghiên cứu Máy gia tốc Quốc gia Ion nặng của Pháp, thiết bị trong ảnh là hệ thống cấp điện của máy gia tốc tuyến tính.

Xem thêm ảnh tại [đây](https://www.quantamagazine.org/global-physics-photowalk-2025-winners-revealed-20260401/).

## Điểm tin

1、[Tại sao cát lại dính?](https://www.mentalfloss.com/posts/why-is-sand-sticky)

Khi chúng ta đi chơi biển, cát thường dính vào da, giày dép, quần áo và tóc.

![](https://cdn.beekka.com/blogimg/asset/202304/bg2023042604.webp)

Thành phần chính của cát là silic dioxide, giống như đá. Đá không dính, tại sao cát lại dính?

Hóa ra bản thân cát không dính nhưng có tính ưa nước, nó sẽ hút nước. Cơ thể con người cũng ưa nước và thường đổ mồ hôi nhễ nhại dưới nắng gắt. Khi cát tiếp xúc với vật ẩm ướt, lực dính sẽ phát sinh giữa các phân tử nước.

Trên da thường còn có dầu hoặc kem chống nắng, chúng cũng khiến cát dính chặt vào da.

Ngoài ra, da còn có những nếp nhăn siêu nhỏ cũng làm cát bị kẹt lại.

Tóm lại, muốn loại bỏ cát thì hãy đợi cho da khô hoặc dùng nước rửa sạch.

## Trích dẫn

1、

Nếu bạn nghĩ tốc độ viết mã là vấn đề của bạn thì vấn đề bạn đối mặt còn lớn hơn nhiều.

-- [Andrew Murphy](https://andrewmurphy.io/blog/if-you-thought-the-speed-of-writing-code-was-your-problem-you-have-bigger-problems), lập trình viên người Úc.

2、

Có một kiểu hưng phấn mà chỉ những người mới tiếp xúc với tiền điện tử vào năm 2017 mới có.

-- [Andrew Murphy](https://andrewmurphy.io/blog/if-you-thought-the-speed-of-writing-code-was-your-problem-you-have-bigger-problems), lập trình viên người Úc.

3、

Một cuộc thăm dò dư luận cho thấy giới trẻ Mỹ coi trọng hôn nhân, con cái và đức tin kém xa cha mẹ họ. Họ cũng tỏ ra lạnh nhạt với các giá trị truyền thống như lòng yêu nước, tôn giáo, cộng đồng và gia đình.

Người trẻ coi thị trường và tiền bạc là chuẩn mực đạo đức. Trong mắt họ, thị trường quyết định giá trị của sự vật, ý nghĩa của sự kiện, ai đúng, ai là người chiến thắng và ai là người quan trọng.

-- [《Hậu quả tồi tệ nhất của các thị trường dự đoán》](https://www.derekthompson.org/p/we-havent-seen-the-worst-of-what)

4、

Đối với tôi, thành phố tương lai thực sự giống như Amsterdam với những con phố dễ chịu và làn đường dành cho xe đạp, chứ không phải giống như Dubai với những xa lộ 16 làn xe và một nhóm lao động bị áp bức làm việc trong các trung tâm mua sắm xa hoa phô trương.

-- [Một độc giả trên Hacker News](https://news.ycombinator.com/item?id=47643388)

5、

Các trường đại học đều yêu cầu nghiên cứu sinh tiến sĩ phải công bố bài báo. Còn bạn viết gì, viết thế nào, nội dung có liên quan đến hướng nghiên cứu hay không thì khoa thực ra đều không quan tâm. Khoa cần bài báo vì bài báo có thể chứng minh tính hợp lý của kinh phí, mà kinh phí lại chứng minh giá trị tồn tại của khoa. Sinh viên chẳng qua chỉ là tư liệu sản xuất để đạt được mục tiêu đó mà thôi.

-- [《Máy móc không có vấn đề, vấn đề nằm ở chính chúng ta》](https://ergosphere.blog/posts/the-machines-are-fine/)

## Nhìn lại các năm trước

[HDMI 2.2 có lẽ là điểm dừng của âm thanh hình ảnh](https://www.ruanyifeng.com/blog/2025/04/weekly-issue-345.html) (#345)

[Đồng hồ bóng đèn khéo léo](https://www.ruanyifeng.com/blog/2024/03/weekly-issue-295.html)（#295）

[Những tòa nhà chọc trời là phản nhân loại](https://www.ruanyifeng.com/blog/2023/03/weekly-issue-245.html)（#245）

[Bạn đã bao giờ làm dự án mà không quan tâm kết quả chưa?](https://www.ruanyifeng.com/blog/2022/02/weekly-issue-195.html)（#195）

(Hết)
