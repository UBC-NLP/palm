Annotation Guideline:

**This document serves as a set of annotation guidelines for constructing an Instruction dataset.**

The instruction dataset is a diverse dataset in different topics following the structure:

(Instruction, Input, output). The input can be a question about a certain topic or a particular type of request or instruction.

Here is one example of instruction in the form of a **question and answer**:

**Question:**

كم عدد السلالات الحاكمة في مصر القديمة؟

**Answer:**

تنقسم فترة الأسرة الحاكمة للحكام المصريين الأصليين فى عصر الفراعنة عمومًا إلى ٣٠ أسرة وفقا لما ورد ذكره فى كتب الكاتب والمؤرخ اليوناني المصري مانيتون أوائل القرن الثالث قبل الميلاد، والتي تم حفظ مقتطفات مما ذكره في أعمال الكتاب اللاحقين.

السلالات الأولى والثانية (السلالة المبكرة).

السلالات الثالثة إلى السادسة (المملكة القديمة).

السلالات من سبعة إلى عشرة.

السلالات من ١٢ إلى ١٣ (المملكة الوسطى).

السلالات من ١٤ إلى ١٧ (شعوب الهكسوس).

السلالات من ١٨ إلى ٢٠ (المملكة الحديثة).

السلالات من ٢١ إلى ٢٤ (الفترة المتوسطة الثالثة).

السلالات من ٢٥ إلى ٣٠ (الفترة المتأخرة).

In the form of **request and response** to the request:

**Request:**

أكتب نبذه عن قيس بن الخطيم

**Response to the request:**

قيس بن الخطيم بن عدي الأوسي، وكنيته أبو يزيد، (توفي 2 قبل الهجرة / 620 م) شاعر عربي من صناديد الجاهلية وأشد رجالها. قُتل أبوه وهو صغير، قتله رجل من الخزرج. فلما بلغ، قتل قاتل أبيه، ونشبت لذلك حروب بين قومه وبين الخزرج.

يقول الصفدي صاحب الوافي بالوفيات عنه: «كان قيس مقرون الحاجبين، أدعج العينين، أحم الشفتين، براق الثنايا كأن بينهما برقاً، ما رأته حليلة رجل قط إلا ذهب عقلها». وله في وقعة بعاث التي كانت بين الأوس والخزرج قبل الهجرة أشعار كثيرة. أدرك الإسلام وتريث في قبوله، فقتل قبل أن يدخل فيه. أسلمت زوجته حواء الأنصارية وكانت قد كتمت إسلامها عنه خوفا من التضرر للتحريض الشديد من القرشيين على النبي محمد.

## **Supported domains:**

### General domains

Note that we can create much more diverse instructions where we can ask the model to {_write, summarize, propose, list…_} based on different domains. For example, domains can be from the set {_biology, chemistry, physics…_}. Later in the guide, we will dive into these details.

For the general domains, we will start with a limited list as follows:

1. Science: Biology
2. Science: Physics
3. Science: Chemistry
4. Science: Math
5. Science: Astronomy
6. Sports
7. Technology.

### #Country-specific domains

One other focus we will have is on different Arab countries.

In the country-specific domains, we are interested in instructions that are related to countries.

Here is one instruction example in the form of a **question and answer** related to Sudan.

**Question:**

بماذا تشتهر مدينة الخرطوم في السودان؟

**Answer:**

تشتهر الخرطوم بالسياحة النهرية على نهر النيل حيث توجد البواخر النيلية وقوارب الفلوكة والزوارق والقوارب الشراعية والعبّارات والتي تمخر مياه النيلين الأزرق والأبيض وتعبر بركابها إلى جزيرة توتي وسط النيل حيث البساتين التقليدية النضرة. وتوجد المراكب بالقرب من المقرن وجزيرة توتي وجزيرة التمساح، وتقوم برحلات نهارية وليلية.

In the form of a **request and response** to the request:

**Request:**

أكتب نبذة عن مدينه دمياط

**Response to the request:**

مدينة دمياط هي عاصمة محافظة دمياط بأقصى شمال مصر، وبعدها بـ 15 كم يصب فرع دمياط من النيل في البحر الأبيض المتوسط عند رأس البر. يفصلها شريط ضيق عن بحيرة المنزلة، وإلى الجنوب الغربي تمتد مزارع وجه بحري (دلتا النيل) وسهولها. ويعتبر ميناء دمياط أحد أهم موانئ مصر فينشط استقبالاً للسفن وتتكثف فيه حركة البضائع.

تتميز دمياط بكثرة مزارع الجوافة وخصوصا في كفر البطيخ. وأيضا أشجار النخيل البالغ عددها نحو 2,5 مليون، والتي تغطى الساحل من رأس البر شرقا وحتى جمصة غربا ومن البحر شمالا وحتى الطريق السريع وجنوب قرية الرياض جنوبا، باستثناء منطقة دمياط الجديدة. وقد صدرت دمياط فوق المليون نخلة إلى عدة دول أهمها اليونان والصين.

For country-specific domains, we will start with a limited list as follows:

1. Local geography of a given country
2. Literature produced by individuals from a given country.
3. History of a given country.
4. Politics of a given country.
5. Travel inside a given country.
6. Celebrations in a given country.
7. Fauna, flora, and environmental life in a given country.
8. Religion in a given country.
9. Sports in a given country.

## **Trustworthy sources:**

We strongly recommend trustworthy sources, and we recommend checking these sources to trust their information.

Examples of trustworthy sources include:

- Wikipedia
- Online encyclopedias
- Books
- Governmental websites,
- Specialized websites (e.g., websites that provide medical information).

Some online sources may be less trustworthy, such as websites based on information by a single individual **(posts, social media)** unless said individual is an authority in the field (expert, professor…).

For some domains, such as travel, food, and country-specific celebrations, the most valuable information may come from online discussions and web fora. That means we can treat these as highly relevant and valuable sources for these domains.

Overall, feel free to use your intuition about what a trustworthy source is.

## **General Guidelines:**

- All instructions and answers should be written in Modern Standard Arabic (MSA).
- Answers should not be subjective…. (continue explanation)
- We should construct the instructions in diverse ways. For example, an instruction that asks the model to provide information about a certain concept, place, or event can use different types of language. Here are some examples:

| Instruction 1 | اعطني نبذة مختصرة عن مدينة الرباط. |
| --- | --- |
| Instruction 2 | اكتب ثلاث فقرات عن مدينة الرباط. |
| Instruction 3 | فيما لا يقل عن 10 أسطر, تحدث عن مدينة الرباط. |
| Instruction 4 | تكلم عن مدينة الرباط. |

- The output should always be unique. We should not have duplicates of instructions and their outputs. Again, here are more examples:
  - بماذا تشتهر مدينة دمياط
    - تشتهر محافظة دمياط بعدد من الصناعات والحرف التي عرفت بها منذ القدم وعُرف أبناؤها في كافة دول العالم بمهارتهم التي حفرت الأخشاب وحولتها لتحف فنية زينت معارض عالمية بإيطاليا، بالإضافة لمهارة صياديها الذين سافروا إلى كل بلدان العالم الواقعة على البحرين الأبيض والمتوسط.
  - أكتب نبذه عن مدينه دمياط
    - عند رأس البر. يفصلها شريط ضيق عن بحيرة المنزلة، وإلى الجنوب الغربي تمتد مزارع وجه بحري (دلتا النيل) وسهولها. ويعتبر ميناء دمياط أحد أهم موانئ مصر فينشط استقبالاً للسفن وتتكثف فيه حركة البضائع. تتميز دمياط بكثرة مزارع الجوافة وخصوصا في كفر البطيخ. وأيضا أشجار النخيل البالغ عددها نحو 2,5 مليون، والتي تغطى الساحل من رأس البر شرقا وحتى جمصة غربا ومن البحر شمالا وحتى الطريق السريع وجنوب قرية الرياض جنوبا، باستثناء منطقة دمياط الجديدة. وقد صدرت دمياط فوق المليون نخلة إلى عدة دول أهمها اليونان والصين.
- In general, we suggest that you try to be creative and come up with diverse instructions to avoid any repetitions
- You could get an answer by a simple online search. However, you should verify each answer and provide the URL of the source (a column will be provided for this purpose).
- Depending on the instruction, the beginning paragraph of the answer should vary,
  - **Example 1:**
    - Request: Give me a list of …….
    - Answer: Absolutely, here is a list:
      - **1-**.........
      - **2-**............
      - **3-**……..
  - **مثال ١:**
    - **طلب:** أعطني قائمة من …….
    - **جواب:** بكل تاكيد، اليك قائمه:
      - **1-**.........
      - **2-**............
      - **3**\-……..
  - **Example 2**
    - **Request:** Explore the main elements in…….
    - **Answer:** ……are……, the main elements in…..
  - **مثال ٢**:
    - **طلب:** استكشف العناصر الرئيسة في…….
    - **جواب:** ……هي……, العناصر الرئيسة في…………
  - **Example 3**
    - **Request:** Reformat the given text using this format
      - **Text:**...........................
      - **Format:**
        - Introduction:..........
        - Discussion:............
        - Conclusion:................
  - **Example 4**
    - **Request:** Write a 1,000-word paragraph in a formal tone, analyzing and providing examples of how ……. have been utilized …………. In your analysis, discuss……….
  - **مثال ٤**: اكتب فقرة من الف كلمة بأسلوب رسمي، حلل وقًدم أمثلة عن كيفية استخدام … في … في تحليك، ناقش …
  - **Example 5:**
    - **Request:** Restructure the following text so that examples should be listed in bullets, the main idea should be in Bold,...........
      - **Text:**.......................................
      - **مثال ٥:**

**طلب:** أعد صياغة النص التالي بحيث أن الأمثلة يجب تكون على شكل نقاط، وتكون الفكرة الرئيسية بخط عريض.

**النص:** …

- - **Example 6:**
        - **Request:** Compose a new way to ask the same question. The new question must be asking the exact same thing as the original question does.
            - **Input question:**..............................
            - **مثال ٦:**
            - **طلب:** صغ طريقة جديدة لطرح نفس السؤال. يجب أن يحتوي السؤال الجديد على نفس الشئ الذي يطرحه السؤال الأصلي.
            - **السؤال المدخل:**

## **Detailed Information about Domains**

### Politics (Can be country-specific or general)

The political domain is multidisciplinary in nature, drawing from fields such as political science, international relations, public administration, law, economics, sociology, and philosophy.

#### Possible subtopics include but are not limited to

- **Political Systems and Ideologies**
  - Democracy, authoritarianism, socialism, capitalism, communism, etc.
  - Forms of government: presidential, parliamentary, federal, unitary, etc.
  - Political ideologies: liberalism, conservatism, socialism, nationalism, etc.
  - **Examples**:
    - What are the different presidential systems of government? (General domain)
    - Discuss the presidential system in the Arab Republic of Egypt. (Country specific)
    - What is the monarch system of government? In addition, list examples of a monarchy government in the Arab world. (General domain)
    - Write an overview of the government system in Saudi Arabia. (Country specific)
    - What is communism in simple words? (General domain)
    - Explain The Concept of “Political Globalization.” (General domain)
- **النظم السياسية والأيديولوجيات**
  - الديمقراطية، الاستبداد، الاشتراكية، الرأسمالية، الشيوعية، الخ.
  - أشكال الحكم: رئاسية، برلمانية، فدرالية، إلخ.
  - الأيديولوجيات السياسية: الليبرالية، المحافظة، الاشتراكية، القومية، إلخ.
  - **أمثلة**:
    - أعطني فكرة عن نظم الحكم الرئاسية. (General domain)
    - تحدث عن نظام الحكم الرئاسي في جمهورية مصر العربية. (Country specific)
    - ما هي نظم الحكم الملكية؟ مع ذكر أمثلة عن نظم الحكم الملكية في العالم العربي.(General domain)
    - أكتب نبذة عن نظام الحكم في المملكة العربية السعودية.(Country specific)
    - ما هي الفلسفة الشيوعية؟ (General domain)
    - أكتب نبذة عن العولمة. (General domain)
- **Political Institutions and Structures:**
  - Executive branch: presidency, prime minister, cabinet, bureaucracy.
  - Legislative branch: parliament, congress, senate, elections, political parties.
  - Judicial branch: courts, legal systems, rule of law, constitutionalism.
  - **Examples**:
    - What is the difference between political structures and political institutions? (General domain)
    - What are the main characteristics and roles of the executive, legislative, and judicial branches in democratic political systems? (General domain)
    - What is the structure and function of the House of Representatives in the Egyptian political system, and how does it shape the legislative process? (Country specific)
- **المؤسسات والهياكل السياسية**
  - السلطة التنفيذية: الرئاسة، رئيس الوزراء، مجلس الوزراء، البيروقراطية.
  - السلطة التشريعية: البرلمان، ، الانتخابات، الأحزاب السياسية.
  - السلطة القضائية: المحاكم، الأنظمة القانونية، سيادة القانون، الدستورية.
  - **أمثلة**:
    - ما الفرق بين الهياكل السياسية والمؤسسات السياسية؟(General domain)
    - ما هي الخصائص والأدوار الرئيسية للسلطات التنفيذية والتشريعية والقضائية في الأنظمة السياسية الديمقراطية؟(General domain)
    - ما هو هيكل ووظيفة مجلس النواب في النظام السياسي المصري، وكيف يشكل العملية التشريعية؟(Country specific)
- **International Relations and Diplomacy**
  - Foreign policy: diplomatic relations, treaties, alliances, international organizations.
  - Global governance: United Nations, World Trade Organization, European Union.
  - Conflict resolution, peacekeeping, and humanitarian interventions.
  - **Examples:**
    - Discuss the following statement: “Realism remains the most compelling theoretical framework for understanding international relations, despite the challenges posed by other views.”(General domain)
    - How do international organizations, such as the United Nations and the World Trade Organization, contribute to global governance and cooperation between countries? (General domain)
    - What role does Saudi Arabia play in shaping the diplomatic landscape of the Gulf region and its relations with neighboring countries? (Country specific)
- **العلاقات الدولية والدبلوماسية**
  - السياسة الخارجية: العلاقات الدبلوماسية، المعاهدات، التحالفات، المنظمات الدولية.
  - الحوكمة العالمية: الأمم المتحدة، منظمة التجارة العالمية، الاتحاد الأوروبي.
  - حل النزاعات وحفظ السلام والتدخلات الإنسانية.
  - **أمثلة:**
    - ناقش العبارة التالية: "تظل الواقعية هي الإطار النظري الأكثر إقناعًا فهم العلاقات الدولية، على الرغم من التحديات التي تطرحها وجهات النظر الأخرى.(General domain)
    - كيف تساهم المنظمات الدولية، مثل الأمم المتحدة ومنظمة التجارة العالمية، في الحوكمة العالمية والتعاون بين الدول؟(General domain)
    - ما هو الدور الذي تلعبه السعودية في تشكيل المشهد الدبلوماسي لمنطقة الخليج وعلاقاتها مع دول الجوار؟(Country specific)
- **Elections and Voting Systems**
  - Electoral systems: proportional representation, first-past-the-post, ranked-choice voting.
  - Campaigns, political advertising, public opinion, polling.
  - Election laws, voter registration, electoral reforms.
  - **Examples**:
    - Are there different types of elections? If so, what are they? What makes them different? (General domain)
    - What is the difference between a legislative referendum and a popular referendum? (General domain)
    - How does the parliamentary election system work in Egypt? (Country specific)
    - How many political parties are there in Morocco? (Country specific)
- **الانتخابات وأنظمة التصويت**
  - الأنظمة الانتخابية: التمثيل النسبي، التصويت على أساس الأكثرية، التصويت حسب الترتيب.
  - الحملات، الإعلانات السياسية، الرأي العام، استطلاعات الرأي.
  - قوانين الانتخابات، تسجيل الناخبين، الإصلاحات الانتخابية.
  - **أمثلة:**
    - هل هناك أنواع مختلفة من الانتخابات؟ إذا كان الأمر كذلك، ما هي هم؟ ما الذي يجعلهم مختلفين؟.(General domain)
    - ما الفرق بين الاستفتاء التشريعي والاستفتاء الشعبي؟.(General domain)
    - كيف يعمل نظام الانتخابات البرلمانية في مصر؟(Country specific)
    - كم عدد الأحزاب السياسية في المغرب؟(Country specific)
- **Political Philosophy and Political Thought**
  - Political theorists: Plato, Machiavelli, Rousseau, Marx, Rawls, etc.
  - Concepts like justice, equality, liberty, rights, democracy.
  - **Examples**:
    - Describe the idea of moral equality and explain its importance in the context of various problems in political philosophy. (General domain)
    - What is Weber’s definition of politics? (General domain)
    - What are the political theories developed by Ibn Khaldun? (Country specific)
- **الفلسفة السياسية والفكر السياسي**
  - المناظرون السياسيون: أفلاطون، مكيافيلي، روسو، ماركس، راولز، إلخ.
  - مفاهيم مثل العدالة والمساواة والحرية والحقوق والديمقراطية.
  - **أمثلة:**
    - وصف فكرة المساواة الأخلاقية وأشرح أهميتها في سياقها مشاكل مختلفة في الفلسفة السياسية.(General domain)
    - ما هو تعريف السياسة عند فيبر؟(General domain)
    - ما هي النظريات السياسية التي وضعها ابن خلدون؟(Country specific)
- **Government and Executive Branch:** Government and executive branch questions/instructions focus on the structure, powers, and functioning of the executive branch, including the roles of the president or prime minister and their relationship with other branches of government.
  - **Examples**
    - What are the responsibilities and powers of the president in Country X, and how do they differ from those of the prime minister?
    - What powers do presidents assume, often during crises, based on the constitutional phrase “executive power of the president”? (Country specific)
- **الحكومة والسلطة التنفيذية**: تركز أسئلة/تعليمات الحكومة والسلطة التنفيذية على هيكل السلطة التنفيذية وصلاحياتها وعملها، بما في ذلك أدوار الرئيس أو رئيس الوزراء وعلاقتهما بفروع الحكومة الأخرى.
  - **أمثلة:**
    - : ما هي مسؤوليات وصلاحيات الرئيس في الدولة X، وكيف تختلف عن تلك التي يتمتع بها رئيس الوزراء؟(Country specific)
    - ما هي الصلاحيات التي يتولاها الرؤساء، غالباً أثناء الأزمات، استناداً إلى العبارة الدستورية “السلطة التنفيذية للرئيس”؟ (Country specific)
- **Legislative and Lawmaking:** Legislative and lawmaking questions/instructions examine the structure, composition, and functioning of the legislative body, including the process of lawmaking and the role of lawmakers.
  - **Examples**
    - How does the legislature in Country X pass and enact new laws, and what are the major legislative priorities? (Country specific)
    - Does the legislative process include the process of implementing the law once it is issued? (Country specific)
- **التشريع وسن القوانين:** تتناول الأسئلة/التعليمات حول التشريع وسن القوانين هيكله وتكوين وعمل الهيئة التشريعية، بما في ذلك عملية سن القوانين ودور المشرعين.
  - **أمثلة:**
    - كيف تقوم الهيئة التشريعية في الدولة X بتمرير وسن قوانين جديدة، وما هي الأولويات التشريعية الرئيسية؟(Country specific)
    - هل تشمل العملية التشريعية عملية تطبيق القانون بمجرد صدوره؟(Country specific)
- **Judiciary and Legal System:** Judiciary and legal system questions/instructions focus on the structure, independence, and functioning of the judiciary, including the appointment of judges, judicial review, and the rule of law.
  - **Examples**
    - How does the judicial system in Country X ensure the independence of the judiciary and protect the rights of citizens? (Country specific)
    - Which of the following relates to the power of judicial review?
      - Advising the President on constitutional matters
      - Declaring unconstitutional laws of Parliament that conflict with the Constitution
      - Review the organization of the judiciary
      - Preparing laws to maintain the rule of law
- **القضاء والنظام القانوني**: تركز الأسئلة/التعليمات الخاصة بالنظام القضائي والقانوني على هيكل السلطة القضائية واستقلالها وعملها، بما في ذلك تعيين القضاة والمراجعة القضائية وسيادة القانون.
  - **أمثلة:**
    - كيف يضمن النظام القضائي في الدولة X استقلال القضاء ويحمي حقوق المواطنين؟(Country specific)
    - أي من الإجراءات التالية تتعلق بسلطة المراجعة القضائية؟
      - تقديم المشورة للرئيس في المسائل الدستورية
      - إعلان عدم دستورية قوانين البرلمان التي تتعارض مع الدستور
      - مراجعة تنظيم السلطة القضائية
      - إعداد القوانين للحفاظ على سيادة القانون
- **Foreign Policy and International Relations:** Foreign policy and international relations questions/instructions address a country's relationships with other nations, its diplomatic strategies, and its engagement in international organizations and agreements.
  - **Example**: What are the key foreign policy priorities and alliances of Country X, and how do they shape its international relations?(Country specific)
- **السياسة الخارجية والعلاقات الدولية:** تتناول أسئلة/تعليمات السياسة الخارجية والعلاقات الدولية علاقات الدولة مع الدول الأخرى، واستراتيجياتها الدبلوماسية، ومشاركتها في المنظمات والاتفاقيات الدولية.
  - **أمثلة:**
    - ما هي الأولويات والتحالفات الرئيسية للسياسة الخارجية للدولة X، وكيف تشكل علاقاتها الدولية؟(Country specific)
- **Regional and Ethnic Politics:** Regional and ethnic politics questions/instructions examine the dynamics of regionalism, ethnic diversity, and identity politics within the country, including issues of autonomy, decentralization, and minority rights.
  - **Example**: How does Country X manage regional tensions and promote inclusivity and representation of ethnic minorities?(Country specific)
- **السياسة الإقليمية والعرقية:** تتناول أسئلة/تعليمات السياسة الإقليمية والعرقية ديناميكيات النزعة الإقليمية والتنوع العرقي وسياسات الهوية داخل الدولة، بما في ذلك قضايا الحكم الذاتي واللامركزية وحقوق الأقليات.
  - **أمثلة:**
    - كيف تدير الدولة X التوترات الإقليمية وتعزز الشمولية وتمثيل الأقليات العرقية؟(Country specific)
- **Political Movements and Activism**
  - Social movements, civil rights, feminism, environmentalism.
  - Protests, demonstrations, activism strategies.
  - Political participation, grassroots mobilization.
  - **Example:**
    - How do social media and digital platforms impact the organization and mobilization of political movements and activism globally? (General domain)
- **الحركات السياسية والنشاط**
  - الحركات الاجتماعية، الحقوق المدنية، الحركة النسوية، حماية البيئة.
  - الاحتجاجات والمظاهرات واستراتيجيات النشاط.
  - المشاركة السياسية والتعبئة الشعبية.
  - **أمثلة:**
    - كيف تؤثر وسائل التواصل الاجتماعي والمنصات الرقمية على تنظيم وتعبئة الحركات السياسية والنشاط على مستوى العالم؟(General domain)
- **Political Economy and Public Policy**
  - Economic systems, fiscal policy, monetary policy.
  - Welfare state, social policies, healthcare, education, infrastructure.
  - Taxation, budgets, public expenditure, government intervention.
- **الاقتصاد السياسي والسياسة العامة**
  - النظم الاقتصادية، السياسة المالية، السياسة النقدية.
  - دولة الرفاهية، السياسات الاجتماعية، الرعاية الصحية، التعليم، البنية التحتية.
  - الضرائب، الميزانيات، الإنفاق العام، التدخل الحكومي.
  - **أمثلة:**
    - ما هي العوامل الرئيسية التي تساهم في نجاح أو فشل مبادرات السياسة العامة الرامية إلى معالجة عدم المساواة في الدخل والفقر؟(General domain)
    - كيف ساهم الاقتصاد السياسي لموارد النفط والغاز في تشكيل السياسة العامة وصنع القرار الاقتصادي في دول مثل إيران والعراق؟(Country specific)

#### Instructions could be but are not limited to

- **Explore** ………..
  - Explore the key principles and values associated with different political ideologies such as liberalism, conservatism, socialism, and nationalism. Examine their origins, core tenets, and how they shape political beliefs and policies.
  - استكشف المبادئ والقيم الأساسية المرتبطة بالأيديولوجيات السياسية المختلفة مثل الليبرالية والمحافظة والاشتراكية والقومية. افحص أصولهم ومبادئهم الأساسية وكيفية تشكيل معتقداتهم وسياساتهم السياسية.
- **Define** …………..
- **عرًف** التنشئة الاجتماعية السياسية
- **Compare between** ……… and …………..
  - Compare and contrast the electoral systems used in presidential systems and parliamentary systems. Analyze their differences in terms of representation, executive selection, and legislative functioning.
  - **قارن بين** الأنظمة الانتخابية المستخدمة في الأنظمة الرئاسية والأنظمة البرلمانية. وقارن/حلل الاختلافات بينهما من حيث التمثيل والاختيار التنفيذي والأداء التشريعي.
- **Investigate /Examine/Explore** ………….
  - Investigate the major challenges faced by democracies in ensuring fair and free elections. Examine issues such as voter suppression, electoral fraud, campaign finance, and the role of technology in elections.
  - تكلم عن التحديات الرئيسية التي تواجهها الديمقراطيات في ضمان انتخابات نزيهة وحرة. اشرح القضايا مثل قمع الناخبين، وتزوير الانتخابات، وتمويل الحملات، ودور التكنولوجيا في الانتخابات.
- **Which of the following statements is True**
  - a)....
  - b)....
  - c)....
- **What is the role of interest groups in politics?**
  - a) Shaping public opinion through media campaigns
  - b) Representing the interests of specific industries or advocacy causes
  - c) Appointing government officials
  - d) Conducting voter registration drives
- **ما هو دور جماعات المصالح في السياسة؟**
  - أ) تشكيل الرأي العام من خلال الحملات الإعلامية
  - ب) تمثيل مصالح صناعات محددة أو قضايا الدعوة
  - ج) تعيين المسؤولين الحكوميين
  - د) إجراء حملات تسجيل الناخبين
- **Identify** …………
  - Identify the country where the president is addressed as the President of the People's Republic and select the correct option:
    - a) China
    - b) Russia
    - c) Mexico
    - d) South Africa
  - **حدد الدولة التي يخاطب فيها الرئيس برئيس الجمهورية الشعبية وحدد الخيار الصحيح:**
    - أ) الصين
    - ب) روسيا
    - ج) المكسيك
    - د) جنوب أفريقيا

#### Examples

**Example 1**

| **Instruction** | في أي دولة يحمل الرئيس لقب رئيس الدولة ورئيس الحكومة؟ |
| --- | --- |
| **Input** | أ) المملكة المتحدة<br><br>ب) ألمانيا<br><br>ج) فرنسا<br><br>د) الولايات المتحدة |
| **Output** | د) الولايات المتحدة |
| **Source** |     |

Notice that we can ask the same question in these two ways as below in Example 2 and Example 3

**Example 2**

| **Instruction** | قارن بين المنظارين السياسيين: أفلاطون،و مكيافيلي |
| --- | --- |
| **Input** |     |
| **Output** |     |
| **Source** | <http://www.penacclaims.com/wp-content/uploads/2021/09/Gary-Jason-Godinho.pdf> |

**Example 3**

| **Instruction** | قارن بين المنظارين السياسيين: |
| --- | --- |
| **Input** | أفلاطون،و مكيافيلي |
| **Output** |     |
| **Source** | <http://www.penacclaims.com/wp-content/uploads/2021/09/Gary-Jason-Godinho.pdf> |

**Example 4**

<table><tbody><tr><th><p><strong>Instruction</strong></p></th><th><p>ما هي المبادئ الأساسية لليبرالية في العلاقات الدولية؟</p></th></tr><tr><td><p><strong>Input</strong></p></td><td></td></tr><tr><td><p><strong>Output</strong></p></td><td><p>الليبرالية هي مدرسة فكرية ضمن نظرية العلاقات الدولية والتي تدور حول ثلاثة مبادئ مترابطة:</p><ul><li>رفض سياسة القوة باعتبارها النتيجة الوحيدة الممكنة للعلاقات الدولية؛ فهي تشكك في مبادئ الواقعية الأمنية/الحربية</li><li>المنافع المتبادلة والتعاون الدولي</li><li>دور المنظمات الدولية والجهات الفاعلة غير الحكومية في تشكيل تفضيلات الدولة وخيارات السياسات</li></ul><p>تؤكد هذه المدرسة الفكرية على ثلاثة عوامل تشجع على المزيد من التعاون وتقليل الصراع بين الدول:</p><ul><li>المؤسسات الدولية، مثل الأمم المتحدة، التي توفر منتدى لحل النزاعات بطرق غير عنيفة</li><li>التجارة الدولية لأنه عندما تكون اقتصادات الدول مترابطة من خلال التجارة، فهي أقل عرضة للحرب مع بعضها البعض</li><li>انتشار الديمقراطية، حيث أن الديمقراطيات الراسخة لا تخوض حربًا مع بعضها البعض، لذلك إذا كان هناك المزيد من الديمقراطيات، فإن الحرب بين الدول ستكون أقل تكرارًا</li></ul></td></tr><tr><td><p><strong>Source</strong></p></td><td><p>https://en.wikipedia.org/wiki/Liberalism_(international_relations)#:~:text=Liberalism%20is%20a%20school%20of,Mutual%20benefits%20and%20international%20cooperation</p></td></tr></tbody></table>

### Religion

Religion is a vast and multifaceted domain. It is a country-specific domain where we can discuss different types of religions based on the countries. Subtopics could include religious beliefs, practices, history, and the socio-cultural fabric of the country in question.

#### Possible subtopics could be but are not limited to

- **World religions:** Islam, Christianity, Hinduism, Buddhism, Judaism, etc. **الديانات العالمية**
- **Sacred texts:** Quran, Bible (Old Testament and New Testament), etc. **النصوص الدينية**
- **Religious practices and rituals:** Prayer, meditation, fasting, pilgrimage, Rites of passage (Baptism, marriage, funerals), etc. **الممارسات والطقوس الدينية**
- **Historical Development of** (Islam) in a given country (Egypt) **تطور الإسلام في مصر على مر التاريخ أو تاريخياً**
- **Major Islamic Denominations** **(المذاهب الإسلامية الأساسية)**
- **Islamic festivals and celebrations** (Eid Al Fitr and Eid Al-Adha) **الاحتفالات والأعياد الإسلامية**
- **Islamic places and pilgrimage sites** **أماكن ومواقع الحج الاسلامية**
- **Islamic Art and Architecture** **الفن والعمارة الاسلامية**: (Islamic calligraphy) **الخط الإسلامي**
- **Islamic personalities, figures, and scholars:** (Imam Al-Shafi, Ibn Khaldun) **الشخصيات و علماء المسلمين**
- **Islamic institutions and education** (the Role of Al-Azhar in the Islamic world) **التعليم الإسلامي والمؤسسات الإسلامية**
- **Islamic texts: Tafsir literature** (Exegesis of the Quran **تفسير القرآن وشرحه**)

#### Instructions could be but are not limited to

- **Explain** \[Religious topic\], E.g., Explain the five Pillars of Islam
- **اشرح** أركان الإسلام الخمسة؟
- **List the main** beliefs of \[Region\], e.g., List the main beliefs of Buddhism
- **اعط قائمة ب**المعتقدات الرئيسية للبوذية؟
- **Compare** \[religion 1\] with \[religion 2\], e.g., compare Hinduism with Buddhism
- **قارن بين** الديانة الهندوسية والبوذية
- **Provide** the origin story of \[religion\], e.g., Provide the origin story of Hinduism
- **قدم قصة** نشأة الهندوسية
- **Who** is the main prophet or figure of \[religion\], e.g., Who is the main prophet of Judaism
- **من هو** النبي الذي أرسل في اليهودية؟
- **Illustrate** the symbolism of \[religious element\], e.g., Illustrate the symbolism of the lotus flower in Buddhism
- **بيْن** رمزية زهرة اللوتس في البوذية
- **Identify** the pilgrimage sites for \[religion\], e.g., Identify the pilgrimage sites for Islam.
- **حدًد** مواقع إقامة شعائر الحج في الإسلام
- **Analyze** the moral teachings of \[religious figure\], e.g., the moral teachings of the prophet Muhammad PBUH
- **قم بتحليل** التعاليم الأخلاقية للنبي محمد صل الله عليه وسلم
- **Trace** the evolution of \[religious practice\] over time. E.g., trace the evolution of meditation in Hinduism over time.
- **تتبع تطور** التأمل في الهندوسية علي مر الزمان.
- **Discuss** the influence of \[religion\] on \[cultural aspect\], e.g., discuss the influence of Christianity on Western Art
- **ناقش تأثير** المسيحية على الفن الغربي
- **Examine** the role of women in \[religion\], e.g., Examine the role of women in Islam.
- **اشرح دور** المرأة في الإسلام
- **Explain** the concept of the afterlife in \[religion\], e.g., Explain the concept of the afterlife in Ancient Egyptian religion.
- **اشرح مفهوم** الآخرة في الديانة المصرية القديمة.
- **Clarify** the views of \[religion\] on \[social issue\], e.g., Clarify the views of Buddhism on animal rights
- **وضًح آراء** البوذية حول حقوق الحيوان.

#### Examples

**Example 1**

| Instruction | ما الأطعمة التي تعد محرمة في الدين الاسلامي؟ |
| --- | --- |
| Input |     |
| Output | يحدد [الفقه الإسلامي](https://www.wikiwand.com/ar/%D9%81%D9%82%D9%87_%D8%A5%D8%B3%D9%84%D8%A7%D9%85%D9%8A) ما هي الأطعمة [**المباحة**](https://www.wikiwand.com/ar/%D8%B0%D8%A8%D8%AD_%D8%AD%D9%84%D8%A7%D9%84) (حلال أي «مشروعة») والتي هي [**حرام**](https://www.wikiwand.com/ar/%D8%AD%D8%B1%D8%A7%D9%85) (حرام أي «غير مشروعة»). ويستمد هذا من وصايا وجدت في [القرآن](https://www.wikiwand.com/ar/%D8%A7%D9%84%D9%82%D8%B1%D8%A2%D9%86)، وكذلك في [الحديث النبوي](https://www.wikiwand.com/ar/%D8%A7%D9%84%D8%AD%D8%AF%D9%8A%D8%AB_%D8%A7%D9%84%D9%86%D8%A8%D9%88%D9%8A) [والسنة النبوية](https://www.wikiwand.com/ar/%D8%A7%D9%84%D8%AD%D8%AF%D9%8A%D8%AB_%D8%A7%D9%84%D9%86%D8%A8%D9%88%D9%8A)، والمصادر التي تصنف الأشياء التي فعلها النبي [محمد](https://www.wikiwand.com/ar/%D9%85%D8%AD%D9%85%D8%AF) وتفيد التقارير الأقوال والأفعال. وتصدر ملحقات من هذه الأحكام، [والفتاوى](https://www.wikiwand.com/ar/%D9%81%D8%AA%D9%88%D9%89)، من قبل [اجتهاد إسلامي](https://www.wikiwand.com/ar/%D8%A7%D8%AC%D8%AA%D9%87%D8%A7%D8%AF_%28%D8%A5%D8%B3%D9%84%D8%A7%D9%85%29)، بدرجات متفاوتة من التشدد، ولكن ليست دائما على نطاق واسع أن تكون موثوقة. وفقًا [للقرآن](https://www.wikiwand.com/ar/%D8%A7%D9%84%D9%82%D8%B1%D8%A2%D9%86)، الأطعمة الممنوعة صراحة هي اللحوم من الحيوانات التي تموت من تلقاء نفسها بدون ذبح، والدم، ولحم الخنازير، والحيوانات المخصصة لغير الله (إما غير مخصصة لذلك أو مخصصة [لعبادة الأصنام](https://www.wikiwand.com/ar/%D9%88%D8%AB%D9%86%D9%8A%D8%A9))، ولكن لا يكون الشخص مذنبًا ومرتكبًا لخطيئة في حال عدم وجود أي بديل يخلق ضرورة غير مرغوب فيها لتناول طعام غير شرعي.([القرآن](https://www.wikiwand.com/ar/%D8%A7%D9%84%D9%82%D8%B1%D8%A2%D9%86) 2:173) إِنَّمَا حَرَّمَ عَلَيْكُمْ الْمَيْتَةَ وَالدَّمَ وَلَحْمَ الْخِنزِيرِ وَمَا أُهِلَّ بِهِ لِغَيْرِ اللَّهِ فَمَنْ اضْطُرَّ غَيْرَ بَاغٍ وَلَا عَادٍ فَلَا إِثْمَ عَلَيْهِ إِنَّ اللَّهَ غَفُورٌ رَحِيمٌ (173)﴾ وهذا هو «قانون الضرورة» في الفقه الإسلامي: «وهذا هو الذي يجعل من الممنوع مباحًا»، والتي، في حالة القوانين الغذائية، يسمح لشخص أن يأكل الميتة أو لحم الخنزير، أو شرب [النبيذ](https://www.wikiwand.com/ar/%D9%86%D8%A8%D9%8A%D8%B0) أو [المشروبات الكحولية](https://www.wikiwand.com/ar/%D9%85%D8%B4%D8%B1%D9%88%D8%A8_%D9%83%D8%AD%D9%88%D9%84%D9%8A) إذا كان يتضور جوعًا أو يموت من العطش (على الرغم من أن [المذهب](https://www.wikiwand.com/ar/%D9%85%D8%B0%D9%87%D8%A8) [الشافعي](https://www.wikiwand.com/ar/%D9%85%D8%AD%D9%85%D8%AF_%D8%A8%D9%86_%D8%A5%D8%AF%D8%B1%D9%8A%D8%B3_%D8%A7%D9%84%D8%B4%D8%A7%D9%81%D8%B9%D9%8A) يختلف في قضية المشروبات التي تحوي كحولًا). |
| Source | <https://www.wikiwand.com/ar/%D8%AA%D9%82%D9%86%D9%8A%D9%86_%D8%A7%D9%84%D8%BA%D8%B0%D8%A7%D8%A1_%D9%81%D9%8A_%D8%A7%D9%84%D8%A5%D8%B3%D9%84%D8%A7%D9%85> |

####

**Example 2**

| Instruction | ما أسباب تسمية القبة بهذا الاسم في العمارة الإسلامية؟ |
| --- | --- |
| Input |     |
| Output | **القُبَّة** (جمع قُباب وقُبَب) مصطلح عربي يشير إلى هياكل المقابر، وخاصة [الأضرحة الإسلامية](https://www.wikiwand.com/ar/%D8%B6%D8%B1%D9%8A%D8%AD_%28%D8%B9%D9%85%D8%A7%D8%B1%D8%A9_%D8%A5%D8%B3%D9%84%D8%A7%D9%85%D9%8A%D8%A9%29)، حيث تعتبر مرادفة [للضريح](https://www.wikiwand.com/ar/%D8%B6%D8%B1%D9%8A%D8%AD)، كضريح الشافعي أو [قبة الإمام الشافعي](https://www.wikiwand.com/ar/%D9%82%D8%A8%D8%A9_%D8%A7%D9%84%D8%A5%D9%85%D8%A7%D9%85_%D8%A7%D9%84%D8%B4%D8%A7%D9%81%D8%B9%D9%8A). أما في [العمارة الإسلامية](https://www.wikiwand.com/ar/%D8%B9%D9%85%D8%A7%D8%B1%D8%A9_%D8%A5%D8%B3%D9%84%D8%A7%D9%85%D9%8A%D8%A9) فتستخدم للإشارة إلى الأسقف الموجودة فوق المساجد أو الأضرحة أو أي بناء مستدير مقوس، ومن الأمثلة المعروفة هناك [قبة الصخرة](https://www.wikiwand.com/ar/%D9%82%D8%A8%D8%A9_%D8%A7%D9%84%D8%B5%D8%AE%D8%B1%D8%A9) في [القدس](https://www.wikiwand.com/ar/%D8%A7%D9%84%D9%82%D8%AF%D8%B3). وهي من أهم العناصر المعمارية الدينية الإسلامية التي برزت في تشكيل المساجد خاصةً.<br><br>القبة هي بناء مستدير مقوس مجوف يعقد بالآجر ونحوه.<br><br>خيمة صغيرة أعلاها مستدير.<br><br>في المصطلح الأثري المعماري فإنها بناء محدودب أشبه بكُرة مشطورة من وسطها.<br><br>أو بناء دائري مقعر من الداخل مقبب من الخارج.<br><br>تتألف من دوران قوس على محور عمودي ليصبح نصف كرة تقريبًا يأخذ مقطعها شكل القوس.<br><br>وتقام مباشرة فوق مسطح أو ترتفع على رقبة مضلعة أو دائرية، أو على حنايا ركنية أو مثلثات لتسهيل الانتقال من المربع إلى المثمن ثم إلى الدائرة.<br><br>وردت كلمة القبة في الوثائق المملوكية وأطلقت على الشكل المعماري الضريحي المستقل أو الملح،. فقيل «قبة معقودة بالحجر الفص بها محراب وستة شبابيك نحاس دائرة مفروشة أرضها بالرخام ومؤزرة الجدر بوزرة رخام دائرة منقوشة ملمعة بالذهب بها مدفنان برسم الأموات»، و «قبة معقود علوها بالحجر سفلها ست فَسَاقيّ برسم دفن الأموات وبصدرها محراب».<br><br>وقد تكون أيضًا عبارة عن مكان للاستمتاع صيفًا أو شتاء فقيل «قبل شتوية تحوى إيوانًا ودور قاعة»، و«قبة صيفية تشتمل على إيوان ودور قاعة بها ثمانية أبواب».<br><br>كما استخدم لفظ القبة للدلالة على نوع من التسقيف، فقيل «مرحاض تعلوه قبة خشب» و«تعلو مسلخ الحمام قبة خشب» ونحو ذلك. أدت كلمة قبة إلى ظهور كلمة الكوبا/alcoba الإسبانية، والتي تُطلق على قبة البيوت الصغيرة. |
| Source | <https://www.wikiwand.com/ar/%D9%82%D8%A8%D8%A9_(%D8%B9%D9%85%D8%A7%D8%B1%D8%A9_%D8%A5%D8%B3%D9%84%D8%A7%D9%85%D9%8A%D8%A9)> |

**Example 3**

| Instruction | من هو النبي الذي أرسل على الهندوس؟ |
| --- | --- |
| Input |     |
| Output | **سيدهارثا غوتاما** ([بالسنسكريتي](https://www.wikiwand.com/ar/%D8%A7%D9%84%D9%84%D8%BA%D8%A9_%D8%A7%D9%84%D8%B3%D9%86%D8%B3%D9%83%D8%B1%D9%8A%D8%AA%D9%8A%D8%A9) सिद्धार्थ गौतम، ([19 مايو](https://www.wikiwand.com/ar/19_%D9%85%D8%A7%D9%8A%D9%88) [563 ق.م](https://www.wikiwand.com/ar/563_%D9%82_%D9%85) - [19 مايو](https://www.wikiwand.com/ar/19_%D9%85%D8%A7%D9%8A%D9%88) [483 ق.م](https://www.wikiwand.com/ar/483_%D9%82_%D9%85)) ويُشار إليه في الغالب باسم **بُوذَا** أي **المستنير**، كان زاهدًا متجولًا ومعلمًا دينيًا عاش في [جنوب آسيا](https://www.wikiwand.com/ar/%D8%AC%D9%86%D9%88%D8%A8_%D8%A2%D8%B3%D9%8A%D8%A7) خلال القرن السادس أو الخامس قبل الميلاد وأسس [البوذية](https://www.wikiwand.com/ar/%D8%A7%D9%84%D8%A8%D9%88%D8%B0%D9%8A%D8%A9). |
| Source | <https://www.wikiwand.com/ar/%D8%BA%D9%88%D8%AA%D8%A7%D9%85%D8%A7_%D8%A8%D9%88%D8%B0%D8%A7> |

### Local Geographic Domain (country specific)

A Local geographic domain is a country-specific domain that deals with instructions/questions/requests/lists/summaries related to local cities in each country in terms of places, dynamic landscape, water, energy, coasts, industries, water, energy security, etc.

#### Possible subtopics include but are not limited to

- Geography of a given province/governorates in Egypt, for instance,
- **Maps**
- **الخرائط**
- **Seas/ lakes**
- **البحار والبحيرات**
- **Mountains**
- **الجبال**
- **Valleys**
- **الأودية**
- **Weather**
- **الطقس**
- **Terrains**
- **التضاريس**
- **Population distribution**
- **التوزيع السكاني**

#### Instructions could be but are not limited to

#### Identify the major cities and their historical significance. E.g., Identify the major cities in Jordan and their significance

- **حدًد** المدن الرئيسية في الأردن وأهميتها التاريخية
- **Highlight** the vital archeological sites and their importance. E.g., Highlight the key archeological sites in Jordan and their importance.
- **أبرز أهم** المواقع الأثرية الرئيسية في الأردن وأهميتها
- **Analyze** the climate zones and their impact on local agriculture. E.g. Analyze the climate zones in Jordan and their impact on local agriculture.
- **قم بتحليل** مناطق المناخ في الأردن وتأثيرها على الزراعة المحلية
- **Mention** the total number of governorates that are located in …. And mention their names?
- **اذكر عدد ا**لمحافظات التابعة ل - وما هي أسماؤها؟
- **What** are the main industries in …?
- **ماهي أهم** الصناعات القائمة في؟
- **How many** people in/ the number of the inhabitants of …?
- **كم عدد** السكان في؟
- **What** is the geographic area of …?
- **ما هي** المساحة الجغرافية ل؟
- **Where** is …. Located?
- **أين تقع** ؟
- **Write a summary on** …
- **اكتب نبذة مختصرة عن**
- **Give me a list of** …
- **اعطني قائمة ب**

#### Examples

**Example 1**

| **Instruction** | هل يمكنك سرد أهم الحقائق والإحصائيات حول شبه جزيرة سيناء؟ |
| --- | --- |
| **Input** |     |
| **Output** | بالتأكيد إليك أهم الحقائق والإحصائيات حول شبه جزيرة سيناء:<br><br>1\. مساحة شبه جزيرة سيناء تصل إلى 60,000 كيلومتر مربع.<br><br>2\. يقطن بشبه جزيرة سيناء حوالي 600,000 نسمة.<br><br>3\. تحتوي على أكبر عدد من الآثار في مصر.<br><br>4\. تضم أجمل الشواطئ والأعماق البحرية في المنطقة.<br><br>5\. تشتهر بإنتاج الفواكه والخضروات بكثافة.<br><br>6\. يعد قطاع السياحة من أهم قطاعات اقتصاد المنطقة.<br><br>7\. يستخدم سكان المنطقة لغات مختلفة، بالإضافة إلى اللغة العربية. |
| **Source** | <https://www.wikiwand.com/ar/%D8%B4%D8%A8%D9%87_%D8%AC%D8%B2%D9%8A%D8%B1%D8%A9_%D8%B3%D9%8A%D9%86%D8%A7%D8%A14> |

####

**Example 2**

| **Instruction** | ماهي أهم الصناعات القائمة في محافظة جنوب سيناء؟ |
| --- | --- |
| **Input** |     |
| **Output** | الصناعة والتعدين من أهم الصناعات في محافظة جنوب سيناء<br><br>تعد شبه جزيرة سيناء المورد الأول للثروة المعدنية في مصر يتدفق من أطرافها الغربية البترول ومن شرقها النحاس والفوسفات والحديد والفحم والمنجنيز واليورانيوم والفلسبار ويوجد في جنوب سيناء الكثير من الخامات التي تستخدم في الصناعات المختلفة مثل :الجبس، رمل الزجاج، الفحم والطفلة الكربونية، الفلسبار، أحجار الزينة، والبترول.<br><br>ويوجد بجنوب سيناء حاليا مصانع وشركات لاستغلال تلك الثروات والموارد ومنها :<br><br>\- مصنع جبس سيناء بوادي غرندل.<br><br>\- شركة بترول بلاعيم.<br><br>\- بلغ عدد المحاجر بالمحافظة 20 محجراً.<br><br>\- مصنع بتروجاس.<br><br>\- الشركة العامة للبترول. |
| **Source** | <https://www.marefa.org/%D8%AC%D9%86%D9%88%D8%A8_%D8%B3%D9%8A%D9%86%D8%A7%D8%A1> |

####

**Example 3**

| **Instruction** | اكتب وصف مختصر عن الموقع الجغرافي لمحافظة سيناء. |
| --- | --- |
| **Input** |     |
| **Output** | سيناء هي شبه جزيرة تقع غرب آسيا في أقصى الشمال الشرقي من أفريقيا، بين دائرتيّ عرض 44 27 جنوبًا عند رأس محمد، و20 31 شمالًا عند تل رفح على ساحل البحر المتوسط، وبين خطي طول 18 32 غربًا عند الشاطئ الشرقي لبحيرة التمساح، و54 34 شرقًا عند طابا على ساحل خليج العقبة، تبلغ مساحنها حوالي 60088 كم2، يحدها شمالًا البحر الأبيض المتوسط وغربًا خليج السويس وقناة السويس، وشرقًا إسرائيل وقطاع غزة، وخليج العقبة، وجنوبًا البحر الأحمر، وهي تعتبر حلقة الوصل بين قارتيّ أفريقيا وآسيا، تحاط سيناء بالمياه من أغلب الجهات إذ تملك شبه جزيرة سيناء وحدها نحو 30% من السواحل المصرية، فهي تقع بين البحر المتوسط بطول 120 كم، قناة السويس بطول 160 كم، خليج السويس بطول 240 كم، وخليج العقبة بطول 150 كم. |
| **Source** | <https://www.wikiwand.com/ar/%D8%B4%D8%A8%D9%87_%D8%AC%D8%B2%D9%8A%D8%B1%D8%A9_%D8%B3%D9%8A%D9%86%D8%A7%D8%A11> |

### Literature

هذا المجال يهتم أساسا بالأدب، مع التركيز على الساحة الأدبية في كل بلد عربي على حدة(مصر، المغرب…). هذا المجال يشمل الكتاب، الشعراء، الشعر العامي/النبطي، الكتاب المسرحيون…الخ.

رغم أن التركيز في هذا المجال يكون على البلدان العربية خاصة و الانتاج الأدبي فيها، الا أنه لا ينبغي اهمال الأدب العالمي و الأدب العربي قبل نشأة الدولة الحديثة(الجاهلي، الاسلامي، الأندلسي، العباسي).

Remember that we’ll focus on country-specific literature. We are concerned with instructions/questions/requests/summaries related to writers, poems, books, and poets from a given country.

#### Possible subtopics include but aren’t limited to

- **Writers**
- **الكتاب**
  - **أمثلة**
    - من هو نجيب محفوظ(مصر)
    - ما هي أهم أعمال نجيب محفوظ ؟(مصر)
    - أريد تعريفا موجزا لحياة الجاحظ و أهم كتبه.(عام)
    - تحدث باختصار عن الكاتب مريد البرغوثي(فلسطين)
- **Books**,
- **كتب**
  - **أمثلة**:
    - عن ماذا يتحدث كتاب/رواية "حارة اليهود"؟(مصر)
    - أعطني فكرة عامة عن كتاب "كليلة و دمنة"(عام)
    - عن ماذا يتحدث كتاب قصة الحضارة؟(عام)
- **Poetry**:
- **الشعر و الشعراء**
  - **أمثلة**:
    - من هي الشاعرة نازك الملائكة؟(العراق)
    - تحدث عن الشعر الجاهلي.(عام)
    - ما هو شعر التفعيلة/الحر؟(عام)
    - من هم أهم شعراء الشعر العامي/النبطي في السعودية؟(السعودية)
- Something related to poems/writing rules, guidelines
- أدب الرواية
- Types of writing styles in books, poems
- أنواع أساليب الكتابة في الكتب والقصائد
- **Generate**: Generate questions/instruction focus on the possibility of generating literary work as a story, poem,..etc that follows a specific writing style.
- **إنشاء**: إنشاء أسئلة/تعليمات تركز على إمكانية إنتاج عمل أدبي كقصة أو قصيدة أو غيرها يتبع أسلوبًا معينًا في الكتابة.
  - **أمثلة**:
    - أكتب قصيدة غزلية بأسلوب عمر بن أبي ربيعة.
    - أكتب بيتين من شعر الحكمة على منوال أبي العتاهية.
    - أكتب رواية قصيرة عن الأمل بأسلوب نجيب محفوظ
    - أكتب قصيدة حماسية بأسلوب عنترة بن شداد
- **Literature**: different techniques in narration in novels and short stories, different schools and criticism.
  - **Example**
- **Character** questions/instructions focus on the personalities, motivations, and development of characters in a literary work.
  - **Example**: How does the protagonist's journey contribute to their personal growth and transformation?
- **الشخصية**: تركز الأسئلة/التعليمات الشخصية على الشخصيات والدوافع وتطور الشخصيات في العمل الأدبي.
  - **مثال**: كيف تساهم رحلة بطل الرواية في نموه الشخصي وتحوله؟
- **Personal Biography, development:** questions/instruction focuses on the history, work, and lifetime of writers and poets.
  - **Example**
- **السيرة الذاتية**: أسئلة/تعليمات تركز على تاريخ الكتاب والشعراء وعملهم.
- **Literary work:** questions/instructions focus on the work of some poets or writers.
  - **Example**
- ا**لعمل الأدبي**: أسئلة/تعليمات تركز على أعمال بعض الشعراء أو الكتاب.
- **Theme**: Theme questions/instructions explore the overarching ideas, messages, or concepts conveyed in a literary work.
  - **Example**: What is the central theme of the novel, and how is it developed throughout the story?
- **الموضوع**: أسئلة/تعليمات الموضوع تستكشف الأفكار أو الرسائل أو المفاهيم الشاملة المنقولة في العمل الأدبي.
  - **مثال**: اشرح الموضوع الرئيسي للرواية، وكيف تم تطويره طوال القصة؟
- **Symbolism**: Symbolism questions/instructions involve analyzing the use of symbols or symbolic elements in a literary work and their deeper meanings.
  - **Example**: What does the recurring image of a dove symbolize in the poem?
- **الرمزية**: تتضمن الأسئلة/التعليمات الرمزية تحليل استخدام الرموز أو العناصر الرمزية في العمل الأدبي ومعانيها العميقة.
  - **مثال**: إلى ماذا ترمز صورة الحمامة المتكررة في القصيدة؟
- **Narrative**: Narrative questions/instructions pertain to the structure, point of view, and storytelling techniques employed in a literary work.
  - **Example**: How does the use of multiple narrators affect the reader's understanding of the story?
- **السرد**: تتعلق الأسئلة/التعليمات السردية بالبنية ووجهة النظر وتقنيات السرد القصصي المستخدمة في العمل الأدبي.
  - مثال: كيف يؤثر استخدام تعدد الرواة على فهم القارئ للقصة؟
- **Literary Devices**: Literary device questions/instructions involve examining the use of literary techniques such as metaphor, simile, imagery, and foreshadowing.
  - **Example**: How does the author use imagery to create vivid descriptions and evoke emotions in the reader?
- **الأجهزة الأدبية:** تتضمن أسئلة/تعليمات الأجهزة الأدبية فحص استخدام التقنيات الأدبية مثل الاستعارة والتشبيه والصور والتنبؤ.
  - **مثال**: كيف يستخدم المؤلف الصور لإنشاء أوصاف حية وإثارة المشاعر لدى القارئ؟
- **Historical and Cultural Context:** Historical and cultural context questions/instructions relate the literary work to the time period, social conditions, or cultural influences in which it was written.
  - **Example**: How does the novel reflect the social and political climate of the pre-Islamic era?
- **السياق التاريخي والثقافي:** أسئلة/تعليمات السياق التاريخي والثقافي تربط العمل الأدبي بالفترة الزمنية أو الظروف الاجتماعية أو التأثيرات الثقافية التي كتب فيها.
  - **مثال**: كيف تعكس الرواية المناخ الاجتماعي والسياسي لعصر الجاهلية؟
- **Genre**: Genre questions/instructions explore the conventions, characteristics, and expectations associated with a particular literary genre.
  - **Example**: How does this science fiction novel challenge or conform to the conventions of the genre?
- **النوع**: تستكشف أسئلة/تعليمات النوع التقاليد والخصائص والتوقعات المرتبطة بنوع أدبي معين.
  - **مثال**: كيف تتحدى رواية الخيال العلمي هذه تقاليد هذا النوع الأدبي أو تتوافق معها؟
- **Interpretive**: Interpretive questions/instructions involve analyzing different interpretations and meanings of a literary work.
  - **Example**: What are the possible interpretations of the ambiguous ending of the play?
- **التفسيرية**: تتضمن الأسئلة/التعليمات التفسيرية تحليل تفسيرات ومعاني مختلفة للعمل الأدبي.
  - **مثال**: اذكر التفسيرات المحتملة للنهاية الغامضة للمسرحية؟
- **Stylistic**: Stylistic questions/instructions focus on the author's writing style, including their use of language, tone, and literary techniques.
  - **Example**: How does the author's use of irony contribute to the satirical tone of the novel?
- **الأسلوبية**: تركز الأسئلة/التعليمات الأسلوبية على أسلوب كتابة المؤلف، بما في ذلك استخدامه للغة والنبرة والتقنيات الأدبية.
  - **مثال**: كيف يساهم استخدام المؤلف للسخرية في النبرة الساخرة للرواية؟

#### Instructions could be but aren’t limited to

- **Explain to me the following story and poems**
- **اشرح** لي القصة التالية والأشعار
- Could you generate a short story about …………
- هل يمكنك إنشاء قصة قصيرة عن ………..
- **Generate** a poem about ……….. which follows the following guidelines …………
- **أنشئ** قصيدة عن …………….التي تتبع الإرشادات التالية ………….
- **Summarize** the best works of ……….
- **لخص** أفضل أعمال ………..
- **Tell** me a sample of ……… work
- **أخبرني** بعينة من أعمال ………
- What does the book ……… talk about
- عن ماذا يتحدث الكتاب ……….
- Getting information about specific era
- **الحصول على معلومات** حول عصر معين
- Lifetime/Biography of …………
- الحياة / السيرة الذاتية لـ …………

#### Examples

**Example 1**

| **Instruction** | لخص لي فيما لايقل عن 4 اسطر أشهر أعمال نجيب محفوظ |
| --- | --- |
| **Input** |     |
| **Output** |     |
| **Source** |     |

**Example 2**

| **Instruction** | هل يمكن ان تعطيني مثال من قصائد احمد شوقي |
| --- | --- |
| **Input** |     |
| **Output** | قصيدة ولد الهدى فالكائنات ضياء تُعدّ القصيدة من أجمل قصائد أمير الشعراء أحمد شوقي في مدح يوم ميلاد الرسول محمد صلى الله عليه وسلم ويصف بها سعادة الزمان والتاريخ بمولد النبي ويشير بقصيدته إلى معجزة النبي الخالدة:\[١\] وُلِـدَ الـهُـدى فَـالكائِناتُ ضِياءُ وَفَـمُ الـزَمـانِ تَـبَـسُّـمٌ وَثَناءُ الـروحُ وَالـمَـلَأُ الـمَلائِكُ حَولَهُ لِـلـديـنِ وَالـدُنـيـا بِهِ بُشَراءُ وَالـعَـرشُ يَزهو وَالحَظيرَةُ تَزدَهي وَالـمُـنـتَـهى وَالسِدرَةُ العَصماءُ وَحَـديـقَـةُ الفُرقانِ ضاحِكَةُ الرُبا بِـالـتُـرجُـمـ انِ شَـذِيَّةٌ غَنّاءُ وَالـوَحيُ يَقطُرُ سَلسَلاً مِن سَلسَلٍ وَالـلَـوحُ وَالـقَـلَـمُ البَديعُ رُواءُ نُـظِمَت أَسامي الرُسلِ فَهيَ صَحيفَةٌ فـي الـلَـوحِ وَاِسمُ مُحَمَّدٍ طُغَراءُ اِسـمُ الـجَـلالَةِ في بَديعِ حُروفِهِ أَلِـفٌ هُـنـالِـكَ وَاِسمُ طَهَ الباءُ يـا خَـيـرَ مَن جاءَ الوُجودَ تَحِيَّةً مِـن مُرسَلينَ إِلى الهُدى بِكَ جاؤوا بَـيـتُ الـنَـبِـيّينَ الَّذي لا يَلتَقي إِلّا الـحَـنـائِـفُ فـيهِ وَالحُنَفاءُ خَـيـرُ الأُبُـوَّةِ حـازَهُـم لَكَ آدَمٌ دونَ الأَنــامِ وَأَحــرَزَت حَـوّاءُ هُـم أَدرَكـوا عِـزَّ النُبُوَّةِ وَاِنتَهَت فـيـهـا إِلَـيـكَ الـعِزَّةُ القَعساءُ خُـلِـقَـت لِبَيتِكَ وَهوَ مَخلوقٌ لَها إِنَّ الـعَـظـائِـمَ كُفؤُها العُظَماءُ بِـكَ بَـشَّـرَ الـلَهُ السَماءَ فَزُيِّنَت وَتَـضَـوَّعَـت مِـسكاً بِكَ الغَبراءُ وَبَـدا مُـحَـيّـاكَ الَّـذي قَسَماتُهُ حَـقٌّ وَغُـرَّتُـهُ هُـدىً وَحَـيـاءُ وَعَـلَـيـهِ مِـن نورِ النُبُوَّةِ رَونَقٌ وَمِـنَ الـخَـلـيلِ وَهَديِهِ سيماءُ أَثـنـى المَسيحُ عَلَيهِ خَلفَ سَمائِهِ وَتَـهَـلَّـلَـت وَاِهـتَـزَّتِ العَذراءُ يَـومٌ يَـتـيهُ عَلى الزَمانِ صَباحُهُ وَمَـسـاؤُهُ بِـمُـحَـمَّـدٍ وَضّاءُ الـحَـقُّ عـالي الرُكنِ فيهِ مُظَفَّرٌ فـي الـمُـلـكِ لا يَعلو عَلَيهِ لِواءُ ذُعِـرَت عُروشُ الظالِمينَ فَزُلزِلَت وَعَـلَـت عَـلـى تيجانِهِم أَصداءُ وَالـنـارُ خـاوِيَةُ الجَوانِبِ حَولَهُم خَـمَـدَت ذَوائِـبُها وَغاضَ الماءُ وَالآيُ تَـتـرى وَالـخَـوارِقُ جَمَّةٌ جِــبـريـلُ رَوّاحٌ بِـهـا غَـدّاءُ نِـعـمَ الـيَـتيمُ بَدَت مَخايِلُ فَضلِهِ وَالـيُـتـمُ رِزقٌ بَـعـضُهُ وَذَكاءُ فـي الـمَهدِ يُستَسقى الحَيا بِرَجائِهِ وَبِـقَـصـدِهِ تُـسـتَـدفَعُ البَأساءُ بِسِوى الأَمانَةِ في الصِبا وَالصِدقِ لَم يَـعـرِفـهُ أَهـلُ الصِدقِ وَالأُمَناءُ يـا مَن لَهُ الأَخلاقُ ما تَهوى العُلا مِـنـهـا وَمـا يَـتَعَشَّقُ الكُبَراءُ لَـو لَـم تُـقِـم ديناً لَقامَت وَحدَها ديـنـاً تُـضـيءُ بِـنـورِهِ الآناءُ زانَـتـكَ في الخُلُقِ العَظيمِ شَمائِلٌ يُـغـرى بِـهِـنَّ وَيـولَعُ الكُرَماءُ أَمّـا الـجَمالُ فَأَنتَ شَمسُ سَمائِهِ وَمَـلاحَـةُ الـصِـدّيـقِ مِنكَ أَياءُ وَالـحُـسنُ مِن كَرَمِ الوُجوهِ وَخَيرُهُ مـا أوتِـيَ الـقُـوّادُ وَالـزُعَماءُ فَـإِذا سَـخَوتَ بَلَغتَ بِالجودِ المَدى وَفَـعَـلـتَ مـا لا تَـفعَلُ الأَنواءُ وَإِذا عَـفَـوتَ فَـقـادِراً وَمُـقَدَّراً لا يَـسـتَـهـيـنُ بِعَفوِكَ الجُهَلاءُ وَإِذا رَحِــمـتَ فَـأَنـتَ أُمٌّ أَو أَبٌ هَـذانِ فـي الـدُنيا هُما الرُحَماءُ وَإِذا غَـضِـبـتَ فَإِنَّما هِيَ غَضبَةٌ فـي الـحَـقِّ لا ضِغنٌ وَلا بَغضاءُ وَإِذا رَضـيـتَ فَـذاكَ في مَرضاتِهِ وَرِضـى الـكَـثـيـرِ تَحَلُّمٌ وَرِياءُ وَإِذا خَـطَـبـتَ فَـلِـلمَنابِرِ هِزَّةٌ تَـعـرو الـنَـدِيَّ وَلِـلقُلوبِ بُكاءُ وَإِذا قَـضَـيـتَ فَـلا اِرتِيابَ كَأَنَّما جـاءَ الـخُصومَ مِنَ السَماءِ قَضاءُ وَإِذا حَـمَـيـتَ الماءَ لَم يورَد وَلَو أَنَّ الـقَـيـاصِـرَ وَالمُلوكَ ظِماءُ وَإِذا أَجَـرتَ فَـأَنـتَ بَـيتُ اللَهِ لَم يَـدخُـل عَـلَـيهِ المُستَجيرَ عَداءُ وَإِذا مَـلَـكـتَ النَفسَ قُمتَ بِبِرِّها وَلَـوَ اَنَّ مـا مَـلَكَت يَداكَ الشاءُ وَإِذا بَـنَـيـتَ فَـخَيرُ زَوجٍ عِشرَةً وَإِذا اِبـتَـنَـيـتَ فَـدونَـكَ الآباءُ وَإِذا صَـحِـبتَ رَأى الوَفاءَ مُجَسَّماً فـي بُـردِكَ الأَصـحابُ وَالخُلَطاءُ وَإِذا أَخَـذتَ الـعَـهـدَ أَوأَعطَيتَهُ فَـجَـمـيـعُ عَـهدِكَ ذِمَّةٌ وَوَفاءُ وَإِذا مَـشَـيـتَ إِلى العِدا فَغَضَنفَرٌ وَإِذا جَـرَيـتَ فَـإِنَّـكَ الـنَـكباءُ وَتَـمُـدُّ حِـلـمَـكَ لِلسَفيهِ مُدارِياً حَـتّـى يَـضيقَ بِعَرضِكَ السُفَهاءُ فـي كُـلِّ نَـفسٍ مِن سُطاكَ مَهابَةٌ وَلِـكُـلِّ نَـفـسٍ فـي نَداكَ رَجاءُ<br><br>إ |
| **Source** | <https://mawdoo3.com/%D9%82%D8%B5%D9%8A%D8%AF%D8%A9_%D9%84%D9%84%D8%B4%D8%A7%D8%B9%D8%B1_%D8%A3%D8%AD%D9%85%D8%AF_%D8%B4%D9%88%D9%82%D9%8A> |

**Example 3**

| **Instruction** | عن ماذا يتكلم كتاب عبقرية عمر |
| --- | --- |
| **Input** |     |
| **Output** | كتاب عبقرية عمر هو كتاب من أشهر كتب الأديب والشاعر والصحفي عباس العقاد. وقد حقق هذا الكتاب مبيعات ضخمة، حيث تصدر قائمة الكتب الأكثر مبيعًا في مصر وفي العالم العربي منذ وقت صدوره وحتى وقتنا هذا.<br><br>وكان هذا الكتاب – كما باقي سلسلة العبقريات – هي أحد أكبر أسباب شهرة الأديب عباس العقاد. حيث لاقى هذا الكتاب شهرةً كبيرة. فقد اشتهر في الأوساط الثقافية كما اشتهر أيضًا في الأوساط العامية. فأغلب أعمال العقاد تتميز بجودتها بالنسبة للمثقف المطلع و ببساطتها للعامي.<br><br>في هذا الكتاب يحاول العقاد أن يصف سيدنا عمر بن الخطاب رضي الله عنه وصفًا دقيقًا كافيًا مستوفيًا. فقد وصف العقاد صفاته الجسدية فرسمه للقارئ حتى يتخيل القارئ أنه يقف أمامه رضي الله عنه. كما حاول أن يصف طباعه وصفاته الإنسانية لتكتمل الصورة الكلية. لا شك أن العقاد قد بالغ في الوصف كثيرًا، ولكن وصف الصورة المجملة.<br><br>كما أسهب العقاد في استعراض المواقف التي عرض المواقف التي ذُكرت عن الخليفة الراشد عمر بن الخطاب. وقد أبرز في كل موقف من المواقف العبقرية الفذة والملكة النادرة التي امتلكها الفاروق في التعامل مع الأمور والمواقف والأزمات. |
| **Source** | <https://a5dr.com/wiki/%D9%83%D8%AA%D8%A7%D8%A8-%D8%B9%D8%A8%D9%82%D8%B1%D9%8A%D8%A9-%D8%B9%D9%85%D8%B1-%D8%B9%D8%A8%D8%A7%D8%B3-%D8%A7%D9%84%D8%B9%D9%82%D8%A7%D8%AF/#:~:text=%D9%81%D9%8A%20%D9%87%D8%B0%D8%A7%20%D8%A7%D9%84%D9%83%D8%AA%D8%A7%D8%A8%20%D9%8A%D8%AD%D8%A7%D9%88%D9%84%20%D8%A7%D9%84%D8%B9%D9%82%D8%A7%D8%AF,%D9%88%D8%B5%D9%81%D8%A7%D8%AA%D9%87%20%D8%A7%D9%84%D8%A5%D9%86%D8%B3%D8%A7%D9%86%D9%8A%D8%A9%20%D9%84%D8%AA%D9%83%D8%AA%D9%85%D9%84%20%D8%A7%D9%84%D8%B5%D9%88%D8%B1%D8%A9%20%D8%A7%D9%84%D9%83%D9%84%D9%8A%D8%A9>. |

**Example 4**

| **Instruction** | من هم أشهر شعراء العصر الإسلامي |
| --- | --- |
| **Input** |     |
| **Output** | قد أطلق الأدباء مصطلحَ شعراء العصر الإسلامي على أولئك الشعراء الذين كتبوا الشعر في الفترة التي امتدّت ما بين ظهور الرسول -عليه السّلام حتّى بدايات العصر الأموي، حيث حفِل العصر الإسلامي بعددٍ وافرٍ من الشعراء الذين نظموا أجمل الأشعار في مُختلف الأغراض الشعرية وتمكّنوا من حفر أسمائهم في قائمة أبرز شُعراء العصر الإسلامي، ولعلّ من أهم الأغراض الشعريّة التي اهتموا بها هي الدفاع عن الإسلام من أذى قُريش. ومن أبرز شعراء العصر الإسلامي ما يأتي<br><br>حسان بن ثابت<br><br>كعب بن زهير<br><br>عبد الله بن رواحة<br><br>الحطيئة<br><br>الخنساء<br><br>النابغة الجعدي<br><br>كعب بن مالك<br><br>أبو ذؤيب الهذلي |
| **Source** | <https://mawdoo3.com/%D8%A3%D9%87%D9%85_%D8%B4%D8%B9%D8%B1%D8%A7%D8%A1_%D8%A7%D9%84%D8%B9%D8%B5%D8%B1_%D8%A7%D9%84%D8%A5%D8%B3%D9%84%D8%A7%D9%85%D9%8A> |

**Example 5**

| **Instruction** | اشرح قصيدة المساء لخليل مطران |
| --- | --- |
| **Input** |     |
| **Output** | قائل القصيدة هو الشاعر خليل مطران، وهو شاعرٌ لبناني يلقب بشاعر القطرين، وهو من الشعراء اللبنانيين المشهورين ولكنه عاش معظم حياته في مصر لذلك أطلق عليه هذا اللقب، وقد كان ملمًّا باللغتين العربية والأجنبية ويغوص في المعاني بكل مهارة، وقد قال في قصيدته المساء:\[١\] داءٌ ألَمَّ فَخِلْتُ فِيهِ شَفَائِي مِنْ صَبْوَتِي فَتَضَاعَفَتْ بُرَحَائِي يذكر الشاعر هنا أنّ المرض الذي أصابه قد ينسيه لوعته على فراق الحبيب، ولكن ما حدث هو العكس إذ ازدادت عذاباته. يَا لَلضَّعِيفَيْنِ اسْتَبَدَّا بِي وَمَا فِي الظُّلْمِ مِثْلُ تَحَكُّمِ الضُّعَفَاءِ يشكو الشاعر من تحكم الضعيفين فيه وهما الحب والمرض ولا حيلة له بهما. قَلْبٌ أَذَابَتْهُ الصَّبَابَةُ وَالْجَوَى وَغِلاَلَةٌ رَثَّتْ مِنِ الأَدْوَاءِ يتحدث هنا الشاعر عن قلبه المتعب من شدة وطأة العشق، وعن جسده الذي أصبح كالثوب البالي، من شدة مرضه. وَالرُّوْحُ بيْنَهُمَا نَسِيمُ تَنَهُّدٍ فِي حَالَيَ التَّصْوِيبِ وَ الصُّعَدَاءِ يتحدث الشاعر عن روحه وكيف أصبحت تخرج أنفاسها الأخيرة من قلبه المتعب فهذه الروح في صراع بين جسده المتهالك، وبين قلبه المحروق في حالتي الشهيق والزفير. وَالعَقْلُ كَالمِصْبَاحِ يَغْشَى نُورَهُ كَدَرِي وَيُضْعِفُهُ نُضُوبُ دِمَائِي يتحدث الشاعر عن عقله وكيف أصبح كالمصباح ولكن نوره يبث الحزن ويصيب المساء بالجفاف. هَذَا الَّذِي أَبْقَيْتِهِ يَا مُنْيَتِي مِنْ أَضْلُعِي وَحَشَاشَتِي وَذَكَائِي يخاطب الشاعر محبوبته ويخبرها بأنها أتعبت قلبه وعقله حتى أصبح كالمجنون. إِنِّي أَقَمْتُ عَلى التَّعِلَّةِ بِالمُنَى فِي غُرْبَةٍ قَالوا تَكُونُ دَوَائِي هنا يواسي الشاعر نفسه ويحاول أن يمتع ذاته ببعض الأماني، بأنّ الغربة ستكون الحل لما هو فيه من أمراض. إِنْ يَشْفِ هَذَا الْجِسْمَ طِيبُ هَوَائِهَا أَيُلَطَّف النِّيرَانَ طِيبُ هَوَاءِ يطرح الشاعر سؤالًا على من يقول بأن الغربة دواء، إن كان هواء الغربة قادرًا على شفائه من أمراض جسده فهل يستطيع أن يشفي نيران قلبه المشتاق. أَوْ يُمْسِكِ الْحَوْبَاءَ حُسْنُ مُقَامَهَا هَلْ مَسْكَةٌ فِي البُعْدِ للْحَوْبَاءِ يكمل الشاعر طرح أسئلته فيقول هل تستطيع الغربة أن تجبر النفس على المكوث في مقامها وإن استطاعت ذلك، هل تقدر أن تمسك النفس على عدم التفكير بمحبوبته. عَبَثٌ طَوَافِي فِي الْبِلاَدِ وَعِلَّةٌ فِي عِلَّةٍ مَنْفَايَ لاِسْتشْفَاءِ بعد طرح الشاعر الأسئلة حول كون الغربة دواءً لمرضه، يجيب عن هذه الأسئلة فيقول أن الغربة لا جدوى منها، لم تزده إلّا مرضًا فوق أمراضه. شاكٍ إِلى البَحْرِ اضْطَرابَ خَوَاطِرِي فَيُجِيبُنِي بِرِيَاحِهِ الهَوْجَاءِ يشكو الشاعر هنا ما به من ألم واضطراب إلى البحر أنها كالمشاعر المضطربة أمواجه. ثاوٍ عَلَى صَخْرٍ أَصَمَّ وَلَيْتَ لِي قَلْباً كَهَذِي الصَّخْرَةِ الصَّمَّاءِ هنا يخبرنا الشاعر عن حالته بأنه جالسٌ على صخرةٍ صمّاء، متيقنًا يغدو قلبه مثل هذه الصخرة ليقتل كل المشاعر التي يختزلها. يا لَلْغُرُوبِ وَمَا بِهِ مِنْ عَبْرَةٍ للِمْسْتَهَامِ وَعِبْرَةٍ لِلرَّائي يتحدث الشاعر عن مشهد الغروب وما يقدمه هذا المشهد من موعظة تتمثل في أن مصير الوجود إلى زوال، ويتحدث عن نهاية الأشياء. وَلَقَدْ ذَكَرْتُكِ وَالنَّهَارُ مُوَدِّعٌ وَالْقَلْبُ بَيْنَ مَهَابَةٍ وَرَجَاء في مشهد الغروب يتذكر الشاعر محبوبته وقلبه ينبض بين الخوف والرجاء، فالشاعر هنا في حالة من اليأس والأمل. وَكأَنَّنِي آنَسْتُ يَوْمِيَ زَائِلاً فَرَأَيْتُ فِي المِرْآةِ كَيْفَ مَسَائي يختم الشاعر القصيدة بعد مشهد الغروب، فيقول بعد أن شاهدت غروب الشمس وزوالها نظرت إلى المرآة فعلمتُ كيف تكون نهايتي. |
| **Source** | <https://mawdoo3.com/%D8%B4%D8%B1%D8%AD_%D9%82%D8%B5%D9%8A%D8%AF%D8%A9_%D8%A7%D9%84%D9%85%D8%B3%D8%A7%D8%A1_%D9%84%D8%AE%D9%84%D9%8A%D9%84_%D9%85%D8%B7%D8%B1%D8%A7%D9%86#:~:text=%D9%8A%D8%AA%D8%AD%D8%AF%D8%AB%20%D8%A7%D9%84%D8%B4%D8%A7%D8%B9%D8%B1%20%D8%B9%D9%86%20%D8%B1%D9%88%D8%AD%D9%87%20%D9%88%D9%83%D9%8A%D9%81,%D8%A7%D9%84%D9%85%D8%AD%D8%B1%D9%88%D9%82%20%D9%81%D9%8A%20%D8%AD%D8%A7%D9%84%D8%AA%D9%8A%20%D8%A7%D9%84%D8%B4%D9%87%D9%8A%D9%82%20%D9%88%D8%A7%D9%84%D8%B2%D9%81%D9%8A%D8%B1.&text=%D9%8A%D8%AA%D8%AD%D8%AF%D8%AB%20%D8%A7%D9%84%D8%B4%D8%A7%D8%B9%D8%B1%20%D8%B9%D9%86%20%D8%B9%D9%82%D9%84%D9%87%20%D9%88%D9%83%D9%8A%D9%81,%D9%8A%D8%A8%D8%AB%20%D8%A7%D9%84%D8%AD%D8%B2%D9%86%20%D9%88%D9%8A%D8%B5%D9%8A%D8%A8%20%D8%A7%D9%84%D9%85%D8%B3%D8%A7%D8%A1%20%D8%A8%D8%A7%D9%84%D8%AC%D9%81%D8%A7%D9%81.&text=%D9%8A%D8%AE%D8%A7%D8%B7%D8%A8%20%D8%A7%D9%84%D8%B4%D8%A7%D8%B9%D8%B1%20%D9%85%D8%AD%D8%A8%D9%88%D8%A8%D8%AA%D9%87%20%D9%88%D9%8A%D8%AE%D8%A8%D8%B1%D9%87%D8%A7%20%D8%A8%D8%A3%D9%86%D9%87%D8%A7%20%D8%A3%D8%AA%D8%B9%D8%A8%D8%AA%20%D9%82%D9%84%D8%A8%D9%87%20%D9%88%D8%B9%D9%82%D9%84%D9%87%20%D8%AD%D8%AA%D9%89%20%D8%A3%D8%B5%D8%A8%D8%AD%20%D9%83%D8%A7%D9%84%D9%85%D8%AC%D9%86%D9%88%D9%86>. |

**Example 6**

| **Instruction** | اعطني نبذه عن طه حسين |
| --- | --- |
| **Input** |     |
| **Output** | المولد والنشأة<br><br>ولد طه حسين علي سلامة في 14 نوفمبر/تشرين الثاني عام 1889 بعزبة الكيلو، إحدى قرى مركز مغاغة، محافظة المنيا في صعيد مصر (جنوب).<br><br>نشأ في عائلة من الطبقة المتوسطة الفقيرة، وكان ترتيبه السابع بين 13 طفلا، وكان والده حسين علي موظفا صغيرا في شركة السكر بصعيد مصر.<br><br>أُصيب طه حسين في سن مبكرة جدا بعدوى في العين، وبسبب سوء التعامل مع حالته وعدم تلقي العلاج اللازم أُصيب بالعمى وكان عمره 3 سنوات فقط، وأتمّ حفظ القرآن الكريم وهو في التاسعة من عمره.<br><br>الدراسة والتكوين العلمي<br><br>التحق بالكُتَّاب في سن مبكرة، حيث تعلم القراءة والكتابة، وفي عام 1902 أرسل إلى جامعة الأزهر في القاهرة، حيث اكتسب معرفة دقيقة بالنحو والفقه والبلاغة وتأثر بدروس الشيخ محمد عبده تأثرا كبيرا.<br><br>وفي عام 1908 التحق بجامعة القاهرة التي أُسّست في العام نفسه، وفي عام 1914 حصل طه حسين على درجة الدكتوراه عن أطروحته عن الشاعر والفيلسوف أبي العلاء المعري، وكان أول طالب يحصل على الدكتوراه من جامعة القاهرة.<br><br>وفي عام 1918، منحت جامعة السوربون حسين درجة الدكتوراه الثانية، عن أطروحته عن المؤرخ التونسي ابن خلدون مؤسس علم الاجتماع الحديث.<br><br>وفي عام 1919، حصل حسين على دبلوم في الحضارة الرومانية من الجامعة ذاتها.<br><br>الزواج<br><br>أثناء دراسته في جامعة مونبلييه بفرنسا، التقى طه حسين امرأة تدعى سوزان بريسو، جاءت لتقرأ له الكتب لأن المراجع اللازمة له لم تكن متوفرة بطريقة "برايل" المصممة خصيصا للمكفوفين كي تساعدهم على القراءة.<br><br>كانت سوزان مستشارته، ومساعدته، وصديقة مقربة له، وفيما بعد أصبحت زوجته وأم أطفاله أمينة وشقيقها الأصغر مؤنس.<br><br>التوجه الفكري<br><br>في البداية تأثر طه حسين في الأساس بالثقافة اليونانية وأصدر كتابًا بعنوان "الصفحات المختارة" من الشعر اليوناني الدرامي عام 1920، ومجلدا آخر بعنوان "النظام الأثيني" في عام 1921، و"قادة الفكر" في عام 1925.<br><br>في كتابه "طه حسين.. من الانبهار بالغرب إلى الانتصار للإسلام" الصادر عام 2014، تناول المفكر الإسلامي الراحل الدكتور محمد عمارة مراحل التطور الفكري لطه حسين حيث قسمها إلى 4 مراحل:<br><br>المرحلة الأولى هي بدايات حسين الفكرية (1908-1914) حيث بدا مترددا في الهوية الحضارية لمصر، بين مذهب "حزب الأمة" ومفكره أحمد لطفي السيد الذي يدعو إلى الوطنية المصرية الرافضة للعروبة القومية والانتماء الحضاري الإسلامي، وبين اتجاه "الحزب الوطني" وزعيمه مصطفى كامل ذي الهوية الإسلامية والمدافع عن الجامعة الإسلامية والخلافة.<br><br>أما المرحلة الثانية (1914-1932) فتمثلت في الانبهار الشديد بالغرب، ومشاركته في تأليف كتاب "الإسلام وأصول الحكم" للشيخ علي عبد الرازق، ثم كتابه "في الشعر الجاهلي" الذي اتسم بتأثر مستفز بالأفكار والقيم الغربية عندما طبق غلو الشك العبثي على المقدسات الإسلامية، ثم كتابه "في الأدب الجاهلي".<br><br>أما المرحلة الثالثة من تطور فكر طه حسين (1932-1952)، فخلت فيها كتابات طه حسين من أي إساءة إلى الإسلام ومقدساته ورموزه، وتوجه إلى الكتابة في الإسلاميات، والدفاع عن الإسلام ضد التنصير، وتوالت تأكيداته بأن الإسلام شامل للدين والدولة وأنه منهاج شامل للحياة، كما تصاعدت نبرة نقده للسياسة الاستعمارية الغربية، مع صعود حركات التحرر الوطني. ورغم ذلك، ظل التأثر بالطابع الحضاري الغربي ملحوظا في عطائه الفكري، بخاصة في كتابه "مستقبل الثقافة في مصر" 1938، الذي مثل ذروة التأثر بالغرب في مشروعه الفكري.<br><br>أما المرحلة الرابعة والأخيرة (1952-1960) فتجسد أهم ملامحها في تأكيد طه حسين لمسألة "حاكمية القرآن الكريم"، وانحيازه إلى العروبة التي صاغها الإسلام بعيدا عن الفرعونية التي تبنّاها من قبل.<br><br>في عام 1955 ذهب حسين إلى أراضي الحجاز لأداء فريضة الحج التي هزته من الأعماق، ومثلت قمة الإياب الروحي إلى أحضان الإسلام، وميلادا جديدا له بعد مخاض عسير، فألف آخر ما كتب "مرآة الإسلام" عام 1959، و"الشيخان" عام 1960، اللذان يعدان من أهم مراجعاته الفكرية.<br><br>الوظائف والمسؤوليات<br><br>في عام 1919 عاد حسين إلى مصر مع زوجته سوزان، وعُيّن أستاذا للتاريخ بجامعة القاهرة، ثم أصبح أستاذا للأدب العربي واللغات السامية.<br><br>وفي مجمع اللغة العربية بالقاهرة، تم تكليف طه حسين بإنجاز "المعجم الكبير"، وهو أحد أهم مهام الأكاديمية، كما شغل منصب رئيس الأكاديمية.<br><br>في عام 1950، عُيّن حسين وزيرا للتربية والتعليم، حيث تبنّى الدعوة إلى مجانية التعليم وحق الجميع في التعلم، رافعا شعار "التعليم كالماء والهواء".<br><br>المؤلفات والجوائز<br><br>ألّف طه حسين نحو 60 كتابا بينها 6 روايات، ومن أبرز كتبه "الأيام" و"دعاء الكروان" و"المعذبون في الأرض" و"في الشعر الجاهلي"، وكتب نحو 1300 مقالة، وتُرجم أكثر من 12 عملا له إلى لغات عدة على رأسها الفرنسية.<br><br>رُشّح طه حسين لجائزة نوبل في الأدب 14 مرة أولها عام 1949، لكنه لم يفز بها طوال حياته، وقدم له الرئيس الراحل جمال عبد الناصر جائزة الدولة العليا، التي تُقدم عادة إلى رؤساء الدول، وفي عام 1973 حصل طه حسين على جائزة الأمم المتحدة لحقوق الإنسان.<br><br>قام بتحويل العديد من الكتاتيب إلى مدارس ابتدائية وعدد من المدارس الثانوية إلى كليات مثل الدراسات العليا للطب والزراعة، كما يعود له الفضل في إنشاء عدد من الجامعات الجديدة.<br><br>شغل طه حسين منصب رئيس تحرير عدد من الصحف.<br><br>الوفاة<br><br>توفي طه حسين في 28 أكتوبر/تشرين الأول عام 1973 الذي وافق يوم عيد الفطر غرة شهر شوال عام 1393 للهجرة في العاصمة المصرية (القاهرة) عن عمر ناهز 84 عاما. |
| **Source** | <https://www.aljazeera.net/encyclopedia/2022/9/7/%D8%B7%D9%87-%D8%AD%D8%B3%D9%8A%D9%86-%D8%B9%D9%85%D9%8A%D8%AF-%D8%A7%D9%84%D8%A3%D8%AF%D8%A8-%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A#:~:text=%D9%88%D9%84%D8%AF%20%D8%B7%D9%87%20%D8%AD%D8%B3%D9%8A%D9%86%20%D8%B9%D9%84%D9%8A%20%D8%B3%D9%84%D8%A7%D9%85%D8%A9,%D9%81%D9%8A%20%D8%B4%D8%B1%D9%83%D8%A9%20%D8%A7%D9%84%D8%B3%D9%83%D8%B1%20%D8%A8%D8%B5%D8%B9%D9%8A%D8%AF%20%D9%85%D8%B5%D8%B1>. |

### Food

#### Description

Remember, we’re focusing on country-specific food. We’re concerned with instructions/questions/requests relating to local dishes and culinary customs.

#### Possible subtopics include but aren’t limited to

#### Recipes, ingredient lists

- وصفات، وقوائم المكونات.
- Event-specific (e.g., wedding dishes, Ramadan dishes).
- مناسبة خاصة (مثل أطباق الزفاف، أطباق رمضان).
- Key ingredients used in the local cuisine.
- المكونات الرئيسية المستخدمة في المطبخ المحلي.
- Cooking techniques (e.g., clay ovens, cooking underground, cooking with heatless methods like using salt).
- تقنيات الطبخ (مثل أفران الطين، الطبخ تحت الأرض, الطهي بطرق لا تعتمد على الحرارة مثل استخدام الملح).
- Street food.
- Traditional beverages.
- المشروبات التقليدية.
- Food etiquette (e.g., eating method, common vs individual dish, table vs floor seating)
- آداب الطعام (مثل طريقة تناول الطعام، والطبق المشترك مقابل الفردي، والجلوس على الطاولة مقابل الجلوس على الأرض)
- Fusion cuisine.
- Famous cooks and culinary personalities.
- الطهاة المشهورين وشخصيات الطهي.
- **Event-specific dishes:** Dishes served at certain events, such as wedding and Ramadan dishes. The questions and Instructions involve seeking guidance about the kind of dishes and how they are prepared when they are served.
  - **Example**: What are the most popular Ramadan dishes in Iraq? (Country-specific)
- **أطباق خاصة بالمناسبات:** الأطباق التي تقدم في مناسبات معينة، مثل أطباق الأعراس ورمضان. تتضمن الأسئلة والتعليمات طلب المعرفة الإرشادية حول نوع الأطباق وكيفية تحضيرها عند تقديمها.
  - **مثال**: ما هي أشهر الأكلات الرمضانية في العراق؟ (Country-specific)
- **Recipe and Cooking Technique:** Recipe and cooking technique questions/instructions involve seek
- ing guidance on how to prepare specific dishes or master certain cooking methods.
  - **Examples**:
    - What is the best way to roast a chicken to achieve a crispy skin and juicy meat? (General)
    - Explain how to prepare Jordanian Mansaf, including details of the cooking steps and the ingredients used. (Country-specific)
- **الوصفة وتقنية الطبخ:** تتضمن أسئلة/تعليمات الوصفة وتقنية الطبخ طلب إرشادات حول كيفية تحضير أطباق معينة أو إتقان طرق طهي معينة.
  - **أمثلة**:
    - ما هي أفضل طريقة لشوي الدجاج للحصول على جلد مقرمش ولحم طري؟ (General)
    - اشرح كيفية تحضير المنسف الأردني مع تفاصيل خطوات الطهي والمكونات المستخدمة. (Country-specific)
- **Ingredient and Substitution:** Ingredient and substitution questions/instructions revolve around selecting and substituting ingredients in recipes based on dietary restrictions, availability, or personal preferences.
  - **Examples**:
    - What can I use as a substitute for buttermilk in a recipe if I don't have any? (General)
    - What are the appropriate substitutes for olive oil in making Egyptian tahini if it's not available? (Country-specific)
- **المكونات والاستبدال:** تدور أسئلة/تعليمات المكونات والاستبدال حول اختيار المكونات واستبدالها في الوصفات بناءً على القيود الغذائية أو التوفر أو التفضيلات الشخصية.
  - **أمثلة**:
    - ما الذي يمكنني استخدامه كبديل للبن في الوصفة إذا لم يكن لدي؟ (General)
    - ما هي البدائل المناسبة لزيت الزيتون في صنع الطحينة المصرية في حال عدم توفره؟ (Country-specific)
- **Culinary Tips and Tricks:** Culinary tips and tricks questions/instructions seek advice and suggestions to enhance cooking skills, improve flavors, or troubleshoot common culinary challenges.
  - **Examples**
    - How can I prevent my homemade pizza dough from becoming too sticky? (General)
    - Do you have tips for keeping Arabic bread soft for a long period? (Country-specific)
- **نصائح وحيل الطهي:** نصائح وحيل الطهي، الأسئلة/التعليمات تسعى للحصول على النصائح والاقتراحات لتعزيز مهارات الطهي، أو تحسين النكهات، أو استكشاف أخطاء تحديات الطهي الشائعة وإصلاحها.
  - **أمثلة**:
    - كيف يمكنني منع عجينة البيتزا المنزلية من أن تصبح لزجة للغاية؟ (General)
    - هل لديك نصائح للحفاظ على طراوة الخبز الفلسطيني لفترة طويلة؟ (Country-specific)
- **Food Pairing and Flavor Combinations:** Food pairing and flavor combinations questions/instructions explore complementary flavors and ingredients that work well together in creating harmonious and flavorful dishes.
  - **Examples**
    - What are some classic food pairings for milk and cheese? (General)
    - Give me a list of the best ingredients to pair with Saudi Kabsa to add a distinctive flavor. (Country-specific)
- **اقتران الطعام ومجموعات النكهات:** تستكشف الأسئلة/التعليمات المتعلقة بإقران الطعام ومجموعات النكهات النكهات والمكونات التكميلية التي تعمل معًا بشكل جيد في إعداد أطباق متناغمة ولذيذة.
  - **أمثلة**:
    - ما هي بعض الأزواج الغذائية الكلاسيكية للحليب والجبن؟ (General)
    - أعطني قائمة من المكونات التي تتماشى مع الكبسة السعودية لإضافة نكهة مميزة. (Country-specific)
- **Cultural and Regional Cuisine:** Cultural and regional cuisine questions/instructions focus on understanding the traditional dishes, ingredients, and cooking styles associated with specific cultures or regions.
  - **Example**: What are some staple ingredients in Moroccan cuisine, and how are they typically used? (Country-specific)
- **الطبخ الثقافي والإقليمي:** تركز أسئلة/تعليمات المطبخ الثقافي والإقليمي على فهم الأطباق التقليدية والمكونات وأساليب الطهي المرتبطة بثقافات أو مناطق معينة.
  - **مثال**: ما هي بعض المكونات الأساسية في الطبخ المغربي وكيف يتم استخدامها عادة؟ (Country-specific)
- **Nutritional Information and Dietary:** Nutritional information and dietary questions/instructions pertain to understanding the nutritional content of foods, dietary guidelines, and addressing specific dietary needs or restrictions.
  - **Examples**
    - What are some good sources of plant-based protein for a vegetarian diet? (General)
    - I want to know the nutritional content of Foul Medames and how it can be modified to suit a low-carb diet. (Country-specific)
- **المعلومات الغذائية والغذائية:** تتعلق المعلومات الغذائية والأسئلة/التعليمات الغذائية بفهم المحتوى الغذائي للأطعمة، والإرشادات الغذائية، ومعالجة الاحتياجات أو القيود الغذائية المحددة.
  - **أمثلة**:
    - أعط بعض المصادر الجيدة للبروتين النباتي لنظام غذائي نباتي؟ (General)
    - أريد معرفة المحتوى الغذائي لطبق الفول المدمس وكيف يمكن تعديله ليناسب حمية منخفضة الكربوهيدرات. (Country-specific)
- **Food Safety and Storage:** Food safety and storage questions/instructions address proper handling, storage, and precautions to ensure food safety and prevent foodborne illnesses.
  - **Example**: How long can leftovers be safely stored in the refrigerator before they should be discarded? (General)
- **سلامة الأغذية وتخزينها:** تتناول الأسئلة/التعليمات المتعلقة بسلامة الأغذية وتخزينها التعامل السليم والتخزين والاحتياطات اللازمة لضمان سلامة الأغذية ومنع الأمراض المنقولة بالغذاء.
  - **مثال**: ما هي المدة التي يمكن تخزين بقايا الطعام فيها بشكل آمن في الثلاجة قبل التخلص منها؟ (General)
- **Food History and Origins:** Food history and origins questions/instructions delve into the historical background, cultural significance, and origin stories of specific dishes or ingredients.
  - **Example**: I would like to inquire about the history and origins of the Egyptian dish Koshari and how it has evolved over time. (Country-specific)
- **تاريخ الغذاء وأصوله:** أسئلة/تعليمات حول تاريخ وأصول الطعام تتعمق في الخلفية التاريخية والأهمية الثقافية وقصص الأصل لأطباق أو مكونات معينة.
  - **أمثلة**:
    - أود الاستفسار عن تاريخ وأصول طبق الكشري المصري وكيف تطور عبر الزمن. (Country-specific)
- **Dining Etiquette and Table Manners:** Dining etiquette and table manners questions/instructions cover proper behavior and manners when dining in different settings or cultures.
  - **Example**: What are the etiquette rules to follow when dining at a traditional Gulf banquet? (Country/region-specific)
- **آداب تناول الطعام وآداب المائدة:** تغطي الأسئلة/التعليمات المتعلقة بآداب تناول الطعام وآداب المائدة السلوك والآداب السليمة عند تناول الطعام في أماكن أو ثقافات مختلفة.
  - **مثال**: ما هي قواعد الإتيكيت التي يجب اتباعها عند تناول الطعام في مأدبة خليجية تقليدية؟ (Country/region-specific)
- **Food Sustainability and Ethical Considerations:** Questions/Instructions related to food sustainability and ethical considerations explore topics such as sustainable farming practices, fair trade, organic food, reducing food waste, and the impact of food choices on the environment and animal welfare.
  - **Example**: What are some sustainable seafood choices that can help protect marine ecosystems? (General)
- **استدامة الغذاء والاعتبارات الأخلاقية:** الأسئلة/التعليمات المتعلقة باستدامة الغذاء والاعتبارات الأخلاقية تستكشف موضوعات مثل الممارسات الزراعية المستدامة، والتجارة العادلة، والأغذية العضوية، والحد من هدر الطعام، وتأثير الخيارات الغذائية على البيئة ورعاية الحيوان.
  - **أمثلة**:
    - أقترح خيارات مستدامة للمأكولات البحرية يمكن أن تساعد في حماية النظم البيئية البحرية؟ (General)
- **Culinary Trends and Innovations:** Culinary trends and innovations questions/instructions address the latest developments in the culinary world, including new cooking techniques, emerging ingredients, fusion cuisines, and innovative culinary creations.
  - **Examples**
    - What are some current food trends in the plant-based or vegan culinary scene? (General)
    - I would like information on the latest culinary trends in Algeria. (Country-specific)
- **اتجاهات وابتكارات الطهي:** تتناول أسئلة/تعليمات اتجاهات وابتكارات الطهي أحدث التطورات في عالم الطهي، بما في ذلك تقنيات الطهي الجديدة، والمكونات الناشئة، والمأكولات المدمجة، وإبداعات الطهي المبتكرة.
  - **أمثلة**:
    - ما هي بعض الاتجاهات الغذائية الحالية في مشهد الطهي النباتي أو النباتي؟ (General)
    - أود الحصول على معلومات حول أحدث اتجاهات الطهي في الجزائر. (Country-specific)
- **Food and Culture:** Food and culture questions/instructions examine the role of food in different cultures, including traditional dishes, food rituals, festive foods, and the cultural significance of certain ingredients or cooking methods.
  - **Examples**
    - What are some traditional foods commonly prepared during the Lunar New Year celebration?
    - Explain the cultural role of food during Ramadan and how this is reflected in traditional dishes.
- **الغذاء والثقافة:** تتناول أسئلة/تعليمات الطعام والثقافة دور الطعام في الثقافات المختلفة، بما في ذلك الأطباق التقليدية، وطقوس الطعام، والأطعمة الاحتفالية، والأهمية الثقافية لبعض المكونات أو طرق الطهي.
  - **أمثلة**:
    - ما هي بعض الأطعمة التقليدية التي يتم إعدادها عادة خلال الاحتفال بالعام القمري الجديد؟
    - قم بتوضيح الدور الثقافي للطعام في شهر رمضان وكيف يتجلى ذلك في الأطباق التقليدية.
- **Health and Wellness:** Health and wellness questions/instructions focus on nutrition, balanced diets, dietary recommendations, special diets (such as vegan, gluten-free, or keto), superfoods, and the relationship between food and overall well-being.
  - **Examples**
    - What are some nutrient-dense foods that are beneficial for maintaining heart health?
    - How can one prepare healthy and balanced meals that align with a vegetarian diet without sacrificing traditional Arabic flavors?
- **الصحة والعافية:** تركز أسئلة/تعليمات الصحة والعافية على التغذية، والأنظمة الغذائية المتوازنة، والتوصيات الغذائية، والأنظمة الغذائية الخاصة (مثل النظام الغذائي النباتي أو الخالي من الغلوتين أو الكيتو)، والأطعمة الفائقة، والعلاقة بين الغذاء والصحة العامة.
  - **أمثلة**:
    - أعطني بعض الأطعمة الغنية بالعناصر الغذائية المفيدة للحفاظ على صحة القلب؟
    - كيف يمكن تحضير وجبات صحية ومتوازنة تتماشى مع النظام الغذائي النباتي دون التضحية بالنكهات العربية التقليدية؟
- **Food and Technology:** Food and technology questions/instructions explore the intersection of food and technology, including topics such as food delivery apps, meal planning apps, smart kitchen appliances, food tracking devices, and the use of technology in food production.
  - **Examples**
    - What are some innovative technologies being used in indoor farming for sustainable food production?
    - What are the latest technologies in the culinary field, and how can they be used to facilitate cooking at home?
- **الغذاء والتكنولوجيا:** تستكشف أسئلة/تعليمات الغذاء والتكنولوجيا التداخل بين الغذاء والتكنولوجيا، بما في ذلك موضوعات مثل تطبيقات توصيل الطعام، وتطبيقات تخطيط الوجبات، وأجهزة المطبخ الذكية، وأجهزة تتبع الطعام، واستخدام التكنولوجيا في إنتاج الغذاء.
  - **أمثلة**:
    - ما هي بعض التقنيات المبتكرة المستخدمة في الزراعة الداخلية لإنتاج الغذاء المستدام؟
    - ما هي أحدث التقنيات في مجال الطهي وكيف يمكن استخدامها لتسهيل عملية الطهي في المنزل؟
- **Food Writing and Criticism:** Food writing and criticism questions/instructions delve into the world of food journalism, restaurant reviews, food blogs, cookbooks, and the art of describing and evaluating food.
  - **Examples**
    - What are some renowned food critics known for their insightful restaurant reviews? (General)
    - I would like tips on how to write a critical review of a local restaurant serving traditional Sudanese cuisine. (Country-specific)
- **كتابة الطعام والنقد:** تتعمق أسئلة/تعليمات كتابة الطعام والنقد في عالم الصحافة الغذائية، ومراجعات المطاعم، ومدونات الطعام، وكتب الطبخ، وفن وصف الطعام وتقييمه.
  - **أمثلة**:
    - من هم بعض نقاد الطعام المشهورين المعروفين بتعليقاتهم الثاقبة عن المطاعم؟ (General)
    - أود نصائح حول كيفية كتابة مراجعة نقدية لمطعم محلي يقدم المأكولات العربية التقليدية. (Country-specific)
- **Food and Social Media:** Food and social media questions/instructions examine the influence of social media platforms on food culture, including food photography, viral food trends, recipe sharing, and the impact of social media on food choices and dining experiences.
  - **Examples**
    - How has social media influenced the popularity of food trucks and street food culture?
    - I want tips on how to photograph food for sharing on Instagram in an attractive way that reflects Arab culture.
- **الطعام ووسائل التواصل الاجتماعي:** تدرس الأسئلة/التعليمات المتعلقة بالطعام ووسائل التواصل الاجتماعي تأثير منصات التواصل الاجتماعي على ثقافة الطعام، بما في ذلك تصوير الطعام، واتجاهات الطعام واسعة الانتشار، ومشاركة الوصفات، وتأثير وسائل التواصل الاجتماعي على خيارات الطعام و تجارب تناول الطعام.
  - **أمثلة**:
    - كيف أثرت وسائل التواصل الاجتماعي على شعبية شاحنات الطعام وثقافة طعام الشوارع؟
    - أريد نصائح حول كيفية تصوير الطعام لمشاركته على إنستغرام بطريقة جذابة تعكس الثقافة العربية.
- **Seasonal and Local Foods:** Seasonal and local foods questions/instructions highlight the importance of eating seasonally and supporting local farmers, as well as the benefits of fresh, locally sourced ingredients.
  - **Examples**:
    - What are some seasonal fruits and vegetables that are typically available during the summer months?
    - What are the traditional seasonal foods in the Gulf region, and how can local farmers be supported by choosing these products?
- **الأطعمة الموسمية والمحلية:** تسلط الأسئلة/التعليمات المتعلقة بالأطعمة الموسمية والمحلية الضوء على أهمية تناول الطعام موسميًا ودعم المزارعين المحليين، فضلاً عن فوائد المكونات الطازجة من مصادر محلية.
  - **أمثلة**:
    - ما هي بعض الفواكه والخضروات الموسمية المتوفرة عادةً خلال أشهر الصيف؟
    - ما هي الأطعمة الموسمية التقليدية في المنطقة الخليجية وكيف يمكن دعم المزارعين المحليين من خلال اختيار هذه المنتجات؟
- **Food and Emotional Connection:** Food and emotional connection questions/instructions explore the role of food in evoking emotions, triggering nostalgia, and creating meaningful connections with others through shared meals and culinary experiences.
  - **Examples**:
    - How can I recreate a traditional family recipe that holds sentimental value for special occasions?
    - I would like to explore how food can evoke memories and strengthen family bonds, especially during cultural occasions like holidays.
- **الغذاء والاتصال العاطفي:** تستكشف أسئلة/تعليمات الطعام والارتباط العاطفي دور الطعام في إثارة المشاعر وإثارة الحنين إلى الماضي وإنشاء اتصالات ذات معنى مع الآخرين من خلال الوجبات المشتركة وتجارب الطهي.
  - **أمثلة**:
    - كيف يمكنني إعادة إنشاء وصفة عائلية تقليدية تحمل قيمة عاطفية للمناسبات الخاصة؟
    - أود استكشاف كيف يمكن للطعام أن يحفز الذكريات ويعزز الروابط الأسرية، خاصة في المناسبات الثقافية مثل الأعياد.

**Possible instructions include but aren’t limited to:**

- **Write** a recipe for ……., providing detailed step-by-step instructions, ingredient measurements, and cooking techniques.
- اكتب وصفة لـ …….، مع توفير تعليمات مفصلة خطوة بخطوة، وقياسات المكونات، وتقنيات الطهي.
- **Create** a meal plan for a week, considering nutritional balance, dietary restrictions, and personal preferences.
- ضع خطة وجبات لمدة أسبوع، مع الأخذ في الاعتبار التوازن الغذائي والقيود الغذائية والتفضيلات الشخصية.
- **Develop** a guide on …………………..
- ضع دليل حول ...............
- **List** famous dishes in ………
- اعط قائمة الأكلات المشهورة في ..........
- How to cook……
- كيف تطبخ……
- What are the ingredients of ……….
- ما هي مكونات ...........
- What is …….. famous dishes
  - what is tunisia famous dish/food
- ما هو الأكلات المشهورة في ……
  - ما هو الطبق/الأكلة التونسية الشهيرة؟
- What is the recipe for ……..
- ما هي وصفة ..........
- What are some common table manners or dining customs in …?
- ما هي بعض آداب المائدة الشائعة أو عادات تناول الطعام في …؟
- **Summarize** ……….
- لخص ……….
- Write a guide on food etiquette in ………
- أكتب دليل آداب الطعام في ..........
- What are the essential components that should be included in ………
- ما هي العناصر الأساسية التي يجب أن يتضمنها ..........
- What are some popular street foods in …… and where can they be commonly found?
- ما هي بعض الأطعمة الشعبية في الشوارع …….وأين يمكن العثور عليها بشكل شائع؟
- What are some traditional desserts or sweets in ………, and what are their main ingredients?
- ما هي بعض الحلويات أو الحلويات التقليدية الموجودة في ………، وما هي مكوناتها الرئيسية؟
- Could we cook ….. using ……..
- هل يمكننا طهي ….. باستخدام ……..
- Is ………., a popular ……… dish made with a combination of rice, lentils, and pasta?
- هل ……… طبق شعبي ……… مصنوع من مزيج من الأرز والعدس والمعكرونة؟
- What is …….
- ما هو…….
- Write an essay exploring the historical and cultural influences on ……food. Discuss how ancient ……., Arab, Mediterranean, and other regional cuisines have shaped the culinary traditions of ……….
- اكتب مقالاً يستكشف التأثيرات التاريخية والثقافية على ……الطعام. ناقش كيف ساهمت المأكولات القديمة …… والمأكولات العربية والمتوسطية وغيرها من المأكولات الإقليمية في تشكيل تقاليد الطهي في ……….

#### Examples

**Example 1**

| **Instruction** | اعط قائمة أطباق يأكلها المغاربة في شهر رمضان. |
| --- | --- |
| **Input** |     |
| **Output** | اليك قائمة أطباق يأكلها المغاربة في شهر رمضان:<br><br>1\. الحريرة: حساء يدخل في تكوينه البصل والطماطم والبقدونس والكزبرة والكرفس والحمص، واللحم أو البيض، والعدس والشعيرية وبعض الدقيق.<br><br>2\. الشباكية: عجين مقلي في الزيت، يتم إغراقه في العسل ويغمس في السمسم. ويتم تحضير الشباكية قبل رمضان ثم تخزن للاستخدام طوال الشهر.<br><br>3\. البطبوط: بعضها محشو بأنواع اللحم المفروم والخضار والجبن، وبعضها غير محشو، قد يكون مطبوخاً بمقلاة جافة، أو مع الزيت، كما يقدم بأحجام مختلفة.<br><br>4\. سلو/ السفوف: مسحوق من الطحين المحمص واللوز والسمسم والسكر، وتُعجن كل هذه المكونات بالزبدة.<br><br>5\. البريوات: عجين ورقي يتم حشوه بتشكيلة واسعة من الحشوات الحلوة والمالحة، من الخضار إلى اللحم مروراً بالسمك والمكسرات، ويتم قلي البريوات في الزيت إغراقها في العسل.<br><br>6\. المسمن/ الملاوي: يتم تحضير عجينهما وبسطه حتى يصبح مكوناً من طبقات عديدة، ثم يقلى في القليل من الزيت، ويختار الطاهي بين إضافة بعض الشحم والبصل إليه أو إبقائه طبيعياً.  <br>7\. البغرير: عجين من السميد والطحين المخلوط بالماء، يتم طهيه في المقلاة، ثم يقدم مع أنواع العسل والمربى. |
| **Source** | [https://www.alaraby.co.uk/أشهر-7-مأكولات-رمضانية-في-المغرب](https://www.alaraby.co.uk/%D8%A3%D8%B4%D9%87%D8%B1-7-%D9%85%D8%A3%D9%83%D9%88%D9%84%D8%A7%D8%AA-%D8%B1%D9%85%D8%B6%D8%A7%D9%86%D9%8A%D8%A9-%D9%81%D9%8A-%D8%A7%D9%84%D9%85%D8%BA%D8%B1%D8%A8) |

**Example 2**

| **Instruction** | ما هو المشروب المغربي التقليدي وكيف يتم تحضيره؟ |
| --- | --- |
| **Input** |     |
| **Output** | هو الشاي الأخضر المغربي المعروف ب(أتاي). ويحضر عن طريق مزج الشاي الأخضر الصيني المسمى بالبارود مع أوراق النعناع الطازجة، ومن ثم يضاف إليه كمية من الماء الساخن والسكر. |
| **Source** | [https://altibbi.com/مصطلحات-طبية/اعشاب-طبية/شاي-اخضر](https://altibbi.com/%D9%85%D8%B5%D8%B7%D9%84%D8%AD%D8%A7%D8%AA-%D8%B7%D8%A8%D9%8A%D8%A9/%D8%A7%D8%B9%D8%B4%D8%A7%D8%A8-%D8%B7%D8%A8%D9%8A%D8%A9/%D8%B4%D8%A7%D9%8A-%D8%A7%D8%AE%D8%B6%D8%B1) |

#### Specific guidelines

- You can feel free to use various measurement and temperature metrics as long as their consistent within a single request-response pair.

### History

Here we would like to construct instruction related to the history domain for a specific country,

focusing on, but not limited to:

#### Sample Topics

- **Ancient eras**
  - **العصور القديمه, عصور ما قبل التاريخ**
- **Modern history**
  - **التارخ المعاصر/ الحديث**
- **Important events**
  - **الاحداث المهمه**
- **Events throughout time intervals**
  - **الاحداث خلال العصور المختلفه**
- **Islamic history, different eras**
  - **مختلف العصور الاسلاميه**
- **Islamic conquests**
  - **الغزوات/ الفتوحات الاسلاميه**
- **Pros/cons of each era**
  - **مزايا وعيوب كل عصر**
- **Ruler of each era, their accomplishments**
  - **الحكام و انجازاتهم**
- **Historical Events:** Question/Instructions related to different historical events, including major ones.
  - **Examples**:
    - How did the Babylonian civilization fall? (Country specific)
    - Discuss the causes and consequences of the Suez Crisis of 1956, especially with regard to Egypt and its relations with Western powers. (Country specific)
    - What led to the extinction of the dinosaurs (General Domain)
- **الأحداث التاريخية:** أسئلة/تعليمات تتعلق بأحداث تاريخية مختلفة، بما في ذلك الأحداث الكبرى.
  - **أمثلة**:
    - كيف سقطت الحضارة البابلية؟(Country specific)
    - أكتب عن أسباب ووعواقب أزمة السويس عام 1956، خاصة فيما يتعلق بمصر وعلاقاتها مع القوى الغربية. (Country specific)
    - ما الذي أدى إلى انقراض الديناصورات. (General Domain)
- **Islamic History:** Questions/Instructions related to Islamic history, different eras, conquest, timeline, ruler of each era, their accomplishments
  - **Examples**:
    - What are the most famous conquests during the era of the Rightly Guided Caliphs? (General Domain)
    - Name different Caliphs ruled egypt .(Country specific)

- **التاريخ الإسلامي:** أسئلة/تعليمات تتعلق بالتاريخ الإسلامي، العصور المختلفة، الفتح، الجدول الزمني، حاكم كل عصر، إنجازاتهم
  - **أمثلة**:
    - ما هي اشهر الفتوحات في عهد الخلفاء الراشدين. (General Domain)
    - اذكر اسماء الخلفاء المختلفين الذين حكموا مصر.(Country specific)
- **Different Historical Eras:** We are interested in questions/instructions that explore, compare different eras as prehistoric, modern eras. This might also include the timeline, pros and cons of each era, the Ruler of each era, their accomplishments, and the impact of each era.
  - **Examples**:
    - Explain how the Ottoman Empire shaped the social and economic dynamics of the Middle East, especially in relation to Turkey and Egypt (Country specific)
    - Dicuss different prehistoric ages (General Domain)
- **العصور التاريخية المختلفة:** نحن مهتمون بالأسئلة والتعليمات التي تستكشف وتقارن بين العصور المختلفة مثل عصور ما قبل التاريخ والعصور الحديثة. وقد يشمل ذلك أيضًا الجدول الزمني وإيجابيات وسلبيات كل عصر وحاكم كل عصر وإنجازاته وتأثير كل عصر.
  - **أمثلة**
    - أكتب عن الإمبراطورية العثمانية التي شكلت الديناميكيات الاجتماعية والاقتصادية في الشرق الأوسط، وخاصة فيما يتعلق بتركيا ومصر(Country specific)
    - ناقش عصور ما قبل التاريخ المختلفة(General Domain)
- **Chronological**: Chronological questions/instructions focus on the sequence and timeline of historical events.
  - **Example**: What were the major events that led to the outbreak of World War II? (General Domain)
- **ترتيب زمني:** تركز الأسئلة/التعليمات المتعلقة بالتسلسل الزمني على تسلسل الأحداث التاريخية وجدولها الزمني.
  - **مثال**: ما هي الأحداث الكبرى التي أدت إلى اندلاع الحرب العالمية الثانية؟(General Domain)
- **Causal**: Causal questions explore the causes and factors that led to specific historical events or developments.
  - **Example**: What were the main causes of the 23rd July Egyptian Revolution?(Country specific)
- **السببية**: تستكشف الأسئلة السببية الأسباب والعوامل التي أدت إلى أحداث أو تطورات تاريخية محددة.
  - **مثال**: ما هي الأسباب الرئيسية لثورة 23 يوليو المصرية؟(Country specific)
- **Comparative**: Comparative questions/instructions involve examining similarities and differences between different historical periods, regions, or civilizations.
  - **Examples:**
    - How did the Industrial Revolution affect the Ottoman Empire?(Country specific)
    - How did the Industrial Revolution change life in the world?(General Domain)
- **المقارنة**: تتضمن الأسئلة/التعليمات المقارنة فحص أوجه التشابه والاختلاف بين الفترات التاريخية أو المناطق أو الحضارات المختلفة.
  - **أمثلة**
    - كيف أثرت الثورة الصناعية على الدولة العثمانية؟(Country specific)
    - كيف غيرت الثورة الصناعية الحياة في العالم؟(General Domain)
- **Interpretive**: Interpretive questions/instructions involve analyzing and interpreting historical sources, documents, or texts to understand their meaning and significance.
  - **Example**: What can we learn about ancient Egyptian society from the writings of rosetta stone?(Country specific)
- **التفسيرية**: تتضمن الأسئلة/التعليمات التفسيرية تحليل وتفسير المصادر أو الوثائق أو النصوص التاريخية لفهم معناها وأهميتها.
  - **مثال**: ماذا يمكننا أن نتعلم عن المجتمع المصري القديم من كتابات حجر رشيد؟
- **Historiographical**: Historiographical questions/instructions examine the interpretations, perspectives, and debates among historians regarding a particular historical event or period.
  - **Example**: How have historians' interpretations of the ……. War changed over time?
- **تاريخية**: الأسئلة/التعليمات التاريخية تدرس التفسيرات ووجهات النظر والمناقشات بين المؤرخين فيما يتعلق بحدث أو فترة تاريخية معينة.
  - **مثال**: كيف جاءت تفسيرات المؤرخين لـ ……. تغيرت الحرب مع مرور الوقت؟
- **Social and Cultural:** Social and cultural questions/instructions explore the lives, beliefs, values, and practices of people in different historical contexts.
- الاجتماعية والثقافية: تستكشف الأسئلة/التعليمات الاجتماعية والثقافية حياة الناس ومعتقداتهم وقيمهم وممارساتهم في سياقات تاريخية مختلفة.
  - **مثال**: ما هو دور المرأة في العصور الوسطى ……. مجتمع؟
- **Political**: Political questions/instructions focus on studying political systems, institutions, ideologies, and movements in history.
  - **Example**: What were the key factors that led to the rise of fascism in ……. during the early 20th century?
- **سياسية**: تركز الأسئلة/التعليمات السياسية على دراسة الأنظمة السياسية والمؤسسات والأيديولوجيات والحركات في التاريخ.
  - **مثال**: ما هي العوامل الأساسية التي أدت إلى ظهور الفاشية في ……. خلال أوائل القرن العشرين؟
- **Economic**: Economic questions/instructions involve studying economic systems, trade, production, and the impact of economic factors on historical events.
  - **Example**: How did the …….. trade impact the economies of ……….?
- **اقتصادية**: تتضمن الأسئلة/التعليمات الاقتصادية دراسة النظم الاقتصادية والتجارة والإنتاج وتأثير العوامل الاقتصادية على الأحداث التاريخية.
  - **مثال**: كيف أثرت تجارة …….. على اقتصاديات ……….؟
- **Global and Transnational:** Global and transnational questions/instructions explore the interactions, connections, and exchanges between different regions and civilizations throughout history.
  - **Example**: How did the……… cultural and economic exchanges between …….. and the ……….?
- **العالمية وعبر الوطنية:** تستكشف الأسئلة/التعليمات العالمية وعبر الوطنية التفاعلات والصلات والتبادلات بين المناطق والحضارات المختلفة عبر التاريخ.
  - **مثال**: كيف تم التبادل الثقافي والاقتصادي بين ........... و..........؟

#### Instructions could be, but not limited to

- **Summarize** the following paragraph
  - **لخص** أهم الأحداث في عصور ما قبل التاريخ
  - **لخص** المقال التالي فيما لايزيد عن 20 سطر
- **Give me a summary of the** ………….era
  - **اعطني نبذة** عن العصر الفاطمي في مصر؟
  - **اكتب مقال عن** تاريخ الجزائر
- **In which of the following years/era**, xx took place
  - a)...
  - b)...
  - c)...
- **في أي من السنوات/الحقبة التالية**، حدث xx
  - ا)……
  - ب)..............
  - ج)............
- **List for me the** name of events happened between 1990-1991
- **اذكر لي** أسماء الأحداث التي وقعت بين عامي 1970-1991
- **Which of the following** **apply to** …
  - **a)**...
  - **b)**...
  - **c)**....
- **أي مما يلي ينطبق على**…
  - **أ)**...
  - **ب)**...
  - **ج)**....
- **Is the following statement correct or incorrect:**
  - ………………………………………………………..
- **هل العبارة التالية صحيحة أم غير صحيحة:**
  - ……………………………………………………………..
- **Suggest a book to read** that talks about …………
- **اقترح كتابًا لقراءته** يتحدث عن ……………
- **Explain why** the following era xxxx was named …………….
- **اشرح سبب تسمية** العصر التالي …………..باسم …………..
- **Discuss why** xxxx era has fallen
- **ناقش سبب** سقوط عصر ………….
- **Rephrase/Reformat** the following paragraph so that it has the following format:
  - Title
  - Summary
  - Key Points
- **أعد صياغة/أعد صياغة** الفقرة التالية بحيث تكون بالتنسيق التالي:
  - عنوان
  - ملخص
  - النقاط الرئيسية

#### Examples

**Example 1**

| **Instruction** | لخص أهم الأحداث في عصور ما قبل التاريخ في اليمن |
| --- | --- |
| **Input** |     |
| **Output** | يضم عصر ما قبل التاريخ فترتين رئيسيتين هما العصر الحَجَرِي القَدِيْم، والعصر الحَجَرِي الحَدِيْث.<br><br>العصر الحجري القديم، هو الفترة الأولى والأطول في تاريخ البشرية، والتي بدأت مع ظهور الجنس البشري Homo قبل 3 ملايين سنة تقريباً وانتهت قبل 10.000 سنة تقريباً، وهي بذلك فترة معاصرة للفترة الجيولوجية للعصر الحديث الأدنى. ويتميز العصر الحجري القديم قبل كل شيء باقتصاد الصَّيْد حيث كان البشر يمارسون الصيد ويستفيدون من الموارد المتاحة في الطبيعة (الصَّيْد، وصَيْد الأسْمَاك، وجَمْع الطَّعَام).<br><br>يتسم العصر الحجري الحديث بوجود تغيرات جذرية على الصعيدين الاجتماعي والفني تتعلق بتبني الجماعات البشرية اقتصاد يعتمد على الإنتاج الزراعي والثروة الحيوانية، الأمر الذي أدى في الغالب إلى حدوث عمليات اسْتِيْطَان. وقد تمثلت الابتكارات التقنية الرئيسية في انتشار الأدوات الحَجَرِيَّة المَصْقُوْلَة والفَخَّار. وفي بعض المناطق، كانت تلك التغيرات العميقة سريعة نسبياً ونتحدث هنا عن «ثورة العصر الحجري الحديث». ففترة العصر الحجري الحديث هي ظاهرة تدريجية حدثت في أوقات مختلفة على حسب ظروف كل منطقة. ففي منطقة الشرق الأوسط، بدأ العصر الحجري الحديث قبل حوالي 9000 سنة قبل الميلاد وانتهى مع انتشار المعادن واختراع الكتابة، قبل حوالي 3300 سنة قبل الميلاد. ففي اليمن قد تعود بداية العصر الحجري الحديث إلى حوالي 7000 سنة قبل الميلاد وحتى 3000 سنة قبل الميلاد.<br><br>13وتعد الحقبة اللاحقة والمعروفة باسم العصر البُرُوْنْزِي جزءاً لا يتجزأ من عصر ما قبل التاريخ بالمعنى الدقيق. وفي أغلب الأحيان، يضعها علماء الآثار وبشكل مختلف في مجموعة زمنية وثقافية وأحياناً يطلق عليها «تاريخ نشوء البشرية». |
| **Source** | <https://books.openedition.org/cefas/2458#:~:text=%D9%88%D8%A7%D8%AA%D8%B3%D9%85%20%D8%A7%D9%84%D8%B9%D8%B5%D8%B1%20%D8%A7%D9%84%D8%AD%D8%AC%D8%B1%D9%8A%20%D8%A7%D9%84%D9%82%D8%AF%D9%8A%D9%85%20%D8%A7%D9%84%D8%A3%D9%88%D8%B3%D8%B7,%D8%A7%D9%84%D8%B9%D8%A7%D9%82%D9%84)%20%D9%81%D9%8A%20%D8%AC%D9%85%D9%8A%D8%B9%20%D8%A3%D9%86%D8%AD%D8%A7%D8%A1%20%D8%A7%D9%84%D8%B9%D8%A7%D9%84%D9%85>. |

**Example 2**

| **Instruction** | لخص المقال التالي فيما لايزيد عن 20 سطر |
| --- | --- |
| **Input** | العصر العباسي الثالث<br><br>عصر النفوذ البويهي<br><br>1055 م ( - 447- ه / 946 334 (<br><br>ظهور البويهيين<br><br>يرجع اصل البويهيين إلى الديلم الذين استوطنوا المنطقة الواقعة بين طبرستان والجبال<br><br>وجيلان و بحر الخزر وجزء من أذربيجان وبلاد الران من جهة الغرب وكانوا يدينون<br><br>بالوثنية في باديء امرهم، ثم انتشر الإسلام بينهم في بداية القرن الرابع الهجري على يد<br><br>الحسن بن علي الزيدي الملقب بالاطروش .<br><br>وقد ارجع بعض المؤرخين نسبب البويهيين الى سابور ذي الأكتاف ، في حين نسبهم<br><br>البعض الآخر إلى قبيلة ضبة العربية. والواقع أن البويهيين هم قبائل فارسية تتكلم اللغة<br><br>الفارسية بلهجة محلية، ولا صلة لهم بالعرب. ويبدوا أن هؤلاء المؤرخين اضفوا على<br><br>البويهيين نسبا عريقا لرفع مكانتهم بعد أن تم لهم السيطرة على اجزاء كبيرة من العالم<br><br>الاسلامي وبسطوا نفوذهم على دار الخلافة<br><br>وكانت الأسرة البويهية تتكون من اخوة ثلاث هم :- علي والحسن واحمد أبناء أبي شجاع<br><br>بويه بن فناخسرو، وكان بويه هذا رجلا من عامة الناس، يتعيش من صيد السمك بناحية<br><br>بحر قزوين من بلاد الديلم وعمل أبناؤه جنودا في جيش القائد الديلمي )ماكان بن كاكي(،<br><br>وقد أتاحت لهم مواهبهم العسكرية الوصول الى مراكز هامة في جيشه.<br><br>وكان ولاء الجند في مثل هذا النظام للقائد الذي يتولى الانفاق عليهم، وجرت العادة أن<br><br>ينتقل هؤلاء الجند من خدمة رئيس الى خدمة اخر، حسب الظروف الاقتصادية المرتبطة<br><br>بكثرة الغنائم وقلتها، فلما ضعف أمر )ماكان بن كاكي( على أثر هزيمته امام )مرداويج<br><br>زيار الديلمي( وعجز نوعا ما عن ضمان الارزاق للجند تفرق عنه كثير من أصحابه،<br><br>ومنهم علي بن بويه واخوته، وطلبوا السماح لهم بالانتقال إلى خدمة )مرداويج(، فتم لهم<br><br>ذلك، ورحب مرداويج بهم، واغدق عليهم الأموال، وولى عليا بن بويه حكم بلاد الكرج<br><br>الواقعة بين همدان وأصبهان .<br><br>غير ان مرداويج ما لبث أن ندم على تولية على بن بويه بلاد الكرج، فكتب إلى اخيه<br><br>وشمكير في الري وإلى أبي عبد الله الحسين بن محمد الملقب بالعميد يأمرها بصرف أولاد<br><br>بويه ومنعهم من الوصول الى بلاد الكرج، الا أن رغبة مرداويج هذه لم تتحقق، اذ تمكن<br><br>علي بن بويه من الوصول إلى مقر عمله بمساعدة أبي عبد الله نفسه ، واستقر في حكم<br><br>البلاد، واظهر كفاءة ومقدرة في تصريف الأمور، وأحسن إلى أهلها فحظي بتأييد الجند<br><br>ومال الناس اليه .<br><br>الا أن عليا بن بويه لم يلبث أن فارق بلاد الكرج بعد أن جبي ضرائبها لمدة عام كامل،<br><br>وسار نحو الجنوب واستولى على اصبهان سنة ) 321 ه( بعد انتصاره على ابي الفتح<br><br>ياقوت عامل العباسيين على المدينة ، وقد زادت تحركات ابن بويه هذه من مخاوف<br><br>مرداويج فصمم على القضاء عليه، وأنفذ إليه جيشا بقيادة أخيه وشمكير وكانت سياسة بويه<br><br>في هذه المرحلة تقضي بعدم الاشتباك مع قوات مرداويج وبالابتعاد عن متناول يده قدر<br><br>الإمكان، ولذلك فانه ما أن سمع بتحرك جيش وشمكير نحوه حتى انسحب من اصبهان<br><br>متجها نحو أرجان فدخلها في ذي الحجة من عام 321 ه من غير حرب بعد أن هرب<br><br>اميرها )ابو بكر بن ياقوت(، وشرع بجباية ضرائبها التي بلغت ألفي الف درهم، ثم فارقها<br><br>خوفا من اجتماع مرداويج واخيه وشمكير على حربه، وتوجه إلى مدينة اصطخر وانتصر<br><br>على المظفر بن ياقوت، وتمكن بعد ذلك من الاستيلاء على شيراز بعد أن خاض معركة<br><br>عنيفة في سنة 322 ه<br><br>اتصال البويهيين بالخلافة العباسية<br><br>اقام علي بن بويه فترة في شيراز، انصرف خلالها إلى تنظيم اموره المالية، وتدعيم نفوذه<br><br>في البلاد، ثم تطلع للحصول على تفويض الخلافة واعترافها بشرعية حكمه، فأرسل الى<br><br>329 ه ( . يلتمس التفويض بالحكم، وتعهد بدفع مبلغ ثمان مائة - الخليفة الراضي ) 322<br><br>مليون درهم إلى دار الخلافة في كل عام. وكانت ظروف الخلافة آنذاك سيئة وحاجتها إلى<br><br>المال شديدة، فلم يتردد الخليفة بالموافقة على طلبه وارسل اليه الخلع ومنشور التفويض مع<br><br>احد رسله، واوصاه بأن لا يسلم ابن بويه شيئا حتى يقبض المال المتفق عليه، فلما وصل<br><br>رسول الخليفة شيراز خرج على بن بويه لاستقباله وأخذ الخلعة، وقرأ على الناس تفويض<br><br>الخليفة واعترافه بحكمه على البلاد، غير انه ماطل في دفع الأموال واستبقى رسول الخليفة<br><br>عنده حتى ادركته الوفاة في شيراز سنة 323 ه .<br><br>وكان لحصول ابن بويه على تفويض الخلافة واعترافها، أثر بالغ في نفس مرداويج الذي<br><br>ثارت ثائرته، وعزم على القضاء على نفوذه، فانفذ جيشا كبيرا إلى منطقة الأحواز، ليقطع<br><br>بذلك الطريق على ابن بويه في الوصول إلى بغداد، وقد تمكن هذا من تحقيق هدفه،<br><br>فاستولى على الاحواز، فأثار ذلك مخاوف على بن بويه، وادرك أن مصلحته في هذه<br><br>الظروف تقضي الاتفاق مع مرداويج وعدم التورط معه بحرب جديدة، فعرض عليه في<br><br>مرونة سياسية أن يدخل في طاعته ويكون تابعا له في حكمه ويخطب باسمه في بلاده،<br><br>واثباتا لحسن نيته ارسل علي بن بويه اخاه الحسن بن بويه ليكون رهينة عنده على الوفاء .<br><br>غير أن مرداويج لقي مصرعه بعد فترة قصيرة على يد جماعة من الاتراك الذين كانوا<br><br>يؤلفون جزء ا من جيشه، بسبب سوء معاملته لهم وتفضيله الديلم عليهم وذلك في سنة 323<br><br>ه وتفرق كثير من جند الديلم بعد مع مرداويج بن زيار، وانضم فريق منهم إلى علي بن<br><br>بويه، واتفق من بقي منهم على طاعة وشمكير بن زيار، وقد إتاح مصرع مرداويج<br><br>للبويهيين تحقيق أهدافهم التوسعية، فاستولوا على اصبهان والري، ودخل احمد بن بويه<br><br>الأحواز سنة 326 ه على الرغم من المقاومة التي قوبل بها في هذه المنطقة، وبسط<br><br>البويهيون نفوذهم على بلاد فارس والاحواز والري واصفهان وهمذان وشمال العراق )اقليم<br><br>الجبال( .<br><br>وتطلع احمد بن بويه إلى الاستيلاء على بغداد، وكانت أحوال الخلافة انذاك مضطربة على<br><br>أثر الخلاف الذي قام بين الخليفة المتقي وامير الأمراء توزون التركي، فشرع احمد بن<br><br>بويه في مهاجمة أملاك الدولة العباسية في سنة 332 ه، ووصل إلى ديالى واصبح على<br><br>مشارف بغداد، الا أن توزون ما لبث أن تصدى له ودارت معركة كبيرة على ضفاف نهر<br><br>ديالى استمرت بضعة عشر يوما، وانتهت بهزيمة أحمد بن بويه في اليوم )الرابع من ذي<br><br>الحجة سنة 322 ه ( ، غير أن الظروف لم تلبث ان سنحت للبويهيين بدخول بغداد، على<br><br>أثر وفاة الأمير توزون في سنة 333 ه ، وتولي كاتبه )ابن شيرزاد( منصب امير الأمراء<br><br>.<br><br>فقد عم الاضطراب نواحي العراق في عهد الخليفة المستكفي، وعمد جماعة من أمراء<br><br>الجند الى مراسلة احمد بن بويه يطلبون اليه المسير الى بغداد، فرحل عن الاحواز، ودخل<br><br>بغداد في )الحادي عشر من شهر جمادى الآخرة من سنة 334 ه ( ، فاحتفى الخليفة<br><br>بقدومه، وخلع عليه، فبايعه أحمد بن بويه وحلف له باغلظ الإيمان، كما حلف المستكفي<br><br>لاحمد واخويه وكتب بذلك كتابا، وعقد له لواء امرة الامراء ولقبه )معز الدولة(، كما لقب<br><br>اخاه عليا عماد الدولة( واخيه الحسن )ركن الدولة(، وامر ان تنقش القابهم وكناهم على<br><br>الدنانير والدراهم وما أن استتب الأمر لمعز الدولة البويهي في بغداد حتي استأثر بالسلطة<br><br>دون الخليفة، ووضع يده على جميع أملاكه، وخصص له راتبا قدره خمسة آلاف درهم في<br><br>كل يوم .<br><br>ثم لم يلبث أن آمر بقطع هذا الراتب وحدد له اقطاعات ليسد منها نفقاته ، ثم اظهر<br><br>البويهيون ما كانوا يضمرونه لخلفاء بني العباس فعمدوا إلى خلع المستكفي في جمادي<br><br>الآخرة من سنة 334 ه، واعتقلوه بدار معز الدولة بعد ايام قليلة من دخولهم بغداد، وبايعوا<br><br>أبا القاسم الفضل بن المقتدر الذي لقب )بالمطيع( ، وأحضر المستكفي فشهد على نفسه<br><br>بالخلع وسلمت عيناه، وظل معتقلا حتى توفي في ربيع الآخرة من سنة 338 ه .<br><br>سقوط البويهيين<br><br>لم يلبث البويهيون أن تعرضوا إلى الانقسام والتنازع بعد عصر الأمراء الأوائل الذين<br><br>حافظوا على وحدة الأسرة وتدعيم نفوذها، فقد تنازع ابناء عضد الدولة على الحكم حتى<br><br>استقرت الأمور بيد بهاء الدولة. ثم تفجر الصراع ثانية بين أولاده، سلطان الدولة ومشرف<br><br>الدولة وجلال الدولة، وبدأ البويهيون يسيرون بخطى سريعة نحو الاضمحلال بسبب<br><br>الحروب التي اندلعت بين أفراد هذه الأسرة من جهة، وانصرافهم عن مواجهة أعدائهم في<br><br>الخارج من جهة أخرى، فسقطت دولتهم على يد السلاجقة في سنة 447 ه، حين دخل<br><br>طغرلبك بغداد وقبض على اخر ملوكهم وهو الملك الرحيم )أبو نصر خسرو فيروز(<br><br>وارسله مقيدا إلى الري، واسقط اسمه من الخطبة في آخر رمضان من السنة المذكورة ،<br><br>وأسدل الستار بذلك على الدولة البويهية لتحل محلها الدولة السلجوقية. |
| **Output** |     |
| **Source** | <https://uomustansiriyah.edu.iq/media/lectures/9/9_2020_07_15!01_23_23_AM.pdf> |

### Travel (country specific)

Here, we would like to construct instructions related to the travel domain for a specific country, for example focusing on any of the following items (but possibly others):

#### Sample Topics

- **Important landmarks**, cities, and beaches
- المعالم والمدن والشواطئ الهامة
- How to plan a day visit or a week visit.
- كيفية التخطيط لزيارة يومية أو زيارة أسبوعية.
- What could be done in each city
  - Certain activities such as skiing, sightseeing, and shopping
- ما الذي يمكن عمله في كل مدينة؟
  - أنشطة معينة مثل التزلج ورؤية المواقع والتسوق
- **Destination**: Destination questions/instructions focus on selecting and learning about specific travel destinations.
  - **Example**: What are the must-see attractions in Marrakech, Morocco?
- **الوجهة**: تركز أسئلة/تعليمات الوجهة على اختيار وجهات سفر محددة والتعرف عليها.
  - **مثال**: ما هي المعالم السياحية التي يجب مشاهدتها في مراكش بالمغرب؟
- **Activities**: Activities questions/instructions focus on different activities in each city, such as visiting landmarks, beaches, sightseeing, and shopping.
  - **ُExample**: What recreational activities can be done in Qatar
- **الأنشطة:** تركز أسئلة/تعليمات الأنشطة على الأنشطة المختلفة في كل مدينة، مثل زيارة المعالم والشواطئ ومشاهدة المعالم السياحية والتسوق.
  - **مثال**: ما هي الأنشطة الترفيهية الممتعة التي يمكن القيام بها في قطر.
- **Planning,Inquiries and Itinerary:** Planning,Inquiries and itinerary questions/instructions involve organizing and structuring the travel experience, including activities, accommodations, and transportation.
  - **Example**: What is the best itinerary for a one-week trip to Tunisia?
- **التخطيط ومسار الرحلة:** تتضمن أسئلة/تعليمات التخطيط ومسار الرحلة تنظيم وهيكلة تجربة السفر، بما في ذلك الأنشطة والإقامة والنقل.
  - **مثال**: ما هو أفضل خط سير لرحلة إلى تونس لمدة أسبوع؟
- **Budget and Finance:** Budget and finance questions/instructions pertain to managing travel expenses, finding cost-effective options, and estimating overall travel costs.
  - **Example**: What are some tips for traveling on a budget in the Middle East?
- **الميزانية والمالية:** تتعلق أسئلة/تعليمات الميزانية والمالية بإدارة نفقات السفر، وإيجاد خيارات فعالة من حيث التكلفة، وتقدير تكاليف السفر الإجمالية.
  - **مثال**: ما هي بعض النصائح للسفر بميزانية محدودة في الشرق الأوسط؟
- **Transportation**: Transportation questions/instructions involve choosing the most suitable means of transportation, such as flights, trains, buses, or rental cars, for a particular trip.
  - **Example**: What is the most convenient way to travel from ….. City to ……?
- **النقل**: أسئلة/تعليمات النقل تتضمن اختيار وسائل النقل الأنسب، مثل رحلات الطيران أو القطارات أو الحافلات أو تأجير السيارات لرحلة معينة.
  - **مثال**: ما هي أنسب طريقة للسفر من ….. مدينة إلى ……؟
- **Accommodation:** Accommodation questions/instructions focus on selecting and booking suitable accommodations, such as hotels, hostels, vacation rentals, or camping sites.
  - **Example**: What are some family-friendly hotels near Warner Bros. World in Abu Dhabi?
- **الإقامة**: تركز أسئلة/تعليمات الإقامة على اختيار وحجز أماكن الإقامة المناسبة، مثل الفنادق أو النزل أو إيجارات العطلات أو مواقع التخييم.
  - **مثال**: ما بعض الفنادق المناسبة للعائلات القريبة من عالم وارنر براذرز في أبو ظبي؟
- **Safety and Security:** Safety and security questions/instructions address concerns and precautions related to personal safety, health, and security while traveling.
  - **Example**: What are the essential safety tips for solo female travelers?
- **السلامة والأمن:** تتناول أسئلة/تعليمات السلامة والأمن المخاوف والاحتياطات المتعلقة بالسلامة الشخصية والصحة والأمن أثناء السفر.
  - **مثال**: ما هي نصائح السلامة الأساسية للمسافرات المنفردات؟
- **Cultural and Local Experience:** Cultural and local experience questions/instructions involve immersing oneself in the local culture, traditions, cuisine, and customs of a destination.
  - **Example**: What are some authentic local experiences in …., …..?
- **الخبرة الثقافية والمحلية:** تتضمن أسئلة/تعليمات الخبرة الثقافية والمحلية الانغماس في الثقافة والتقاليد والمأكولات والعادات المحلية للوجهة.
  - **مثال**: ما هي بعض التجارب المحلية الأصيلة في ….، …..؟
- **Travel Tips and Recommendations:** Travel tips and recommendations questions/instructions seek advice and suggestions from experienced travelers or locals regarding specific destinations or travel-related matters.
  - **Example**: What are some off-the-beaten-path attractions to explore in ……, …….?
- **نصائح وتوصيات السفر:** أسئلة/تعليمات نصائح وتوصيات السفر تطلب المشورة والاقتراحات من المسافرين ذوي الخبرة أو السكان المحليين فيما يتعلق بوجهات محددة أو المسائل المتعلقة بالسفر.
  - **مثال:** ما هي بعض المعالم السياحية البعيدة عن المسار التي يمكنك استكشافها في .........، .........؟

#### Instruction could be, but not limited to, the following

- **What is an important landmark** to visit in….
- **ما هو المعلم** المهم الذي يجب زيارته في....
- **Tell me how** to plan a week visit for …..
- **أخبرني** كيف أخطط زيارة لمدة أسبوع ل....
- **Suggest an activity** to do when visiting ………..
- **اقترح نشاطًا** يمكنك القيام به عند زيارة …………
- **Is xxx located** in ………..city?
- **هل يقع موقع** ……….في مدينة ………?
- **Design a weekly plan** for staying at ………..city so that I could visit most of the essential landmarks and try local dishes
- **صمم خطة أسبوعية** للإقامة في مدينة …..، حتى أتمكن من زيارة معظم المعالم المهمة وتجربة الأطباق المحلية
- **Write a guidebook for tourists** interested in experiencing adventure sports in ……….., such as surfing, hiking, and desert trekking, providing information on the best locations, equipment, and safety guidelines.
- **قم بكتابة دليل إرشادي** للسياح المهتمين بتجربة رياضات المغامرة في ………… مثل ركوب الأمواج والمشي لمسافات طويلة والرحلات الصحراوية، مع توفير معلومات عن أفضل المواقع والمعدات وإرشادات السلامة.
- **Write a travel guide to food** in …….., highlighting must-visit restaurants, cafes, and markets known for authentic ………..cuisine. Include recommendations for dishes to try and any local food customs or etiquette to be aware of.
- **قم بكتابة دليل سفر للطعام** في …….. مع تسليط الضوء على المطاعم والمقاهي والأسواق المشهورة بمأكولات ……….. الأصيلة. قم بتضمين توصيات بشأن الأطباق التي يمكنك تجربتها وأي عادات أو آداب طعام محلية يجب أن تكون على دراية بها.

#### Examples

**Example 1**

| **Instruction** | ما هي الشواطئ الجميلة التي يمكن زيارتها في مدينة الرباط؟ |
| --- | --- |
| **Input** |     |
| **Output** | ذا كُنت تنوي قريبًا السياحة في الرباط المغرب، فلا يفوتك أبدًا وضع شواطئ الرباط الجميلة ضمن برنامجك السياحي بالمدينة، فيما يلي تعرف على 7 من شواطئ الرباط الجميلة التي نقترح عليك زيارتها…<br><br>شاطئ الصخيرات<br><br>شاطئ تمارة<br><br>شاطئ الاوداية<br><br>شاطئ الرباط<br><br>شاطئ الأمم<br><br>شاطئ الرمال الذهبية<br><br>شاطئ سيد العابد<br><br>شاطئ المهربين |
| **Source** | <https://www.travellwd.com/top-beaches-in-rabat/> |

####

**Example 2**

| **Instruction** | ما هي الأنشطة الترفيهية الممتعة التي يمكن القيام بها في مدينة طرابلس |
| --- | --- |
| **Input** |     |
| **Output** | طرابلس، هي عاصمة ليبيا وإحدى أقدم المدن، بها واحدة من الوجهات السياحية الشاملة، إليك أفضل أماكن السياحة في طرابلس ليبيا.<br><br>تجمع طرابلس بين التاريخ العريق والثقافة الغنية والجمال الطبيعي الخلاب لذلك تجذب العديد من السياح إليها سنويًا، وتشتهر طرابلس بماضيها العريق الذي يمتد إلى آلاف السنوات، حيث تُعد مركزًا حضريًا يجمع بين التأثيرات العربية والرومانية والعثمانية، مما يمنحها سحرًا فريدًا يستقطب الزوار من جميع أنحاء العالم.<br><br>بالإضافة إلى تراثها التاريخي تتميز طرابلس بمناظرها الطبيعية الخلابة وشواطئها الرملية الجميلة التي تجعلها وجهة مثالية لمحبي الاستجمام.<br><br>فإذا كنت تود زيارة أماكن السياحة في ليبيا ابدأ بالعاصمة طرابلس واستكشف الأماكن السياحية وأفضل الفعاليات السياحية في طرابلس، والأسواق التقليدية لشراء الحرف اليدوية. |
| **Source** | <https://al-ain.com/article/places-tourism-tripoli-libya> |

**Example 3**

| **Instruction** | اقترح مدينة في المغرب لقضاء العطلة الصيفية بها. |
| --- | --- |
| **Input** |     |
| **Output** | إذا كنت تخطط لرحلتك الأولى إلى المغرب، من المحتمل أنك ستميل لزيارة المواقع الأكثر شهرة في البلاد؛ بما في ذلك الأسواق المزدحمة في مراكش، المساجد التاريخية في فاس، البحر اللانهائي من الكثبان الرملية الذهبية في الصحراء، أو تذهب للاستمتاع بالمناظر الطبيعية الجبلية في الأطلس الكبير، إلا أن المغرب يضم أيضا 1،200 ميلا من السواحل المذهلة، فضلا عن موانئ ساحرة، وبلدات شاطئية خلابة تستحق الاكتشاف، من ضمنها الصويرة وميرلفت |
| **Source** | <https://news.travelerpedia.net/%D8%A7%D9%84%D9%85%D8%BA%D8%B1%D8%A8/%D8%A3%D8%AC%D9%85%D9%84-%D9%85%D8%AF%D9%86-%D8%A7%D9%84%D9%85%D8%BA%D8%B1%D8%A8-%D8%A7%D9%84%D8%B3%D8%A7%D8%AD%D9%84%D9%8A%D8%A9/> |

####

**Example 4**

| **Instruction** | صمم خطة ليوم للإقامة في مدينة القاهرة، حتى أتمكن من زيارة معظم المعالم المهمة وتجربة الأطباق المحلية |
| --- | --- |
| **Input** |     |
| **Output** |     |
| **Source** |     |

### Celebrations (Can be country specific or general)

Here we would like to construct instructions related to celebrations domain for a specific country, we are interested in cultural celebrations, national holidays,..etc.

#### Possible subtopics include but aren’t limited to

- **Traditional Celebrations**
  - Religious, Spiritual, festivals, or Cultural celebrations/festivals
  - **احتفالات/مهرجانات** دينية أو روحية أو مهرجانات أو ثقافية
- **National celebrations, Holidays**
- **الأعياد الوطنية،** الأعياد, الاجازات
- **Casual Gatherings**
- **Outdoor Events**
  - Picnic, Beach Day
- **Adventurous Outings**
  - Memorial Trip
- **Ceremonies, Parades, Concerts, music, Performances**
- **الاحتفالات، المسيرات**، الحفلات الموسيقية، الموسيقى، العروض
- **Planning and Preparation:** Planning and preparation questions /instructions involve organizing and arranging the logistics, details, and elements of the celebration.
  - **Example**: which is the best place to celebrate new year
- **التخطيط والإعداد:** تتضمن أسئلة/تعليمات التخطيط والإعداد تنظيم وترتيب الخدمات اللوجستية والتفاصيل وعناصر الاحتفال.
  - **مثال**: ما هو أفضل مكان للاحتفال بالعام الجديد
- **Theme and Decoration:** Theme and decoration questions/instructions pertain to selecting a theme or concept for the celebration and choosing appropriate decorations to enhance the ambiance.
  - **Example**: What are some creative decoration ideas for a ……..?
- **الموضوع والديكور:** تتعلق أسئلة/تعليمات الموضوع والديكور باختيار موضوع أو مفهوم للاحتفال واختيار الديكورات المناسبة لتعزيز الأجواء.
  - **مثال**: ما هي بعض أفكار الديكور الإبداعية لـ ……..؟
- **Food and Beverage:** Food and beverage questions/instructions focus on selecting the menu, catering options, and beverages that will be served during the celebration.
  - **Example**: What are some popular dishes to include in a Ramadan Iftar menu?
- **الأطعمة والمشروبات:** تركز أسئلة/تعليمات الأطعمة والمشروبات على اختيار القائمة وخيارات تقديم الطعام والمشروبات التي سيتم تقديمها خلال الاحتفال.
  - **مثال**: ما هي بعض الأطباق الشعبية التي يجب تضمينها في قائمة إفطار رمضان؟
- **Entertainment and Activities:** Activities questions/instructions involve planning and organizing entertainment options, games, or performances to engage guests and create a lively atmosphere.
  - **Example**: What are some fun activities to include in a children's birthday party?
- **الترفيه والأنشطة:** تتضمن أسئلة/تعليمات الأنشطة تخطيط وتنظيم خيارات الترفيه أو الألعاب أو العروض لإشراك الضيوف وخلق جو مفعم بالحيوية.
  - **مثال**: ما هي بعض الأنشطة الممتعة التي يجب تضمينها في حفلة عيد ميلاد الأطفال؟
- **Guest List and Invitations:** Guest list and invitations questions/instructions address determining the guest list, sending out invitations, and managing RSVPs.
  - **Example**: How can I create and send digital invitations for a graduation party?
- **قائمة الضيوف والدعوات:** عنوان أسئلة/تعليمات قائمة الضيوف والدعوات لتحديد قائمة الضيوف وإرسال الدعوات وإدارة الرد على الدعوات.
  - **مثال**: كيف يمكنني إنشاء وإرسال دعوات رقمية لحفل تخرج؟
- **Gift and Registry:** Gift and registry questions/instructions pertain to creating gift registries, suggesting gift ideas, or providing guidance to guests regarding appropriate gifts for the occasion.
  - **Example**: What are some popular items/gifts for children in Eid Mubarak? ?
- **الهدية والتسجيل:** تتعلق أسئلة/تعليمات الهدايا والتسجيل بإنشاء سجلات الهدايا، أو اقتراح أفكار الهدايا، أو تقديم التوجيه للضيوف فيما يتعلق بالهدايا المناسبة لهذه المناسبة.
  - **مثال**: ما هي بعض العناصر/الهدايا الشائعة للأطفال في عيد مبارك؟ ؟
- **Speeches:** Speeches questions/instructions involve preparing speeches to honor and celebrate the individual or occasion.
  - **Example**: How do I write a heartfelt speech for a retirement party?
- الخطب: أسئلة/تعليمات الخطب تتضمن إعداد الخطب لتكريم الفرد أو المناسبة والاحتفال بها.
- **Traditions and Rituals:** Traditions and rituals questions/instructions address incorporating specific cultural or traditional customs and rituals into the celebration.
  - **Example**: What are some traditional customs to include in an Islamic New Year celebration?
- **التقاليد والطقوس:** تتناول أسئلة/تعليمات التقاليد والطقوس دمج عادات وطقوس ثقافية أو تقليدية معينة في الاحتفال.
  - **مثال**: ما هي بعض العادات التقليدية التي يجب تضمينها في الاحتفال بالعام الهجري الجديد؟
- **Cultural and Religious Significance**: Cultural and religious significance questions/instructions focus on understanding and incorporating specific cultural or religious elements into the celebration.
  - **Example**: What are some traditional dances and music that can be included in a ……… ceremony?
- **الأهمية الثقافية والدينية:** تركز الأسئلة/التعليمات ذات الأهمية الثقافية والدينية على فهم ودمج عناصر ثقافية أو دينية محددة في الاحتفال.
  - **مثال**: ما هي بعض الرقصات والموسيقى التقليدية التي يمكن تضمينها في حفل ..........؟
- **Timeline and Schedule:** Timeline and schedule questions/instructions involve creating a timeline or schedule for the celebration, including the sequence of events and the timing of various activities.
  - **Example**: create a detailed timeline to ensure participating in all events in …….cermony/festive/party in ………
- **الجدول الزمني والجدول الزمني: ت**تضمن أسئلة/تعليمات الجدول الزمني والجدول الزمني إنشاء جدول زمني أو جدول زمني للاحتفال، بما في ذلك تسلسل الأحداث وتوقيت الأنشطة المختلفة.
  - **مثال**: انشاء جدول زمني مفصل لضمان المشاركة في جميع الفعاليات في حفلة……….. في ………
- **Dress Code and Attire:** Dress code and attire questions/instructions address selecting appropriate attire or establishing a specific dress code for the celebration.
  - **Example**: What should the dress code be for a formal gala event?
- **قواعد اللباس والملابس:** تتعلق الأسئلة/التعليمات المتعلقة بقواعد اللباس والملابس باختيار الملابس المناسبة أو تحديد قواعد لباس محددة للاحتفال.
  - **مثال**: ما هي قواعد اللباس التي يجب أن تكون في حفل رسمي؟
- **National celebrations and holidays:** questions/instructions involve gathering information about different national holidays, the timeline of national holidays, their importance, historical background, and how it’s celebrated.
  - **Example**: What are the most popular holidays in Algeria?
- **الاحتفالات والأعياد الوطنية:** تتضمن الأسئلة/التعليمات الاستعلام عن جمع معلومات حول الجدول الزمني للأعياد الوطنية وأهميتها وخلفيتها التاريخية وكيفية الاحتفال بها.
  - مثال: ما هي أشهر الاحتفالات الوطنيه في الجزائر؟
- **Ceremonies, Parades, Concerts, music, Performances, festivals:** questions/instructions involves querying about the timeline of a certain event to be held in a specific country or city, when to be held, what it is about, how to reserve/attend an event, previous year information
  - **Example**: List the date where ….. might take place in ……..
- **الاحتفالات، المسيرات، الحفلات الموسيقية، الموسيقى، العروض، المهرجانات:** أسئلة/تعليمات تتضمن الاستعلام عن الجدول الزمني لحدث معين سيعقد في بلد أو مدينة معينة، متى سيعقد، موضوعه، كيفية الحجز/الحضور الحدث، معلومات العام السابق.
  - **مثال**: اذكر التاريخ الذي قد يحدث فيه ........ في ...........

#### Instructions could be, but not limited to

- **Could you list** for me the festivals in ……..city to be held in October
- **هل يمكنك أن تذكر لي** المهرجانات التي ستقام في مدينة ………….في شهر أكتوبر؟
- **What are religious celebrations/festivals** in ……….country
- **ما هي الاحتفالات/الأعياد الدينية** في بلد ………
- **Which city** do you recommend to visit to celebrate ………
- **ما هي المدينة** التي تنصح بزيارتها للاحتفال بـ …………؟
- **اقترح مدينة** لزريارتها للاحتفال ب ……….
- **What is** …………holiday
- **ما هي عطلة** ……..
- **تكلم عن عيد** ………….
- **How do** people in ……………celebrate with …………
- **كيف يحتفل** الناس في ………….مع …………
- **List for me** popular dishes/food in ………… festival
- **أذكر لي الأطباق/الأطعمة** الشعبية في مهرجان ………
- **Is there xxx** parade in xxx country/city?
- **هل يوجد عرض** …………في بلد/مدينة …………
- **Where to find** ……………. concert in xxx and when will it happen?
- **أين يمكن العثور على** حفل ……………. في …………. ومتى سيحدث؟
- **Design a plan to** Host a Holiday Dinner Party
- **صمم خطة** لاستضافة حفل عشاء في العطلة
- **Plan** a road tip activities between ……. city and …… city
- **Provide a list of** dishes to cook over a beach party
- **قدم قائمة** بالأطباق التي يمكنك طهيها خلال حفلة على الشاطئ
- **How do** people celebrate ………….
- **كيف** يحتفل الناس بـ …………..
- **Prepare a list of** the best recreational activities in ……for families. Offer options such as parks, cultural events, theaters and amusement parks suitable for children and adults
- **أعد قائمة ب**أفضل الأنشطة الترفيهية في ……للعائلات. قدم خيارات مثل الحدائق والحدث الثقافية والمسارح والملاهي الترفيهية المناسبة للأطفال والكبار

#### Examples

**Example 1**

| **Instruction** | ما هي المهرجانات والأحداث الثقافية التي تجري في مدينة مراكش |
| --- | --- |
| **Input** |     |
| **Output** | المهرجانات والفعاليات الرئيسية المخطط لها في مراكش<br><br>الاجتماعات السنوية لعام 2023 لمجموعة البنك الدولي وصندوق النقد الدولي (IMF)<br><br>من 09 إلى 15 أكتوبر 2023<br><br>مهرجان مراكش الدولي للسينما<br><br>من 24 نوفمبر إلى 02 ديسمبر 2023<br><br>الإصدار الرابع عشر من معرض PURE Life Experiences Fair<br><br>من 10 إلى 13 سبتمبر 2023<br><br>بطولة العالم للجسر السادس والأربعين<br><br>من 20 أغسطس إلى 2 سبتمبر 2023<br><br>منتدى الأعمال "المغرب VIP B2B"<br><br>15 و 16 يونيو 2023<br><br>مهرجان النزوات<br><br>12 إلى 13 مايو 2023<br><br>افتتاح معرض Hubert Privé<br><br>السبت 29 أبريل 2023<br><br>مراكش<br><br>من 20 إلى 21 مايو 2023<br><br>الاحتفال بمئوية فندق المأمونية<br><br>من 01 إلى 08 أكتوبر 2023<br><br>الدورة 52 من المهرجان الوطني للفنون الشعبية<br><br>من 22 إلى 26 يونيو 2023 |
| **Source** | <https://visitmarrakech.com/ar/%D8%A5%D9%83%D8%AA%D8%B4%D9%81%D9%8A/?type=evenements&filtre-events=top-events> |

**Example 2**

| **Instruction** | أعد قائمة بأفضل الأنشطة الترفيهية في بيروت بلبنان للعائلات. قدم خيارات مثل الحدائق والملاهي الترفيهية المناسبة للأطفال |
| --- | --- |
| **Input** |     |
| **Output** | لبنان تضم عدد كبير من المتنزهات والحدائق التي تكون أصلا تمثل طبيعة لبنان الخضراء فكل ما يسر عينك تجده من خلال اجمل الأماكن السياحية والمتنزهات اللبنانية التي يمارس فيها الاطفال اجمل النشاطات الترفيهيه في لبنان. بذلك تكون السياحة في لبنان تأخذ طابع اصاله وهدوء من نوع خاص بين ارضها الخضراء. فيمكن التجول بين حدائق لبنان ورؤية الجمال.<br><br>حديقة السيوفي في بيروت<br><br>حديقة الصنائع في ميدان الحمرا<br><br>حديقة حرش بيروت<br><br>يوجد المدن الترفيهية الجميلة في لبنان فيها الألعاب والملاهي الحديثة جدا والتي تناسب جميع الاعمار من سن ثلاثة سنوات الي خمسين سنة استرجع طفولتك وادخل عالم المرح وعيش اجمل حياه مع نشاطات ترفيهية في لبنان.<br><br>دون فوكس بارك " Don Fox Park "<br><br>كيدزموندا " Kidzmondo "<br><br>ديد لاند هانتد وودز " Dead Land Haunted Woods " |
| **Source** | <https://www.tourism-travels.com/2019/02/Places-entertainment-children-Lebanon-parks-playgrounds.html> |

####

**Example 3**

| **Instruction** | صمم خطة لاستضافة حفل عشاء في العطلة في مصر |
| --- | --- |
| **Input** |     |
| **Output** |     |
| **Source** |     |

**Example 4**

| **Instruction** | تكلم عن احتفال شم النسيم |
| --- | --- |
| **Input** |     |
| **Output** |     |
| **Source** |     |

### Fauna, flora, and environmental life (Can be country-specific or general)

#### Description

Country-specific. Relates to the local ecosystem of the region.

#### Possible subtopics

- **Native species**
- **National parks & reserves**
- **المتنزهات والمحميات الوطنية**
- **Marine life**
- **الحياة البحرية**
- **Traditional uses (e.g. of plants)**
- **Climate**
- **المناخ**
- **Sea surfaces**
- **الأسطح البحرية**
- **Oasis**
- **واحات**
- **Agriculture, seasons**
- **الزراعة واستخدام الأراضي و المواسم الزراعيه**
- **Biodiversity**
- **التنوع البيولوجي**
- **Ecosystems**
- **النظم البيئية**
- **Preserving the environment**
- **الحفاظ على البيئة**
- **Environmental policies and regulations**
- **السياسات واللوائح البيئية**
- **Natural Resources**
- **الموارد الطبيعية**
- **Environmental challenges**
- **تحديات بيئية**
- **Species Identification:** Species identification questions/instructions involve identifying specific plants, animals, or organisms in the natural environment.
  - **Examples:**
    - What bird species is known for its distinct red crest and melodious song?(General)
    - I would like to know how to identify common bird species in natural reserves in Egypt. (Country specific)
- **تحديد الأنواع:** تتضمن أسئلة/تعليمات تحديد الأنواع تحديد نباتات أو حيوانات أو كائنات حية محددة في البيئة الطبيعية.
  - **أمثلة**:
    - ما هي أنواع الطيور المعروفة بعرفها الأحمر المميز وأغنيتها الشجية؟
    - أود معرفة كيفية التعرف على أنواع الطيور الشائعة في المحميات الطبيعية بمصر.
- **Habitat and Ecosystem:** Habitat and ecosystem questions/instructions focus on understanding the specific environments, ecosystems, and habitats where different species thrive.
  - **Examples**
    - What are the key characteristics of a coral reef ecosystem? (General)
    - What are the main characteristics of the ecosystem in the Sahara desert, and how do animals adapt to this environment? (Country specific)
- **الموئل والنظام البيئي:** تركز أسئلة/تعليمات الموئل والنظام البيئي على فهم البيئات والأنظمة البيئية والموائل المحددة التي تزدهر فيها الأنواع المختلفة.
  - **أمثلة**:
    - ما هي الخصائص الرئيسية للنظام البيئي للشعاب المرجانية؟
    - ما هي الخصائص الرئيسية للنظام البيئي في الصحراء الكبرى وكيف تتكيف الحيوانات مع هذه البيئة؟
- **Conservation and Preservation:** Conservation and preservation questions/instructions address strategies and actions to protect and conserve endangered species, habitats, and ecosystems.
  - **Examples**
    - What are some effective conservation measures to protect sea turtle nesting sites? (General)
    - What strategies are used to protect the Arabian leopard from extinction in the Arabian Peninsula? (Country specific)
- **الحفظ والحفظ:** تتناول أسئلة/تعليمات الحفظ والحفظ الاستراتيجيات والإجراءات الرامية إلى حماية وحفظ الأنواع والموائل والنظم البيئية المهددة بالانقراض.
  - **أمثلة**:
    - ما هي بعض تدابير الحفظ الفعالة لحماية مواقع تعشيش السلاحف البحرية؟
    - ما هي الاستراتيجيات المُستخدمة لحماية الفهد العربي من الانقراض في شبه الجزيرة العربية؟
- **Life Cycle and Reproduction:** Life cycle and reproduction questions involve understanding the reproductive processes, life stages, and behaviors of various organisms.
  - **Examples:**
    - How do butterflies undergo metamorphosis from caterpillars to adults? (General)
    - I want to understand the life cycle of the palm tree and how it reproduces in the Middle East environment. (Country specific)
- **دورة الحياة والتكاثر:** تتضمن أسئلة دورة الحياة والتكاثر فهم العمليات الإنجابية ومراحل الحياة وسلوكيات الكائنات الحية المختلفة.
  - **أمثلة**:
    - كيف تخضع الفراشات للتحول من اليرقات إلى البالغة؟
    - أرغب في فهم دورة حياة شجرة النخيل وكيفية تكاثرها في بيئة الشرق الأوسط.
- **Environmental Threats:** Environmental threats questions/instructions focus on identifying and addressing threats to the natural world, such as pollution, deforestation, climate change, or invasive species.
  - **Examples:**
    - What are the main causes of habitat destruction in rainforests? (General)
    - How can the problem of desertification in arid areas of Arab countries be addressed and its impact on the environment be mitigated? (Country specific)
- **التهديدات البيئية:** تركز أسئلة/تعليمات التهديدات البيئية على تحديد ومعالجة التهديدات التي يتعرض لها العالم الطبيعي، مثل التلوث أو إزالة الغابات أو تغير المناخ أو الأنواع الغازية.
  - **أمثلة**:
    - ما هي الأسباب الرئيسية لتدمير الموائل في الغابات المطيرة؟
    - كيف يمكن التصدي لمشكلة التصحر في المناطق الجافة بالدول العربية والحد من تأثيرها على البيئة؟
- **Adaptations and Survival Strategies:** Adaptations and survival strategies questions/instructions pertain to the unique characteristics and behaviors that help organisms adapt and survive in their respective environments.
  - **Examples:**
    - How do desert plants adapt to survive in arid conditions? (General)
    - I would like to know how camels adapt to the harsh conditions in the Sahara desert. (Country specific)
- **استراتيجيات التكيف والبقاء:** تتعلق أسئلة/تعليمات التكيفات واستراتيجيات البقاء بالخصائص والسلوكيات الفريدة التي تساعد الكائنات الحية على التكيف والبقاء على قيد الحياة في بيئاتها الخاصة.
  - **أمثلة**:
    - كيف تتكيف النباتات الصحراوية للبقاء على قيد الحياة في الظروف القاحلة؟
    - أود معرفة كيف تتكيف الجمال مع الظروف القاسية في الصحراء الكبرى.
- **Biodiversity and Ecosystem Services:** Biodiversity and ecosystem services questions/instructions explore the importance of diverse species and ecosystems in providing essential services, such as pollination, water purification, and carbon sequestration.
  - **Examples:**
    - What are the ecological benefits of preserving wetlands? (General)
    - What is the role of coral reefs in the Red Sea in supporting biodiversity and how do they contribute to water purification? (Country specific)
- **خدمات التنوع البيولوجي والنظام البيئي:** تستكشف أسئلة/تعليمات خدمات التنوع البيولوجي والنظام البيئي أهمية الأنواع والأنظمة البيئية المتنوعة في توفير الخدمات الأساسية، مثل التلقيح وتنقية المياه وعزل الكربون.
  - **أمثلة**:
    - ما هي الفوائد البيئية للحفاظ على الأراضي الرطبة؟
    - ما هو دور الشعاب المرجانية في البحر الأحمر في دعم التنوع البيولوجي وكيف تساهم في تنقية المياه؟
- **Environmental Education and Awareness:** Environmental education and awareness questions/instructions involve learning about environmental issues, promoting sustainability, and fostering a connection with nature.
  - **Examples:**
    - How can we raise awareness about the importance of recycling in our community? (General)
    - How can environmental awareness among school students in the UAE be enhanced regarding the importance of recycling? (Country specific)
- **التثقيف والتوعية البيئية:** تتضمن أسئلة/تعليمات التثقيف والتوعية البيئية التعرف على القضايا البيئية وتعزيز الاستدامة وتعزيز الاتصال بالطبيعة.
  - **أمثلة**:
    - كيف يمكننا رفع مستوى الوعي حول أهمية إعادة التدوير في مجتمعنا؟
    - كيف يمكن تعزيز الوعي البيئي بين طلاب المدارس في الإمارات العربية المتحدة حول أهمية إعادة التدوير؟
- **Ethical Considerations:** Ethical considerations questions/instructions address the moral and ethical dimensions of interactions with flora, fauna, and the environment, including topics like animal welfare, sustainable practices, and responsible tourism.
  - **Examples:**
    - What are the ethical implications of using animals in scientific research? (General)
    - What are the ethical considerations to be taken into account when interacting with wildlife during eco-tourism? (General)
- **الاعتبارات الأخلاقية:** تتناول أسئلة/تعليمات الاعتبارات الأخلاقية الأبعاد الأخلاقية والأخلاقية للتفاعلات مع النباتات والحيوانات والبيئة، بما في ذلك موضوعات مثل رعاية الحيوان والممارسات المستدامة والسياحة المسؤولة.
  - **أمثلة**:
    - ما هي الآثار الأخلاقية لاستخدام الحيوانات في البحث العلمي؟
    - ما هي الاعتبارات الأخلاقية التي يجب أخذها في الاعتبار عند التفاعل مع الحياة البرية أثناء السياحة البيئية؟
- **Ecological Interactions:** Ecological interaction questions/instructions address the complex relationships between different species in an ecosystem, such as predator-prey dynamics, symbiotic relationships, and food webs.
  - **Examples:**
    - How do bees and flowers engage in a mutually beneficial relationship through pollination? (General)
    - How do plants and animals interact in a desert oasis, and what are the key food relationships present there? (General)
- **التفاعلات البيئية:** تتناول أسئلة/تعليمات التفاعل البيئي العلاقات المعقدة بين الأنواع المختلفة في النظام البيئي، مثل ديناميكيات المفترس والفريسة، والعلاقات التكافلية، والشبكات الغذائية.
  - **أمثلة**:
    - كيف ينخرط النحل والزهور في علاقة متبادلة المنفعة من خلال التلقيح؟
    - كيف تتفاعل النباتات والحيوانات في واحة الصحراء، وما هي أهم العلاقات الغذائية الموجودة هناك؟
- **Plant and Animal Behavior:** Plant and animal behavior questions/instructions involve studying the behaviors and patterns exhibited by different species, including migration, foraging, mating rituals, and territoriality.
  - **Examples:**
    - How do humpback whales communicate with each other during their annual migration? (General)
    - I am interested in studying the behavior of migratory birds in the Mediterranean region and how climate changes affect their migration paths. (Specific)
- **سلوك النبات والحيوان:** تتضمن أسئلة/تعليمات سلوك النبات والحيوان دراسة السلوكيات والأنماط التي تظهرها الأنواع المختلفة، بما في ذلك الهجرة والبحث عن الطعام وطقوس التزاوج والإقليمية.
  - **أمثلة**:
    - كيف تتواصل الحيتان الحدباء مع بعضها البعض أثناء هجرتها السنوية؟
    - أرغب في دراسة سلوك الطيور المهاجرة في منطقة البحر المتوسط وكيفية تأثير التغيرات المناخية على مساراتها.
- **Indigenous Knowledge and Traditional Practices:** Indigenous knowledge and traditional practices questions/instructions explore the wisdom and practices of indigenous cultures in relation to flora, fauna, and the environment.
  - **Example:** What are some traditional uses of medicinal plants by indigenous communities? (General)
- **معارف السكان الأصليين والممارسات التقليدية:** تستكشف الأسئلة/التعليمات الخاصة بمعارف السكان الأصليين والممارسات التقليدية حكمة وممارسات ثقافات السكان الأصليين فيما يتعلق بالنباتات والحيوانات والبيئة.
  - **مثال:** ما هي بعض الاستخدامات التقليدية للنباتات الطبية من قبل المجتمعات الأصلية؟
- **Citizen Science and Community Involvement:** Citizen science and community involvement questions/instructions focus on engaging the public in scientific research, data collection, and conservation initiatives to foster a sense of stewardship.
  - **Examples:**
    - How can individuals contribute to bird population monitoring through citizen science projects? (General)
    - What are the ways in which individuals can contribute to data collection on biodiversity in their area? (General)
- **علوم المواطن وإشراك المجتمع:** تركز أسئلة/تعليمات علوم المواطن والمشاركة المجتمعية على إشراك الجمهور في البحث العلمي، وجمع البيانات، ومبادرات الحفظ لتعزيز الشعور بالإدارة.
  - **أمثلة**:
    - كيف يمكن للأفراد المساهمة في مراقبة أعداد الطيور من خلال المشاريع العلمية للمواطنين؟
    - ما هي الطرق التي يمكن بها للأفراد المساهمة في جمع البيانات حول التنوع البيولوجي في منطقتهم؟
- **Environmental Policy and Advocacy:** Environmental policy and advocacy questions/instructions address the development and implementation of policies and initiatives to protect and sustainably manage natural resources.
  - **Examples:**
    - What are some key policies aimed at reducing greenhouse gas emissions and combating climate change? (General)
    - How can awareness be raised about the importance of water conservation policies in arid regions like North Africa? (Country specific)
- **السياسة البيئية والدعوة:** تتناول أسئلة/تعليمات السياسة البيئية والدعوة تطوير وتنفيذ السياسات والمبادرات لحماية الموارد الطبيعية وإدارتها بشكل مستدام.
  - **أمثلة**:
    - ما هي بعض السياسات الرئيسية التي تهدف إلى الحد من انبعاثات الغازات الدفيئة ومكافحة تغير المناخ؟
    - كيف يمكن التوعية بأهمية سياسات الحفاظ على المياه في المناطق الجافة مثل شمال إفريقيا؟
- **Nature Conservation and Protected Areas:** Nature conservation and protected areas questions/instructions involve understanding the establishment and management of national parks, nature reserves, and other protected areas for biodiversity conservation.
  - **Examples:**
    - What are the benefits of establishing marine protected areas for coral reef conservation? (General)
    - What are the management strategies for nature reserves in Oman, and how do they contribute to biodiversity protection? (Country specific)
- **الحفاظ على الطبيعة والمناطق المحمية:** تتضمن أسئلة/تعليمات الحفاظ على الطبيعة والمناطق المحمية فهم إنشاء وإدارة المتنزهات الوطنية والمحميات الطبيعية والمناطق المحمية الأخرى للحفاظ على التنوع البيولوجي.
  - **أمثلة**:
    - ما هي فوائد إنشاء مناطق بحرية محمية للحفاظ على الشعاب المرجانية؟
    - ما هي استراتيجيات إدارة المحميات الطبيعية في سلطنة عمان وكيف تسهم في حماية التنوع البيولوجي؟
- **Restoration Ecology and Habitat Rehabilitation:** Restoration ecology and habitat rehabilitation questions/instructions focus on restoring degraded ecosystems and habitats through active interventions and ecological restoration techniques.
  - **Examples:**
    - How can we restore a deforested area and encourage the return of native plant and animal species? (General)
    - I am interested in knowing effective methods for rehabilitating damaged grasslands in the Levant region and restoring them to their natural state. (General)
- **استعادة البيئة وإعادة تأهيل الموائل:** تركز أسئلة/تعليمات استعادة البيئة وإعادة تأهيل الموائل على استعادة النظم البيئية والموائل المتدهورة من خلال التدخلات النشطة وتقنيات الاستعادة البيئية.
  - **أمثلة**:
    - كيف يمكننا استعادة منطقة أزيلت منها الغابات وتشجيع عودة الأنواع النباتية والحيوانية المحلية؟
    - أرغب في معرفة الطرق الفعالة لإعادة تأهيل المراعي المتضررة في منطقة الشام وإعادتها إلى حالتها الطبيعية.
- **Ecotourism and Nature-Based Recreation:** Ecotourism and nature-based recreation questions/instructions explore sustainable tourism practices that promote natural appreciation, support local communities, and minimize negative environmental impacts.
  - **Examples:**
    - What are some ecotourism activities that allow visitors to observe wildlife without disturbing their natural behaviors? (General)
    - What are the best practices for developing ecotourism in the Red Sea area while maintaining environmental balance? (Country specific)
- **السياحة البيئية والترفيه القائم على الطبيعة:** تستكشف أسئلة/تعليمات السياحة البيئية والترفيه القائم على الطبيعة ممارسات السياحة المستدامة التي تعزز التقدير الطبيعي، وتدعم المجتمعات المحلية، وتقلل من الآثار البيئية السلبية.
  - **أمثلة**:
    - ما هي بعض أنشطة السياحة البيئية التي تسمح للزوار بمراقبة الحياة البرية دون الإخلال بسلوكياتهم الطبيعية؟
    - ما هي أفضل الممارسات لتطوير السياحة البيئية في منطقة البحر الأحمر مع الحفاظ على التوازن البيئي؟

#### Specific guidelines

- **Fauna:** Describe appearance, habitat, and migration pattern (if any)
- **Flora:** Describe appearance, location, and traditional use (if any)

#### Instructions could be, but are not limited to

- **Define** …..
  - Define the concept of ………….
- **عرِّف**
  - عرِّف مفهوم ..........
- **List** ……
  - Create a comprehensive list of native plant and animal species found in the ………, categorizing them by ecosystem and highlighting any endangered or endemic species.
- **أعطني قائمة**
  - إنشئ قائمة شاملة بأنواع النباتات والحيوانات المحلية الموجودة في .........، وتصنيفها حسب النظام البيئي وتسليط الضوء على أي أنواع مهددة بالانقراض أو مستوطنة.
- **Suggest** ……
  - Propose conservation strategies for protecting the biodiversity in ……, considering factors such as …….,...........,.................,.............
- **اقترح** ……
  - اقترح إستراتيجيات الحفاظ على التنوع البيولوجي في …… مع الأخذ في الاعتبار عوامل مثل ……...........،................... ............
- **Describe** …….
  - Describe the Impacts of Climate Change on………………………….
- **صف** …….
  - صف آثار تغير المناخ على ............................
- **What is** ……
  - What Is the Ecological Importance of Coral Reefs in ……………………
- **ما هو/هي** ……
  - ما هي الأهمية البيئية للشعاب المرجانية في ...............
- **How** ………
  - How to Create Wildlife-Friendly Gardens in………………
- **كيف** ………
  - كيفية إنشاء حدائق صديقة للحياة البرية في ...............
- **Compare**
  - Compare and contrast the adaptations of desert plants and mountain plants in ………………..
- **قارن ب**
  - قارن بين تكيفات النباتات الصحراوية والنباتات الجبلية في ...............
- **Provide**……
  - provide examples of ……………. in …………………
- **قم بتقدم/ قدًم** ……
  - تقديم أمثلة على …………. في …………………
- **Explain**……
  - Provide a detailed explanation of the ……………. in ………….., highlighting the ……………, their role in……………, and their significance for……………………
- **أشرح**……
  - تقديم شرح مفصل عن ........... في ………….. مع تسليط الضوء على ………… ودورها في ………… وأهميتها بالنسبة لـ…………………
- **Which of the following statements is True**
  - …………….
  - ……………….
  - …………..
- **أي من العبارات التالية صحيحة**
  - ………….
  - ……………
  - …………..

#### Examples

**Example 1**

| **Instruction** | اعطني ثلاث أمثلة محميات التراث العالمي في مصر |
| --- | --- |
| **Input** |     |
| **Output** | محمية محمية رأس محمد من محميات التراث العالمي<br><br>محمية جزر تيران وصنافير من محميات التراث العالمي<br><br>محمية سانت كاترين من محميات التراث العالمي |
| **Source** | <https://www.wikiwand.com/ar/%D8%A7%D9%84%D8%AD%D9%8A%D8%A7%D8%A9_%D8%A7%D9%84%D8%A8%D8%B1%D9%8A%D8%A9_%D9%81%D9%8A_%D9%85%D8%B5%D8%B2> |

####

**Example 2**

| **Instruction** | ما فائدة التنوع البيولوجي؟ |
| --- | --- |
| **Input** |     |
| **Output** | يتمتع بفوائد متعددة منها «قيمة استهلاكية»، حيث يُوفر التنوُّع البيولوجي الموجود فـي النظام البيئي للسكان جميع احتياجاتهم اليومية، و«قيمة استخدام المنتج»، ويُوفر «التنوُّع الجيني» المدخل الأساسي فـي علم التكنولوجيا الحيوية، و«قيمة اجتماعية» فتوفر التنوع البيولوجي لسكان الأنظمة البيئية المختلفة سبل عيشهم وعاداتهم وتقاليدهم، وقيمة جمالية وأخلاقية. |
| **Source** | <https://www.elwatannews.com/news/details/6337191> |

**Example 3**

| **Instruction** | اكتب قائمة بالنظم البيئية في مصر |
| --- | --- |
| **Input** |     |
| **Output** | النظم البيئية في مصر:<br><br>١. النظام البيئي الصحراوي:<br><br>تغطي البيئات القاحلة وشبه القاحلة أكثر من 90% من أراضي مصر التي تضم نظم بيئية متباينة، مثل الصحراء الساحلية المتوسطية، والصحراء الغربية، التي تحتل حوالي ثلثي مساحة البلاد، وتعتبر الواحات أكثر السمات البارزة في الصحراء الغربية، وهي المصدر الوحيد للمياه والنباتات في معظم هذه المناطق الصحراوية، والصحراء المتاخمة للبحر الأحمر، المعروفة باسم الصحراء الشرقية، وهي جافة جداً، وتبلغ مساحتها حوالي 223 ألف كيلومتر مربع، والنباتات السائدة في هذه المنطقة معظمها محصور في مناطق مداخل الوديان الكبرى وعلى طول ساحل البحر الأحمر، حيث توجد المستنقعات المالحة، ومعظم النباتات المسجلة تقترن بالمعارف التقليدية في صحراء سيناء والساحل الشمالي والشرقي والغربي.<br><br>٢. النظام البيئي البحري:<br><br>تتميز النظم البيئية البحرية لكل من البحر الأبيض المتوسط والبحر الأحمر بالعديد من البيئات والأنواع المهددة بالانقراض، وخاصة جميع الثدييات البحرية، وتشمل 17 نوعاً، والسلاحف البحرية بواقع 4 أنواع، وأسماك القرش بأكثر من 20 نوعاً، وأشجار المانجروف، والعديد من الطيور، منها “النورس أبيض العين”، و”صقر الغروب”، و”العقاب النسارية”، بالإضافة إلى التنوع البيولوجي البحري الكبير، لأكثر من 5 آلاف نوع، ممثلة في 800 نوع من الطحالب والأعشاب البحرية، و209 أنواع من الشعاب المرجانية، وأكثر من 800 نوع من الرخويات، و600 نوع من القشريات، و350 نوعاً من الجلد شوكيات، بالإضافة إلى مئات الأنواع التي لم يتم اكتشافها حتى الآن.<br><br>٣. النظام البيئي للأراضي الرطبة:<br><br>تتمتع الأراضي الرطبة بوظائف بيولوجية وإيكولوجية حيوية، من خلال توفير بيئة مناسبة دائمة للعديد من مجموعات التنوع البيولوجي، وخاصة الطيور المائية المهاجرة، وتقع الأراضي الرطبة، أو البحيرات الساحلية المصرية، على طول ساحل دلتا النيل، ومنها “المنزلة، والبرلس، وإدكو، ومريوط”، وشرق قناة السويس، مثل “بور فؤاد، والبردويل”، وترتبط جميعها مباشرة بالبحر المتوسط، باستثناء بحيرة مريوط، وتمثل الحيوانات المائية للبحيرات الشمالية مزيجاً من أنواع المياه العذبة والأنواع البحرية، وتعتبر أنواع سمكة “البلطي”، التي تعيش في المياه العذبة، هي المصيد السائد في تلك المناطق، كما يسكن العديد من أنواع الأسماك النيلية هذه البحيرات، مثل “القراميط، والبني، وقشر البياض، والبياض النيلي، والمبروك”، كما توجد العديد من الأنواع البحرية المتحملة للمياه العذبة في بحيرات الدلتا، بما في ذلك أسماك “البوري، وموسى، والدنيس، والقاروص، ولوت، والحنشان والجمبرى”.<br><br>٤. النظام البيئي الزراعي:<br><br>أخذت بيئات الأراضي الزراعية في التقلص منذ أواخر الثمانينيات، ويعتقد أن هذه الانخفاضات مرتبطة بالتغير في استخدام الأراضي وتغير الممارسات الزراعية، كما أدى إدخال الأصناف ذات الإنتاجية العالية واستخدامها على نطاق واسع، إلى إهمال واختفاء الأصناف التقليدية، وتآكل التنوع الجيني النباتي للمحاصيل، وتعتمد مصر، حالياً، على 4 محاصيل رئيسية، هي “القمح، والذرة، والأرز، والبطاطس″، لتوفير 50% من غذائها النباتي، و14 نوعاً من الثدييات والطيور، لتوفير 90% من البروتينات الحيوانية.<br><br>٥. النظام البيئي للمراعي:<br><br>تُعتبر المراعي الموجودة في منطقة جبال “علبة، ووادي العلاقي” في الجنوب، وفي منطقتي “العميد” على البحر المتوسط، وسيناء في الشمال، أكثر مناطق المراعي في مصر، ويخضع استخدام هذه الموارد في كل من هذه المناطق لشيخ القبيلة، حيث يضع قواعد لاستغلال مياه الآبار، وقطع الأشجار المستخدمة في بناء المنازل أو الوقود.<br><br>٦. النظام البيئي الجبلي:<br><br>توجد البيئات الجبلية في عدة أماكن، منها “جنوب سيناء، والعوينات، والبحر الأحمر، وعلبة”، وتغطي حوالى 0.7% من إجمالي مساحة الأراضي المصرية، وتشتمل على أمثلة حصرية من التنوع البيولوجي النباتي والحيواني. |
| **Source** | <https://raednetwork.org/eg-biodiversity/> |

### Sports (Can be country specific or general)

هذا المجال يهتم بالرياضة بشكل عام و في البلدان العربية على وجه الخصوص. يمكننا التطرق في هذا المجال الى الألعاب الرياضية، بما في ذلك الرياضات الجماعية والرياضات الفردية والأنشطة الترفيهية، بالإضافة إلى الصناعات والمؤسسات والمنظمات المرتبطة بها التي تدعم وتنظم الأحداث الرياضية في بلد عربي محدد. بالاضافة الى ما سبق يمكننا التطرق الى الرياضات المشهورة عالميا و تاريخها و مشاهيرها على الصعيدين العربي و العالمي (مثل: كرة القدم، كأس العالم، ريال مدريد، بنزيما، أبو تريكة…).

The sports domain refers to the broad field that encompasses various activities, competitions, and forms of physical exercise that involve skill, athleticism, and organized play. It encompasses a wide range of sports, including team sports, individual sports, and recreational activities, as well as the associated industries, institutions, and organizations that support and regulate sporting events.

#### Possible subtopics could be but are not limited to

- **Popular sports in a given country**
- **الرياضات الشعبية في أي بلد**
  - أمثلة:
    - ما هي اللعبة الأكثر شعبية في مصر؟ (مصر)
    - ما هي اللعبة الأكثر شعبية في الهند؟ (عام)
- **Popular clubs for a given country**
  - General information about each sports league in each country
  - Name of players, general information, medals
- **الأندية الشعبية لأي بلد**
  - معلومات عامة عن كل الدوريات الرياضية في كل دولة
  - أسماء اللاعبين، معلومات عامة، الميداليات
  - أمثلة:
    - ما هو النادي الأكثر شعبية في مصر؟(مصر)
    - تحدث عن أكثر الأندية فوزا بالدوري المصري(مصر)
- **General information about sports in general:**
  - Rule of sports
  - How its played
  - History
  - Important tournaments
  - Name of famous players throughout history
- **معلومات عامة عن الرياضة بشكل عام:**
  - تحدث عن الهداف التاريخي لمنتخب مصر؟ (مصر)
  - من من المنتخبات التالية يعتبر الأكثر فوزا بكأس العالم؟(عام)
    - الأرجنتين، كندا، البرازيل؟
- **Popular sports:** Questions/instructions focus on important/popular sports and clubs in each country/city. Background of each club. Also, inquiring about each sports league in each country, medals/ tournaments achieved, names of famous players, and general information.
  - **Example:**
- **الرياضات الشعبية:** تركز الأسئلة/التعليمات على الرياضات والأندية المهمة/الشعبية في كل بلد/مدينة. خلفية كل نادي. وكذلك الاستعلام عن كل دوري رياضي في كل دولة، والميداليات/البطولات التي حققها، وأسماء اللاعبين المشهورين، ومعلومات عامة.
- **General Sports information:** Questions/instructions focus on rules of sports, how they are played, history, important tournaments, and names of famous players throughout history.
  - **Example**
- **معلومات رياضية عامة:** أسئلة/تعليمات تركز على قواعد الرياضة وكيفية لعبها وتاريخها والبطولات المهمة وأسماء اللاعبين المشهورين عبر التاريخ.
- **Performance:** Performance questions/instructions focus on understanding and improving an athlete's performance in their specific sport.
  - Example: How can a tennis player improve their backhand technique?
- **الأداء:** تركز أسئلة/تعليمات الأداء على فهم وتحسين أداء الرياضي في رياضته المحددة.
  - مثال: كيف يمكن للاعب التنس تحسين أسلوب الضربة الخلفية لديه؟
- **Strategy and Tactics:** Strategy and tactics questions/instructions involve analyzing and devising game plans, techniques and approaches to gain an advantage in a specific sport.
  - **Example:** What offensive strategy should a basketball team adopt to break through a strong defense?
- **الإستراتيجية والتكتيكات:** تتضمن أسئلة/تعليمات الإستراتيجية والتكتيكات تحليل ووضع خطط اللعبة والتقنيات والأساليب للحصول على ميزة في رياضة معينة.
  - **مثال:** ما هي الإستراتيجية الهجومية التي يجب أن يعتمدها فريق كرة السلة لاختراق الدفاع القوي؟
- **Training and Conditioning:** Training and conditioning questions/instructions pertain to the physical preparation and fitness of athletes for their sport.
  - **Example:** What are the best exercises and drills to improve speed and agility in soccer players?
- **التدريب والتكييف:** أسئلة/تعليمات التدريب والتكييف تتعلق بالإعداد البدني واللياقة البدنية للرياضيين لرياضتهم.
  - **مثال:** ما هي أفضل التمارين والتدريبات لتحسين السرعة والرشاقة لدى لاعبي كرة القدم؟
- **Rules and Regulations:** Rules and regulations questions/instructions involve understanding and interpreting the rules and regulations of a particular sport.
  - **Example:** What is the penalty for a handball violation in volleyball?
- **القواعد واللوائح:** تتضمن أسئلة/تعليمات القواعد واللوائح فهم وتفسير القواعد واللوائح الخاصة برياضة معينة.
  - **مثال:** ما هي عقوبة مخالفة كرة اليد في الكرة الطائرة؟
- **Injury Prevention and Rehabilitation:** Injury prevention and rehabilitation questions/instructions address techniques and practices to prevent injuries and promote recovery from sports-related injuries.
  - **Example:** What are the recommended exercises and treatments for rehabilitating a sprained ankle in a basketball player?
- **الوقاية من الإصابات وإعادة التأهيل:** تتناول أسئلة/تعليمات الوقاية من الإصابات وإعادة التأهيل التقنيات والممارسات اللازمة لمنع الإصابات وتعزيز التعافي من الإصابات المرتبطة بالرياضة.
  - **مثال:** ما هي التمارين والعلاجات الموصى بها لإعادة تأهيل التواء الكاحل لدى لاعب كرة السلة؟
- **Sports Psychology:** Sports psychology questions/instructions focus on the mental and emotional aspects of sports performance, including motivation, concentration, and managing pressure.
  - **Example:** How can a golfer improve their mental focus and concentration during a tournament?
- **علم النفس الرياضي:** تركز أسئلة/تعليمات علم النفس الرياضي على الجوانب العقلية والعاطفية للأداء الرياضي، بما في ذلك الدافع والتركيز وإدارة الضغط.
  - **مثال:** كيف يمكن للاعب الجولف تحسين تركيزه الذهني أثناء البطولة؟
- **Team Dynamics and Communication:** Team dynamics and communication questions/instructions involve understanding and improving teamwork, communication, and cohesion among team members.
  - **Example:** How can a soccer team improve their on-field communication and coordination?
- **ديناميكيات الفريق والتواصل:** تتضمن ديناميكيات الفريق وأسئلة/تعليمات الاتصال فهم وتحسين العمل الجماعي والتواصل والتماسك بين أعضاء الفريق.
  - **مثال:** كيف يمكن لفريق كرة القدم تحسين التواصل والتنسيق على أرض الملعب؟
- **Performance Analysis and Statistics:** Performance analysis and statistics questions/instructions involve analyzing performance data and statistics to identify strengths, weaknesses, and areas for improvement.
  - **Example:** What statistical metrics can be used to evaluate the effectiveness of a basketball player?
- **تحليل الأداء والإحصائيات:** تتضمن أسئلة/تعليمات تحليل الأداء والإحصائيات تحليل بيانات الأداء والإحصائيات لتحديد نقاط القوة والضعف ومجالات التحسين.
  - **مثال:** ما هي المقاييس الإحصائية التي يمكن استخدامها لتقييم فعالية لاعب كرة السلة؟
- **Sports Ethics and Fair Play:** Sports ethics and fair play questions/instructions explore the moral and ethical considerations in sports, including issues such as doping, sportsmanship, and fair competition.
  - **Example:** What are the ethical implications of using performance-enhancing drugs in professional sports?
- **تحليل الأداء والإحصائيات:** تتضمن أسئلة/تعليمات تحليل الأداء والإحصائيات تحليل بيانات الأداء والإحصائيات لتحديد نقاط القوة والضعف ومجالات التحسين.
  - **مثال:** ما هي الآثار الأخلاقية لاستخدام العقاقير المعززة للأداء في الألعاب الرياضية الاحترافية؟

#### Instruction could be, but not limited to

- **Define** ……….
  - What is Baseball?
- **عرًف** ………..
  - ما هي لعبة البيسبول؟
- **Explain the rules of** ………. game
  - Explain the rules and scoring system of a specific sport, such as basketball or soccer.
  - Research and create a timeline of the major events and achievements in the history of a particular sport, like tennis or cricket.
- **اشرح قواعد لعبة** ……………
  - اشرح القواعد ونظام التسجيل في رياضة معينة، مثل كرة السلة أو كرة القدم.
  - قم بالبحث وإنشاء جدول زمني للأحداث والإنجازات الكبرى في تاريخ رياضة معينة، مثل التنس أو الكريكيت.
- **Create** ……………
  - Create a training plan for improving performance in a specific sport, considering aspects such as strength, endurance, and agility.
- **قم بإنشاء** …………
  - قم بإنشاء خطة تدريبية لتحسين الأداء في رياضة معينة، مع الأخذ في الاعتبار جوانب مثل القوة والتحمل وخفة الحركة.
- **Design** …………
  - Design a fitness program tailored for athletes in a specific sport, focusing on exercises that enhance sport-specific skills and physical conditioning.
- **صمم** …………
  - صمم برنامج لياقة بدنية مصمم خصيصًا للرياضيين في رياضة معينة، مع التركيز على التمارين التي تعزز المهارات الخاصة بالرياضة واللياقة البدنية.
- **Write** ……………..
  - Write a report on the health benefits of participating in regular physical activities and sports.
- **اكتب** …………..
  - اكتب تقريرًا عن الفوائد الصحية للمشاركة في الأنشطة البدنية والرياضة المنتظمة.
- **Compare between** ……….. and …………..
  - Compare and contrast the equipment and gear used in two different sports, like baseball and golf.
- **قارن بين** ……………… و ……….
  - قارن بين المعدات والعتاد المستخدم في رياضتين مختلفتين، مثل البيسبول والجولف.
  - قارن بين عدد مرات فوز الأهلي و الزمالك بالبطولات المحلية و الافريقية(مصر)
  - قارن بين كريستيانو و ميسي(عام)
  - مالفرق بين كرة القدم الأمريكية و كرة القدم في باقي دول العالم؟
- **Give me rules/Instructions for** specific game
- **أعطني قواعد/تعليمات لعبة معينة**
- **Analyze the** gameplay strategies played by ………… team
- **قم بتحليل** استراتيجيات اللعب التي يلعبها فريق …………….
- **Organize**
  - Organize a sports event or tournament, outlining the necessary steps for scheduling matches, coordinating teams, and ensuring smooth execution of the event.
- **نظم**
  - نظم حدث رياضي أو بطولة، مع تحديد الخطوات اللازمة لجدولة المباريات وتنسيق الفرق وضمان التنفيذ السلس للحدث.
- **Summarize** ………….
  - Give me a brief summary of the last World Cup
- **لخص/ قم بتلخيص**
  - أعطني نبذة مختصرة عن كأس العالم الأخيرة.
- **In which year** were the first ……….. Games held?
  - **a)** .....
  - **b)** .....
  - **c)** ......
  - **d)** .......
- **في أي عام** أقيمت أول ألعاب ………….؟
  - ………………..
  - ………………..
  - …………………
  - …………………
- **Which city** hosted the first ……………tournament?
  - **a)** .....
  - **b)** ......
  - **c)** .....
  - **d)** ......
- **ما هي المدينة** التي استضافت أول بطولة …………..؟
  - ………….
  - ………….
  - …………..
- **What is the** most popular sport in …………?
  - **a)**
  - **b)**
  - **c)**
- **ما هي** الرياضة الأكثر شعبية في ………..؟
  - ………………
  - …………………
  - ……………….
- **Which** ………….. football club is considered the most successful domestically?
  - **a)** .....
  - **b)** .....
  - **c)** ......
- **ما هو** نادي كرة القدم …………. الذي يعتبر الأكثر نجاحًا محليًا؟
  - …………
  - ………..
  - ……….
- **List the** player's name in ………… club
- **اكتب قائمة أسماء** اللاعبين في نادي ………….
- **Which** xxxx athlete won a gold medal in weightlifting at the 2021 Tokyo Olympics?
  - **a)** .....
  - **b)** .....
  - **c)** .......
- **من هو ال**رياضي …………الذي فاز بميدالية ذهبية في رفع الأثقال في أولمبياد طوكيو 2021؟
  - …..
  - …..
  - …..
- **Write a report on** the development and popularity of football (soccer) in …………., highlighting the national team's achievements and the most successful …………… football clubs.
- **اكتب تقريرًا عن** تطور وشعبية كرة القدم في ………….، مع تسليط الضوء على إنجازات المنتخب الوطني وأنجح أندية كرة القدم ………..
- **Mention** the countries that won the ………… Championship and the number of times they won
- **اذكر** الدول التي فازت ببطولة ……….. وعدد مرات فوزها

#### Examples

**Example 1**

| **Instruction** | اعطني قوانين كرة اليد<br><br>ما هي قواعد كرة اليد<br><br>كيف العب كرة اليد<br><br>اشرح لي قواعد كرة اليد |
| --- | --- |
| **Input** |     |
| **Output** | هناك العديد من القوانين التي تحكُم مباراة كرة اليد، ومن هذه القوانين: تبدأ المباراة برمية البداية التي يتمّ تنفيذها من قِبل أحد لاعبي الفريق الذي يمتلك الكرة، ثمّ تمريرها إلى لاعبي فريقه، ولا بدّ أن يكون اللاعب واقفاً على قدم واحدة على خطّ المركز أثناء تنفيذه لهذه الرمية. تُنفَّذ رمية البداية عقب كلّ هدف يتمّ إحرازه في المباراة، وفي بداية كلّ شوط من أشواطها. يكون لاعبو الفريقين كلٌّ في الجزء المُخصَّص له من أرض الملعب عند تنفيذ رمية البداية. يُحظَر على لاعب كرة اليد استخدام قدمَيه، أو الأجزاء السُّفلى من ساقَيه للتعامل مع الكرة، كتمريرها، أو إيقافها، أو حتى الإمساك بها. لا يجوز للاعب الاحتفاظ بالكرة ثلاث خطوات متتالية دون تنطيطها. يُحظَر على لاعب كرة اليد لمس الكرة مرّتَين مُتتاليتَين دون تنطيطها، أو تمريرها. لا يحقّ لأيّ لاعب الوجود ضمن منطقة المرمى سوى حارس مرمى دفاع الفريق. يكسب الفريق رمية حرة في حال تمّ رمي الكرة بطريقة غير قانونية، أو في حال حدوث خطأ من قِبل أحد أعضاء الفريق الخَصم. تُتيح الرمية الحرة للاعب تنفيذ رمية بدون أيّ تدخُّل من لاعبي الفريق الخَصم. يقف لاعبو الفريق الخَصم على بُعد ثلاثة أمتار خلف خطّ تنفيذ الرمية الحرة، وذلك في حال حدوث الخطأ ضمن منطقة الرمية الحرة. يحصل اللاعب على رمية جزاء في حال تعرُّضه لتدخُّل أحد لاعبي الفريق الخَصم ضمن منطقة المرمى، أو عرقلته عند التسديد المُباشر على المرمى. تُنفَّذ رمية الجزاء من خطّ الجزاء الذي يبعد سبعة أمتار عن خطّ المرمى، ويُحظَر على أيّ شخص التصدّي لركلة الجزاء سوى حارس المرمى، بشرط إبقاء مسافة لا تقلّ عن ثلاثة أمتار بينه وبين اللاعب المُنفِّذ لرمية الجزاء. يُسمَح للاعبي الفريقَين مُدافعة بعضهم باستخدام أجسادهم، ودون العرقلة باستخدام الأيدي، أو الأقدام. يُمنَع سحب الكرة، أو ضربها أثناء وجودها في يدي لاعب آخر. تُمنَح رمية إدخال جانبيّة للفريق في حال خروج الكرة من الملعب، وذلك عند مُلامستها لأحد لاعبي الفريق الخَصم قبل خروجها. يحصل لاعبو الفريق الخَصم على رمية رُكنيّة في حال لمْس أحد لاعبي الفريق للكرة قبل خروجها في منطقة دفاع الفريق. يرمي الحَكم الكرة في الهواء بين لاعبَين اثنين يُمثّلان كلا الفريقَين، وذلك في حال توقُّف اللعب لسبب لا يُعتبَر فيه أيّ من الفريقَين مسؤولاً عن ذلك، ثمّ يقفز كلا اللاعبين؛ للحصول على الكرة. تحقّ لحارس المرمى حرّية الحركة دون أيّة قيود طيلة وجوده ضمن منطقة مرماه. لا يُحظَر على حارس المرمى استخدام قدمَيه، أو أيٍّ من أجزاء جسده؛ للدفاع عن مرماه. لا يجوز للاعبي الفريقَين رمي الكرة وإبعادها خارج الملعب بشكل مُتعمَّد ومقصود. تُمنَح بطاقة صفراء، إلى جانب الإيقاف عن اللعب مدّة دقيقتين للاعب عند ارتكابه خطأ أو سوء تصرُّف على أرضيّة الملعب. يُمنَح اللاعب بطاقة حمراء للأخطاء العنيفة والشديدة التي قد تحدث في المباراة. يتحتّم على اللاعب الذي يحصل على بطاقة حمراء أو بطاقتَين صفراوين التوقُّف عن اللعب والخروج خارج منطقة الملعب كاملة. يحصل الفريق الخَصم على رمية حرة يتمّ تنفيذها من مكان حدوث الخطأ الذي أدّى إلى حصول الفريق على بطاقة. يعود اللاعب الذي تمّ إيقافه عن اللعب إلى أرض الملعب في حال تسجيل الخصم لهدف. |
| **Source** | <https://mawdoo3.com/%D8%AA%D8%B9%D8%B1%D9%8A%D9%81_%D9%83%D8%B1%D8%A9_%D8%A7%D9%84%D9%8A%D8%AF_%D9%88%D9%82%D9%88%D8%A7%D9%86%D9%8A%D9%86%D9%87%D8%A7> |

###

**Example 2**

| **Instruction** | في أي عام أقيمت أول دورة ألعاب أولمبية حديثة؟ |
| --- | --- |
| **Input** | أ) 1896<br><br>ب) 1908<br><br>ج) 1924<br><br>د) 1952 |
| **Output** | أ) 1896 |
| **Source** |     |

####

**Example 3**

| **Instruction** | صمم برنامج للياقة البدنية للمبتدئين في المنزل |
| --- | --- |
| **Input** |     |
| **Output** | قد يكون بدء برنامج للياقة البدنية أحد أفضل الأشياء التي يمكنك القيام بها من أجل صحتك. يمكن أن يقلل النشاط البدني من خطر الإصابة بالأمراض المزمنة، ويحسن توازنك وتنسيقك، ويساعدك على إنقاص الوزن — وحتى تحسين عادات نومك واحترامك لذاتك. وهناك المزيد من الأخبار الجيدة. يمكنك بدء برنامج للياقة البدنية في خمس خطوات فقط.<br><br>1\. تقييم مستوى لياقتك البدنية<br><br>ربما لديك فكرة عن مدى لياقتك البدنية. لكن تقييم وتسجيل درجات اللياقة البدنية الأساسية يمكن أن يمنحك معايير لقياس مدى تقدمك. لتقييم اللياقة البدنية والعضلية والمرونة وتكوين الجسم، فكر في التسجيل:<br><br>معدل نبضك قبل وبعد المشي لمسافة ميل واحد (1.6 كيلومتر) مباشرة<br><br>كم من الوقت يستغرق المشي لمسافة ميل واحد، أو كم من الوقت يستغرق الجري لمسافة 1.5 ميل (2.41 كيلومتر)<br><br>كم عدد تمارين الضغط القياسية أو المعدلة التي يمكنك القيام بها في المرة الواحدة<br><br>إلى أي مدى يمكنك الوصول للأمام أثناء الجلوس على الأرض مع وضع ساقيك أمامك<br><br>محيط خصرك، فوق عظام الورك مباشرةً<br><br>مؤشر كتلة جسمك<br><br>2\. صمم برنامج اللياقة البدنية الخاص بك<br><br>من السهل أن تقول أنك ستمارس الرياضة كل يوم. لكنك ستحتاج إلى خطة. أثناء تصميم برنامج اللياقة البدنية الخاص بك، ضع هذه النقاط في الاعتبار:<br><br>النظر في أهداف اللياقة البدنية الخاصة بك. هل تبدأ برنامجًا للياقة البدنية للمساعدة في إنقاص الوزن؟ أو هل لديك دافع آخر، مثل الاستعداد لسباق الماراثون؟ إن وجود أهداف واضحة يمكن أن يساعدك على قياس التقدم الذي تحرزه والبقاء متحفزًا.<br><br>إنشاء روتين متوازن. مارس ما لا يقل عن 150 دقيقة من النشاط الهوائي المعتدل أو 75 دقيقة من النشاط الهوائي القوي أسبوعيًا، أو مزيجًا من النشاط المعتدل والقوي. تقترح الإرشادات أن تقوم بتوزيع هذا التمرين على مدار الأسبوع. لتوفير فائدة صحية أكبر وللمساعدة في فقدان الوزن أو الحفاظ على فقدان الوزن، يوصى بممارسة 300 دقيقة على الأقل في الأسبوع.<br><br>ولكن حتى الكميات الصغيرة من النشاط البدني مفيدة. إن ممارسة النشاط لفترات قصيرة من الوقت على مدار اليوم يمكن أن تضيف فوائد صحية.<br><br>قم بتمارين القوة لجميع مجموعات العضلات الرئيسية مرتين على الأقل في الأسبوع. اهدف إلى أداء مجموعة واحدة من كل تمرين، باستخدام وزن أو مستوى مقاومة ثقيل بما يكفي لإرهاق عضلاتك بعد حوالي 12 إلى 15 تكرارًا.<br><br>ابدأ بالمستوى المنخفض ثم تقدم ببطء. إذا كنت قد بدأت للتو في ممارسة التمارين الرياضية، فابدأ بحذر وتقدم ببطء. إذا كنت تعاني من إصابة أو حالة طبية، فاستشر طبيبك أو معالج التمارين الرياضية لمساعدتك في تصميم برنامج للياقة البدنية يعمل على تحسين نطاق الحركة والقوة والقدرة على التحمل تدريجيًا.<br><br>بناء النشاط في روتينك اليومي. يمكن أن يشكل إيجاد الوقت لممارسة الرياضة تحديًا. لتسهيل الأمر، حدد وقتًا لممارسة التمارين كما تفعل في أي موعد آخر. خطط لمشاهدة برنامجك المفضل أثناء المشي على جهاز المشي، أو القراءة أثناء ركوب الدراجة الثابتة، أو أخذ قسط من الراحة للذهاب للمشي في العمل.<br><br>خطة لتشمل أنشطة مختلفة. يمكن للأنشطة المختلفة (التدريب المتقاطع) أن تمنع ملل التمارين الرياضية. كما أن التدريب المتقاطع باستخدام أشكال الأنشطة منخفضة التأثير، مثل ركوب الدراجات أو التمارين المائية، يقلل أيضًا من فرص إصابة عضلة أو مفصل معين أو الإفراط في استخدامه. خطط للتبديل بين الأنشطة التي تركز على أجزاء مختلفة من جسمك، مثل المشي والسباحة وتدريبات القوة.<br><br>جرب التدريب عالي الكثافة. في التدريب عالي الكثافة، تقوم بأداء دفعات قصيرة من النشاط عالي الكثافة مفصولة بفترات تعافي من النشاط منخفض الشدة.<br><br>إتاحة الوقت للتعافي. يبدأ العديد من الأشخاص في ممارسة التمارين الرياضية بحماسة محمومة — ممارسة التمارين الرياضية لفترة طويلة جدًا أو بشكل مكثف للغاية — ويتوقفون عن ممارسة الرياضة عندما تصبح عضلاتهم ومفاصلهم مؤلمة أو مصابة. خطط للوقت بين الجلسات حتى يرتاح جسمك ويتعافى.<br><br>ضعها على الورق. قد تشجعك الخطة المكتوبة على البقاء على المسار الصحيح.<br><br>3\. قم بتجميع المعدات الخاصة بك<br><br>من المحتمل أن تبدأ بالأحذية الرياضية. تأكد من اختيار الأحذية المصممة للنشاط الذي تفكر فيه. على سبيل المثال، أحذية الجري أخف وزنًا من أحذية التدريب المتقاطع، والتي تكون أكثر دعمًا.<br><br>إذا كنت تخطط للاستثمار في معدات التمارين الرياضية، فاختر شيئًا عمليًا وممتعًا وسهل الاستخدام. قد ترغب في تجربة أنواع معينة من المعدات في مركز اللياقة البدنية قبل الاستثمار في المعدات الخاصة بك.<br><br>قد تفكر في استخدام تطبيقات اللياقة البدنية للأجهزة الذكية أو أجهزة تتبع النشاط الأخرى، مثل تلك التي يمكنها تتبع المسافة التي تقطعها أو تتبع السعرات الحرارية المحروقة أو مراقبة معدل ضربات القلب.<br><br>4\. ابدأ<br><br>أنت الآن جاهز للعمل. عندما تبدأ برنامج اللياقة البدنية الخاص بك، ضع هذه النصائح في الاعتبار:<br><br>ابدأ ببطء وقم بالبناء تدريجيًا. امنح نفسك متسعًا من الوقت للإحماء والتهدئة من خلال المشي بسهولة أو تمارين التمدد اللطيفة. ثم قم بزيادة السرعة إلى وتيرة يمكنك الاستمرار فيها لمدة خمس إلى 10 دقائق دون الشعور بالتعب الشديد. مع تحسن قدرتك على التحمل، قم بزيادة مقدار الوقت الذي تمارسه تدريجيًا. مارس التمارين الرياضية لمدة تصل إلى 30 إلى 60 دقيقة معظم أيام الأسبوع.<br><br>قم بتفكيك الأشياء إذا كان عليك ذلك. ليس عليك القيام بكل تمارينك الرياضية في وقت واحد، لذا يمكنك ممارسة النشاط طوال يومك. أقصر بو |
| **Source** | <https://www.mayoclinic.org/healthy-lifestyle/fitness/in-depth/fitness/art-20048269> |

####

**Example 4**

| **Instruction** | اذكر البلدان العربية الفائزة ببطولة افريقيا و عدد مرات الفوز |
| --- | --- |
| **Input** |     |
| **Output** | بكل تأكيد، فازت خمسة بلدان عربية ببطولة افريقيا للأمم، هذه البلدان هي مصر بسبع بطولات، ثم الجزائر ببطولتين، ثم المغرب و تونس و السودان ببطولة لكل منهم. |
| **Source** | <https://ar.wikipedia.org/wiki/%D8%B3%D8%AC%D9%84_%D8%A7%D9%84%D9%85%D8%B4%D8%A7%D8%B1%D9%83%D8%A7%D8%AA_%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9_%D9%81%D9%8A_%D9%83%D8%A3%D8%B3_%D8%A7%D9%84%D8%A3%D9%85%D9%85_%D8%A7%D9%84%D8%A5%D9%81%D8%B1%D9%8A%D9%82%D9%8A%D8%A9> |

### Science: Physics (General Domain)

Physics is related to the natural science of matter, its fundamental constitutes, its motion and behavior through space and time, and the related entities of energy and force

**Possible subtopics could be but are not limited to**

- **Mechanics (الميكانيكا)**: E.g., Newton’s law of Motion قانون نيوتن للحركة
- **Thermodynamics (الديناميكا الحرارية):** E.g., The first law of thermodynamics (conservation of Energy) (القانون الأول للديناميكا الحرارية (حفظ الطاقة
- **Electromagitism (الكهرومغناطيسية):** E.g., Faraday’s law of electromagnetic induction (قانون فراداي للحث الكهرومغناطيسي)
- **Condensed Matter Physics (فيزياء المادة المكثفة):** E.g., Superconductivity (الموصلية الفائقة)
- **Cosmology (علم الكون):** The Big Bang Theory (نظرية الإنفجار الكبير)
- **Geophysics (لفيزياء الجيولوجية):** Earth’s magentic field (المجال المغناطيسي للأرض)
- **Acoustics (الصوتيات):** E.g., The Doppler Effect (تأثير دوبلر)
- **Plasma Physics (فيزياء البلازما):** The magnetic confinement
- **Optics (البصريات):** E.g., Laws of reflection and refraction (قوانين الانعكاس والانكسار)
- **Quantum Mechanics (الميكانيكا الكمية):** Schrodinger’s Wave equation (معادلة شرودنجر الموجية)
- **Relativity (النسبية):** E.g., Einstin’s Theory of special relativity (نظرية اينشتاين للنسبية الخاصة)
- **Nuclear physics (الفيزياء النووية):** E.g., Radioactive Decay (الاضمحلال الاشعاعي)
- **Particle physics (فيزياء الجسيمات):** E.g., The Higgs Boson Particle (جسيم ​​**بوزون** هيغز)
- **Astrophysics (الفيزياء الفلكية):** E.g., Black Holes (الثقوب السوداء)
- **Fluid mechanics (ميكانيكا الموائع):** E.g., Bernollui’s principle (مبدأ برونولي)

#### Instructions could be but are not limited to

- **Explain** the fundamental principles of mechanics

E.g., Explian the three core laws of Newtonian mechanics

- **اشرح** قوانين الميكانيكا الثلاثة الاساسية حسب نيوتن
- **Decribe** … (the relationship between pressure, volume and temperature as per the Ideal Gas Law)
- **قدم وصف** للعلاقة بين الضغط والحجم ودرجة الحرارة طبقا لقانون الغاز المثالي
- **Discuss** … (the characteristics and and applications of electromagnetic waves in daily life)
- **ناقش** خصائص و تطبيقات الموجات الكهرومغناطيسية في الحياة اليومية
- **Outline** … (the foundation assumptions underlying quantum mechanical theory)
- **حدد** الافتراضات الأساسية التي تقوم عليها نظرية الميكانيكا الكمية
- **Mention** … (practical examples illustrating the principles of light reflection and refraction)
- **اذكر أمثلة** عملية توضح مبادئ انعكاس وانكسار الضوء
- **Highlight** … (the distinctions and similarities between Einestein’s relativity and Newtonian physics)
- **سلًط الضوء على** الفروق و التشابهات بين النظرية النسبية لأينشتاين وفيزياء نيوتن
- **Illustrtate** … (through experiments the dual nature of matter and light)
- **وضًح** من خلال التجارب الطبيعة المزدوجة للمادة و الضوء
- **Follow the steps** … (of Foucault’s pendulum experiment to demonstrate the rotation of the earth)
- **اتبع خطوات** تجربة بندول فوكو لإثبات دوران الأرض
- **Compare** … (the output and the feasibility of solar panels, wind turbines, and hydroelectric dams)
- **قارن بين** الإخراج والجدوى لألواح الطاقة الشمسية، توربينات الرياح والسدود المائية.
- **Using the formulas of** … (special relativity determin how much time would seem to pass for someone traveling at 90% of the speed of light for five years.)
- **باستخدام صيغ النسبية الخاصة، حدد كم** من الوقت قد يبدو انه مر على شخص يسافر بسرعة تعادل ٩٠٪ من سرعة الضوء لمدة ٥ سنوات.

#### Examples

**Example 1**

| **Instruction** | اكتب نبذة عن تجربة بندول فوكو لإثبات دوران الأرض |
| --- | --- |
| **Input** |     |
| **Output** | **رقاص فوكو** ([بالإنجليزية](https://www.wikiwand.com/ar/%D8%A7%D9%84%D9%84%D8%BA%D8%A9_%D8%A7%D9%84%D8%A5%D9%86%D8%AC%D9%84%D9%8A%D8%B2%D9%8A%D8%A9): Foucault pendulum)‏ هي تجربة وضعت لتقديم إثبات علمي بسيط لحقيقة [دوران الأرض](https://www.wikiwand.com/ar/%D8%AF%D9%88%D8%B1%D8%A7%D9%86_%D8%A7%D9%84%D8%A3%D8%B1%D8%B6) حول محورها. صمم التجربة الفيزيائي الفرنسي [ليون فوكو](https://www.wikiwand.com/ar/%D9%84%D9%8A%D9%88%D9%86_%D9%81%D9%88%D9%83%D9%88). التجربة التي قام بها فوكو في أواسط القرن التاسع عشر كانت عبارة عن تعليق ثقل قدره 28 كجم بسلك طوله 67 متراً إلى قبة كنيسة بانتيون Panthéon في [باريس](https://www.wikiwand.com/ar/%D8%A8%D8%A7%D8%B1%D9%8A%D8%B3) مشكلاً بذلك رقاصا عملاقاً. وعند تحريك الرقاص وُجد أن مستوى اهتزازه كان يدور باتجاه عقارب الساعة بمقدار 11° كل ساعة، متمماً بذلك دورة كاملة كل 32.7 ساعة<br><br>في الحقيقة، لو قمنا بوضع الرقاص عند القطب الشمالي مثلاً فإنه سيتم دورة كاملة كل 24 ساعة تقريباً، وهو زمن دوران الأرض حول نفسها. لكن زمن إتمام دورة الرقاص سيزداد كلما ابتعدنا عن القطب واقتربنا من خط الاستواء، حيث يصبح ما لانهاية عند خط الاستواء. من الجدير بالذكر أيضاً أن اتجاه دوران الرقاص هو اتجاه دوران عقارب الساعة إذا ما كان الرقاص في النصف الشمالي للكرة الأرضية، لكن اتجاه الدوران يصبح عكس اتجاه دوران عقارب الساعة إذا ما كان الرقاص في النصف الجنوبي للكرة الأرضية. يوجد اليوم العديد من النماذج المختلفة من رقاص فوكو معروضة في كثير من دول العالم. ونستطيع الاستنتاج من البندول ذات الابعاد الثلاثة للتقويم الشمسي وهي الليل والنهار والارض والشمس. وبناء علي تلك الابعاد استطاع الإنسان استبيان الاعتدالين واختراع الساعة الرقميه الحديثه ويمكن ان نطلق عليها مجازا الساعة الشمسيه. |
| **Source** | <https://www.wikiwand.com/ar/%D8%B1%D9%82%D8%A7%D8%B5_%D9%81%D9%88%D9%83%D9%88> |

####

**Example 2**

| **Instruction** | كيف يتم قياس الجاذبية الأرضية؟ |
| --- | --- |
| **Input** |     |
| **Output** | تتغير شدة مجال الثقالة g بتغير المكان و الارتفاع على [سطح الأرض](https://www.wikiwand.com/ar/%D8%A7%D9%84%D8%A3%D8%B1%D8%B6)، وترتبط قيمتها بطبيعة الطبقات الجيولوجية المكونة [للقشرة الأرضية.](https://www.wikiwand.com/ar/%D8%A7%D9%84%D9%82%D8%B4%D8%B1%D8%A9_%D8%A7%D9%84%D8%A3%D8%B1%D8%B6%D9%8A%D8%A9) يمكن قياس تغيرات شدة مجال [الثقالة](https://www.wikiwand.com/ar/%D8%AC%D8%A7%D8%B0%D8%A8%D9%8A%D8%A9) من رسم خرائط جيولوجية دقيقة تساعد الأخصائيين في [الفيزياء الجيولوجية](https://www.wikiwand.com/ar/%D9%81%D9%8A%D8%B2%D9%8A%D8%A7%D8%A1) من معرفة مكونات طبقات القشرة الأرضية. لقياس تغيرات شدة مجال الثقالة في مكان ما يستعمل جهاز قياس مجال الثقالة (gravimétre) المحول على متن طائرة للأبحاث تحلق على ارتفاع ثابت. تقوم الطائرة بمسح الجهة المراد دراستها، ويسجل هذا المقياس التغيرات الدقيقة جدا لشدة المجال. تستثمر هذه القياسات لتحديدد أماكن المعادن، [والحقول البترولية](https://www.wikiwand.com/ar/%D9%86%D9%81%D8%B7)، و المواقع الأثرية، والمياه الباطنية، و مناجم الملح... التي توجد في باطن الأرض. |
| **Source** | <https://www.wikiwand.com/ar/%D8%AC%D8%A7%D8%B0%D8%A8%D9%8A%D8%A9_%D8%A3%D8%B1%D8%B6%D9%8A%D8%A9> |

**Example 3**

| **Instruction** | اشرح قانون بقاء الطاقة في النظرية النسبية لأينشتاين |
| --- | --- |
| **Input** |     |
| **Output** | **حفظ الطاقة** في [الفيزياء](https://www.wikiwand.com/ar/%D9%81%D9%8A%D8%B2%D9%8A%D8%A7%D8%A1) ينص قانون **حفظ الطاقة** على أنه في أي نظام معزول خلال التفاعل داخل النظام، الطاقة لا تستحدث من العدم ولا تنعدم ولكن يمكن تحويلها من شكل لآخر. مكن تحويل الطاقة من شكل إلى آخر مثل [طاقة الحركة](https://www.wikiwand.com/ar/%D8%B7%D8%A7%D9%82%D8%A9_%D8%AD%D8%B1%D9%83%D9%8A%D8%A9) يمكن أن تتحول إلى [طاقة حرارية](https://www.wikiwand.com/ar/%D8%B7%D8%A7%D9%82%D8%A9_%D8%AD%D8%B1%D8%A7%D8%B1%D9%8A%D8%A9)، ولكن ليس ممكنا في نظام مغلق معزول أن تخلق طاقة من نفسها أو تفنى. ونقول أن الطاقة تتبع [قوانين الانحفاظ](https://www.wikiwand.com/ar/%D9%82%D8%A7%D9%86%D9%88%D9%86_%D8%AD%D9%81%D8%B8).<br><br>نعرف اشكالا عديدة للطاقة: [طاقة حركة](https://www.wikiwand.com/ar/%D8%B7%D8%A7%D9%82%D8%A9_%D8%AD%D8%B1%D9%83%D9%8A%D8%A9)، [طاقة حرارية](https://www.wikiwand.com/ar/%D8%B7%D8%A7%D9%82%D8%A9_%D8%AD%D8%B1%D8%A7%D8%B1%D9%8A%D8%A9)، [طاقة كهربائية](https://www.wikiwand.com/ar/%D8%B7%D8%A7%D9%82%D8%A9_%D9%83%D9%87%D8%B1%D8%A8%D8%A7%D8%A6%D9%8A%D8%A9)، [طاقة حركية](https://www.wikiwand.com/ar/%D8%B7%D8%A7%D9%82%D8%A9_%D9%85%D9%8A%D9%83%D8%A7%D9%86%D9%8A%D9%83%D9%8A%D8%A9)، [طاقة إشعاعية](https://www.wikiwand.com/ar/%D8%B7%D8%A7%D9%82%D8%A9_%D8%A5%D8%B4%D8%B9%D8%A7%D8%B9%D9%8A%D8%A9) وغيرها، ويمكن تحولها من صورة إلى أخرى. ولكن تبقى الطاقة لا تنعدم ولا تستحدث. كما بينت النظرية النسبية [لأينشتاين](https://www.wikiwand.com/ar/%D8%A3%D9%84%D8%A8%D8%B1%D8%AA_%D8%A3%D9%8A%D9%86%D8%B4%D8%AA%D8%A7%D9%8A%D9%86) أن الطاقة يمكن أن تتحول إلى مادة (انظر أسفله):<br><br>وقانون انحفاظ الطاقة هو أحد المبادئ الأساسية في جميع العلوم وينص على:<br><br>**قيمة الطاقة الكلية في نظام مغلق لا تتغير.**<br><br>ونعني «بنظام مغلق» بأنه نظام لا يتبادل طاقة أو معلوماتية أو مادة أو تآثر مع الوسط المحيط. |
| **Source** | <https://www.wikiwand.com/ar/%D8%AD%D9%81%D8%B8_%D8%A7%D9%84%D8%B7%D8%A7%D9%82%D8%A9_(%D9%81%D9%8A%D8%B2%D9%8A%D8%A7%D8%A1)> |

### Science: Biology (General Domain)

Biology is a general domain that addresses living organisms, their origins, anatomy, behavior, and distribution.

#### Possible subtopics are not limited to

- **Cell Biology (Cytology)**: cell structure and function, cell cycle and division, cellular metabolism.
- **Molecular Biology:** DNA, RNA, and protein synthesis, Gene regulation, Molecular.
- **Genetics**: Mendelian genetics, population genetics, genetic engineering and biotechnology.
- **Evolutionary Biology:** The theory of evolution, speciation, human evolution
- **Ecology:** Ecosystems, population ecology, conservation biology.
- **Anatomy and physiology:** Human anatomy, plant anatomy (Botany), Animal physiology.
- **Microbiology:** Bacteria and archaea, viruses, fungi
- **Botany (plant science):** Plant physiology, plant taxonomy, plant disease.
- **Zoology (Animal Science):** Animal behavior, taxonomy, and disease.
- **Neuroscience:** Neurons and synapses, the human brain, neurological diseases.
- **Developmental Biology:** Embryology, Growth and differentiation, regeneration and aging.
- **Immunology:** The immune response, vaccination, autoimmune diseases.
- **Biotechnology:** Genetic engineering, CRISRP technology, cloning.
- **Paleontology:** Fossils, evolutionary history, ancient life forms.
- **Biochemistry:** Metabolism, Enzyme function, cellular respiration.
- **Biophysics:** Mechanisms of molecular systems, biophysical techniques
- **Ethology (Animal Behavior):** Animal communication, mating, feeding behaviors, instinct vs. learning.
- **Bioinformatics:** Genomic data analysis, Molecular modeling, systems biology.
- **Pharmacology:** Drug action and discovery, clinical trials, toxicology
- **Environmental Biology**: pollution and its effects, climate change impacts, conservation strategies.

#### Instructions could be but are not limited to

- **Explain** … (photosynthesis)
- **اشرح** …..
- **Describe the** … (process of DNA replication)
- **صف** … (عملية استنساخ الدي ان اي)
- **What is** ….?
- **ما هو** ….؟
- **How does the** … (immune system work)?
- **كيف يعمل** … (الجهاز المناعي؟)
- **Compare** … (mitosis and meiosis.)
- **قارن بين** … (الانقسام الخلوي و التخصيب)
- **List the** … (types of blood cells.)
- **اكتب قائمة** … (أنواع خلايا الدم)
- **Discuss the importance of** … (biodiversity)
- **ناقش أهمية** … (التنوع البيولوجي.)
- **Provide examples of** … (genetic disorders)
- **قدم أمثلة على** … (الاضطرابات الوراثية)
- **Outline the steps of** … (protein synthesis)
- **حدد خطوات** … (تصنيع البروتين)
- **Elaborate/ illustrate on** … (the role of hormonse in the human body)
- **وضّح** … (دور الهرمونات في جسم الإنسان)
- **Define** … (ecology)
- **عّرف** … (البيئة)
- **Summarize** … (the principles of Mendelian genetics)
- **اختصر** … (مبادئ الوراثة المندلية)
- **Identify** … (the main components of the nervous system)
- **حدد** … (المكونات الرئيسية للجهاز العصبي)
- **Distinguish between** … ( )
- **قم بالتمييز بين** …
- **Theorize about** … (the origins of life on Earth).
- **اطرح نظرية حول** … ( أصول الحياة على كوكب الأرض)
- **Calculate** … (the genetic probability of a trait being passed on).
- **احسب** … (الاحتمال الجيني لنقل صفة معينة)
- **Recommend** … (ways to conserve endangered species)
- **قدم توصية حول** … (طرق الحفاظ على الأنواع المهددة بالأنقراض)

#### Examples

**Example 1**

| **Instruction** | اكتب نبذة عامة من أربع فقرات عن عملية النسخ Transcription |
| --- | --- |
| **Input** |     |
| **Output** | النسخ هو تخليق (mRNA) على أساس تسلسل النيوكليوتيدات في DNA. يحدث ذلك عندما تنفصل الأشرطة المزدوجة لجزء DNA ، حيث تعمل أحد الأشرطة كقالب، وتقترن نيوكليوتيدات RNA مع نيوكليوتيدات DNA للقالب. تقترن النيوكليوتيدات مع بعضها البعض وفقًا للقاعدة التالية: أزواج الأدينين (A) مع الثيمين (T) أو اليوراسيل (U)، وأزواج السيتوسين (C) مع الجوانين (G). يحتوي DNA على الثيمين (T)، لكن اليوراسيل (U) يحل محل الثيمين في RNA. لذلك، تقترن نيوكليوتيدات DNA من الأدينين، والثيمين، والسيتوسين، والجوانيين، مع النيوكليوتيدات التي توجد في RNA ، على التوالي.<br><br>تضمن علاقة الاقتران هذه بين النيوكليوتيدات نقل المعلومات الموجودة في DNA بشكل صحيح إلى (mRNA). تتحد نيوكليوتيدات (RNA) من خلال تفاعلات نزع الماء (Dehydration reactions) المحفزة بواسطة إنزيمات ال RNA البوليمرية لتشكيل جزء (mRNA) طويل.يحدث استطالة لجميع الأحماض النووية، ل DNA و RNA ، في نفس الاتجاه الكيميائي: From the 5' to the 3' of the molecule.يحتوي جزيء mRNA على المعلومات المطلوبة لتحديد تسلسل الأحماض الأمينية في البروتين. يتم نقل المعلومات، التي تسمى الشفرات الجينية (genetic code)، في مجموعات من ثلاثة نيوكليوتيدات تسمى الكودونات (codons).<br><br>يتم تحديد عدد وتسلسل الكودونات في (mRNA) من خلال عدد وتسلسل مجموعات من ثلاث نيوكليوتيدات، تسمى (Triplets)، في أجزاء من RNA التي تم نسخها. على سبيل المثال، الكود الثلاثي لـ CTA في DNA يؤدي إلى كودون GAU في ترميز (mRNA)، أي شفرات حمض الأسبارتيك. كل شفرة كودون خاصة بحمض أميني معين. يوجد أربعة وستون شيفرة من (mRNA)، لكن فقط 20 من الأحماض الأمينية موجودة في البروتينات. ونتيجة لذلك، تكون الجينات الوراثية زائدة عن الحاجة لأن بعض الأحماض الأمينية تشفر بأكثر من شفرة كودونية واحدة.فمثلا، CGA و CGG و CGT و CGC جميع شفرات للحمض الأميني الانين و UUU و UAC كلاهما شفرة للفينيل ألانين. بعض الCodons لا تعتبر شفرات للأحماض الأمينية ولكنها تؤدي وظائف أخرى. تعمل AUG وأحيانا GUG كإشارات لبدء استنساخ امتداد DNA إلى RNA. تعمل ثلاث شفرات هي UAA و UGA و UAG كإشارات لإيقاف استنساخ DNA إلى RNA.منطقة جزيء DNA الواقعة بين شفرات بداء النسخ وشفرات الوقف تستنسخ إلى داخل امتدادات RNA وتسمىوحدة النسخ (Transcription unit). وترمز وحدة النسخ إلى بروتين أو جزء من البروتين. وحدة النسخ ليست بالضرورة جينًا. حيث إن الجين وحدة وظيفية، وبعض الجينات التنظيمية لا ترمز للبروتينات. التعريف الجزيئي للجين هو: هو جميع تسلسلات الأحماض النووية اللازمة لخلق وظيفة ال RNA أو البروتين.<br><br>ليس كل امتداد مستمر من DNA قد يرمز لأجزاء من البروتين. تسمى مناطق DNA التي ترمز لأجزاء من البروتين exons))، في حين أن مناطق الحمض النووي التي لا ترمز لأجزاء من البروتين تسمى الإنترونات (introns). قد يتم نسخ كل من مناطق ال exons و intron من DNA إلى RNA. يُطلق على mRNA المحتوي على الإنترونات اسم ال RNA المجهري الأولي (pre-mRNA). بعد نسخ امتداد pre-mRNA ، يمكن إزالة الإنترونات وتقسيم الإكسونات معًا بواسطة إنزيمات معقدة تسمى المكورات العصبية spliceosomes لإنتاج mRNA الوظيفي. وتسمى هذه التغييرات في الحمض النووي الريبوزي بعملية posttranscriptional. |
| **Source** | <https://www.wikiwand.com/ar/%D9%86%D8%B3%D8%AE_(%D9%88%D8%B1%D8%A7%D8%AB%D8%A9)> |

**Example 2**

| **Instruction** | كيف يعمل جهاز المناعة على مقاومة العدوى؟ |
| --- | --- |
| **Input** |     |
| **Output** | الجهاز المناعي هو عبارة عن جيش يدافع عن موطنه من الغزاة، ويتم تحصين الجيش من خلال الجلد وطبقة القرنية في العين، وبطانة المخاط الموجودة في الفم، والرئتين، والخلايا، والأنسجة في الأمعاء.<br><br>ليس هذا فقط بل إن الإفرازات والسوائل التي تخرج من الجسم تساعد في دفع الجراثيم للخارج كما أن الإنزيمات الموجودة فيها تقوم بقتل الجراثيم، وتتمثل هذه الإفرازات والسوائل في العرق، ودموع العين، والمخاط في الأنف، وإفرازات المهبل.<br><br>لذلك فإن أي ضرر بالجلد أو هذه الأنسجة، أو تلف الخلايا أو الخلل في الإفرازات والسوائل قد يعرض الجسم إلى هجوم الجراثيم وسهولة العدوى. |
| **Source** | <https://www.webteb.com/articles/%D9%83%D9%8A%D9%81-%D9%8A%D8%B9%D9%85%D9%84-%D8%AC%D9%87%D8%A7%D8%B2-%D8%A7%D9%84%D9%85%D9%86%D8%A7%D8%B9%D8%A9-%D9%81%D9%8A-%D8%A7%D9%84%D8%AC%D8%B3%D9%85_19542> |

**Example 3**

| **Instruction** | اكتب قائمة بأهم مكونات جهاز المناعة في جسم الإنسان |
| --- | --- |
| **Input** |     |
| **Output** | يتكون الجهاز المناعي من العديد من الأجزاء التي تعمل كجيش متكامل الأركان لمقاومة الأعداء، ومن أهم مكوناته التي تقوم بالأدوار الأساسية في الجسم:<br><br>1\. الخلايا الليمفاوية<br><br>تعتبر الخلايا الليمفاوية صاحبة المهمة الأصعب في الجهاز المناعي، وهي عبارة عن شبكة من الأنابيب الرفيعة الممتدة في جميع أنحاء الجسم وتحتوي على سائل، ومن أهم وظائفها أنها تقوم بإلتقاط الخلايا الميتة والجراثيم، ثم يتم ترشيح هذا السائل للتخلص من العدوى.<br><br>2\. نخاع العظام<br><br>نخاع العظام هو عبارة عن نسيج لين موجود داخل العظام، ويحتوي على خلايا جذعية تنضج وتتطور لتكون خلايا الدم الحمراء والبيضاء والصفائح الدموية، وتتمثل وظيفة نخاع العظام في تكوين أجسام مناعية مع بقية مراكز المناعة لمحاربة العدوى والأمراض والجراثيم.<br><br>3\. الخلايا البالعة<br><br>لها اسم آخر وهي الخلايا الأكولة، وهي عبارة عن خلايا تقوم بتناول الجسم الغريب أو الميكروب الذي يلتصق بالأجسام المضادة، ثم تقوم بالتهام كافة الخلايا التي سقطت خلال معركة المقاومة بين الأجسام المضادة والميكروبات التي تهاجم الجسم لتنظفه.<br><br>4\. الأجسام المناعية المضادة<br><br>في حالة غزو الميكروبات للجسم، فهناك أجسام تعمل بمثابة قرون استشعار تدرك هذا الغزو الميكروبي لتبلغ بها الخلايا الليمفاوية لتحثها على إنتاج الأسلحة الدفاعية ضد هذه الميكروبات.<br><br>تتألف هذه الأسلحة من بروتينات وظيفتها الأساسية هي مقاومة الميكروبات التي تسبب تلف أنسجة الجسم، وهذه البروتينات تسمى الأجسام المناعية المضادة. |
| **Source** | <https://www.webteb.com/articles/%D9%83%D9%8A%D9%81-%D9%8A%D8%B9%D9%85%D9%84-%D8%AC%D9%87%D8%A7%D8%B2-%D8%A7%D9%84%D9%85%D9%86%D8%A7%D8%B9%D8%A9-%D9%81%D9%8A-%D8%A7%D9%84%D8%AC%D8%B3%D9%85_19542> |

### Science: Chemistry (General Domain)

The chemistry domain is a scientific discipline that focuses on the study of matter, its properties, composition, structure, and the changes it undergoes during chemical reactions. It explores the fundamental principles and theories that govern the behavior of atoms, molecules, and their interactions.

#### Possible subtopics could be but are not limited to

- **Atomic Structure**
- **التركيب الذري**
- **Organic chemistry**
- **الكيمياء العضوية**
- **Reactivity of Metals**
- **تفاعل المعادن**
- **Chemical Reaction Rates**
- **معدلات التفاعل الكيميائي**
- **Chemical Calculations**
- **الحسابات الكيميائية**
- **Chemical Analysis**
- **تحليل كيميائي**
- **Electrolysis**
- **التحليل الكهربائي**
- **Structure and Bonding**
- **Chemistry of the Atmosphere**
- **كيمياء الغلاف الجوي**
- **Organic Reactions**
- **التفاعلات العضوية**
- **Nature of matters**
- **Conceptual**: These questions/instructions assess understanding of fundamental concepts and principles in chemistry.
  - **Example**: What is the difference between an element and a compound?
- **المفاهيم**: تقوم هذه الأسئلة/التعليمات بتقييم فهم المفاهيم والمبادئ الأساسية في الكيمياء.
  - **مثال**: اذكر الفرق بين العنصر والمركب؟
- **Calculation**: Calculation questions/instructions involve performing mathematical calculations using chemical equations, stoichiometry, or other quantitative relationships.
  - **Example**: How many moles of oxygen gas are required to react with 2 moles of hydrogen gas to produce water?
- **الحساب**: تتضمن الأسئلة/التعليمات الحسابية إجراء عمليات حسابية باستخدام المعادلات الكيميائية أو قياس العناصر الكيميائية أو العلاقات الكمية الأخرى.
  - **مثال**: ما عدد مولات غاز الأكسجين اللازمة للتفاعل مع 2 مول من غاز الهيدروجين لإنتاج الماء؟
- **Laboratory**: These questions/instructions relate to laboratory techniques, experimental procedures, and data analysis.
  - **Example**: How would you separate a mixture of sand and salt?
- **المختبر**: تتعلق هذه الأسئلة/التعليمات بالتقنيات المخبرية والإجراءات التجريبية وتحليل البيانات.
  - **مثال**: كيف يمكنك فصل خليط من الرمل والملح؟
- **Reaction**: Reaction questions/instructions focus on understanding and predicting chemical reactions, including balancing chemical equations and identifying reaction products.
  - **Example**: Balance the following chemical equation: CH4 + O2 → CO2 + H2O.
- **التفاعل**: تركز أسئلة/تعليمات التفاعل على فهم التفاعلات الكيميائية والتنبؤ بها، بما في ذلك موازنة المعادلات الكيميائية وتحديد منتجات التفاعل.
  - **مثال**: زن المعادلة الكيميائية التالية: CH4 + O2 → CO2 + H2O.
- **Nomenclature**: Nomenclature questions/instructions involve naming compounds based on their chemical formulas or vice versa.
  - **Example**: What is the systematic name for the compound NaCl?
- **التسميات**: تتضمن أسئلة/تعليمات التسميات تسمية المركبات بناءً على صيغها الكيميائية أو العكس.
  - **مثال**: ما هو الاسم النظامي لمركب NaCl؟
- **Structural**: Structural questions/instructions relating to the understanding and interpretation of molecular structures, including drawing Lewis structures or identifying functional groups.
  - **Example**: Draw the Lewis structure for the molecule H2O.
- **الهيكلية**: الأسئلة/التعليمات الهيكلية المتعلقة بفهم وتفسير الهياكل الجزيئية، بما في ذلك رسم هياكل لويس أو تحديد المجموعات الوظيفية.
  - **مثال**: ارسم تركيب لويس لجزيء H2O.
- **Thermodynamics**: Thermodynamics questions/instructions study energy changes and heat flow in chemical reactions.
  - **Example**: Is a reaction spontaneous or non-spontaneous if the entropy change is positive and the enthalpy change is negative?
- **الديناميكا الحرارية**: أسئلة/تعليمات الديناميكا الحرارية تتناول دراسة تغيرات الطاقة وتدفق الحرارة في التفاعلات الكيميائية.
  - **مثال**: هل التفاعل عفوي أم غير تلقائي إذا كان تغير الانتروبيا موجباً وتغير الإنثالبي سالباً؟
- **Kinetics**: Kinetics questions/instructions focus on the rates of chemical reactions and factors that affect reaction rates.
  - **Example**: How does temperature affect the rate of a chemical reaction?
- **Acid-Base:** Acid-base questions/instructions involve understanding the properties, strengths, and reactions of acids and bases.
  - **Example**: Identify whether the following substance is an acid or a base: NH3 (ammonia).
- **حمض-قاعدة:** الأسئلة/التعليمات المتعلقة بالحمض-القاعدة تتضمن فهم خصائص ونقاط القوة و تفاعلات الأحماض والقواعد.
  - **مثال**: حدد هل المادة التالية حمض أم قاعدة: NH3 (الأمونيا).
- **Chemical Composition:** Chemical composition questions/instructions focus on the elements of a substance or compound and their respective ratios.
  - **Example**: What is the chemical composition of water (H2O), and what elements make up its structure?
- **التركيب الكيميائي:** تركز أسئلة/تعليمات التركيب الكيميائي على العناصر الموجودة في المادة أو المركب ونسب كل منها.
  - **مثال**: ما التركيب الكيميائي للماء (H2O)، وما العناصر التي تشكل تركيبه؟
- **Bonding and Molecular Structure:** Bonding and molecular structure questions/instructions explore the arrangement and nature of chemical bonds within molecules or compounds.
  - **Example**: What is the molecular structure of methane (CH4), and how are its carbon and hydrogen atoms bonded?
- **الترابط والبنية الجزيئية:** أسئلة/تعليمات الترابط والبنية الجزيئية تستكشف ترتيب وطبيعة الروابط الكيميائية داخل الجزيئات أو المركبات.
  - **مثال**: ما التركيب الجزيئي للميثان (CH4)، وكيف ترتبط ذرات الكربون والهيدروجين فيه؟
- **Periodicity and the Periodic Table:** The periodic table questions/instructions involve organizing elements in the periodic table, their properties, trends, and relationships.
  - **Example**: How does atomic radius change as you move from left to right across a period in the periodic table?
- **الدورية والجدول الدوري:** تتضمن أسئلة/تعليمات الدورية والجدول الدوري تنظيم العناصر في الجدول الدوري خصائصها واتجاهاتها وعلاقاتها.
  - **مثال**: كيف يتغير نصف القطر الذري عندما تتحرك من اليسار إلى اليمين خلال فترة زمنية في الجدول الدوري؟
- **Organic Chemistry:** Organic chemistry questions/instructions focus on the structure, properties, and reactions of organic compounds, which contain carbon atoms.
  - **Example**: What are the functional groups in alcohol, and how do they influence its chemical reactivity?
- **الكيمياء العضوية:** تركز أسئلة/تعليمات الكيمياء العضوية على بنية وخصائص وتفاعلات المركبات العضوية التي تحتوي على ذرات الكربون.
  - **مثال**: ما هي المجموعات الوظيفية في الكحول، وكيف تؤثر على تفاعلها الكيميائي؟
- **Materials Chemistry:** Materials chemistry questions/instructions focus on the design, characterization, and properties of materials, such as polymers, metals, ceramics, and composites.
  - **Example**: How can we modify the properties of a polymer to make it more flexible or heat-resistant?
- **كيمياء المواد:** تركز أسئلة/تعليمات كيمياء المواد على تصميم المواد وتوصيفها وخصائصها، مثل البوليمرات والمعادن والسيراميك والمواد المركبة.
  - **مثال**: كيف يمكننا تعديل خصائص البوليمر لجعله أكثر مرونة أو مقاومة للحرارة؟

#### Instructions could be, but not limited to

- **Explain**
- **اشرح** ما هو التفاعل الكيميائي
- **Define** xxxx
- **عرف** النظائر؟
- **Describe** the
- **صف** هيكل ثاني أكسيد السيليكون
- **What is** ….?
- **ما هو** المركب العضوي
- **List**
- **أعطني قائمة** بمركبات الكربون
- **Discuss the importance of**
- **ناقش أهمية** الميثانول
- **Outline the steps of** ……….
- **ما هي خطوات** موازنة المعادلة الكيميائية؟
- **Compare between** ……… and ………….
- **قارن بين** الأحماض والقاعدة
- **Provide examples of** ……….
- **قدم أمثلة على** المركبات العضوية
- **Summarize the following paragraph**
- **لخص الفقرة التالية**
- **Calculate**
  - When 10.0 g pure calcium carbonate is heated and converted to solid calcium oxide CaO, how much calcium oxide should be obtained? If only 5.0 grams of CaO is obtained, what is the actual yield?
- **Outline the steps of**
- **حدد خطوات** موازنة المعادلة الكيميائية التالية: N2 + H2 → NH3
- **Is the following statement correct** about …………...
- **هل العبارة التالية صحيحة بخصوص** …………...
- **Choose the correct answers from the following list**
- **أي العناصر التالية** هي الأكثر والأقل سالبية كهربية في الجدول الدوري؟
  - \[أ\] الفلور والسيزيوم
  - \[ب\] الهيدروجين والهيليوم
  - \[ج\] الكربون والأكسجين
  - \[د\] الكلور والفلور

#### Examples

**Example 1**

| **Instruction** | ما هي الذرات؟ |
| --- | --- |
| **Input** |     |
| **Output** | الذرة هي أصغر حجر بناءٍ أو أصغر جزء من العنصر الكيميائي يمكن الوصول إليه والذي يحتفظ بالخصائص الكيميائية لذلك العنصر. يرجع أصل الكلمة الإنجليزية (بالإنجليزية: Atom)‏ إلى الكلمة الإغريقية أتوموس، والتي تعني غير القابل للانقسام؛ إذ كان يعتقد أنه ليس ثمة ما هو أصغر من الذرة. تتكون الذرة من سحابة من الشحنات السالبة (الإلكترونات) التي تدور حول نواة موجبة الشحنة صغيرة جدًا في المركز، وتتكون النواة من بروتونات موجبة الشحنة، ونيوترونات متعادلة، وتعدّ الذرة هي أصغر جزء من العنصر يمكن أن يتميز به عن بقية العناصر؛ إذ كلما غصنا أكثر في المادة لنلاقي البنى الأصغر لن يعود هناك فرق بين عنصر وآخر. فمثلاً، لا فرق بين بروتون في ذرة حديد وبروتون آخر في ذرة يورانيوم مثلًا، أو ذرة أي عنصرٍ آخر. الذرة، بما تحمله من خصائص؛ عدد بروتوناتها، كتلتها، توزيعها الإلكتروني... تصنع الفروقات بين العناصر المختلفة، وبين الصور المختلفة للعنصر نفسه (المسماة بالنظائر)، وحتى بين كَون هذا العنصر قادرًا على خوض تفاعل كيميائي ما أم لا.<br><br>ظل وما زال تركيب الذرة وما يجري في هذا العالم البالغ الصغر يشغل العلماء ويدفعهم إلى اكتشاف المزيد. ومن هنا أخذت تظهر فروع جديدة في العلم حاملة معها مبادئها ونظرياتها الخاصة بها، بدءًا بمبدأ عدم التأكد (اللاثقة)، مرورًا بنظريات التوحيد الكبرى، وانتهاءً بنظرية الأوتار الفائقة. الذرة اصغر من الجزيء ويمكن لذرتين أو أكثر تكوين جزيء. |
| **Source** | <https://ar.wikipedia.org/wiki/%D8%B0%D8%B1%D8%A9> |

**Example 2**

| **Instruction** | اختر الإجابة الصحيحة مما يلي: |
| --- | --- |
| **Input** | النظام الدولي للوحدات<br><br>(وحدة SI) لدرجة الحرارة هي:<br><br>(أ) فهرنهايت<br><br>(ب) مئوية<br><br>(ج) كلفن<br><br>(د) درجة مئوية |
| **Output** | (ج) كلفن<br><br>شرح: الكلفن هو أحد الوحدات الأساسية السبعة للنظام الدولي للوحدات (SI) ويستخدم لقياس درجة الحرارة الديناميكية الحرارية. قمنا بتعيين وحدة أخرى لدرجة الحرارة، وهي الدرجة المئوية (°C)، في النظام الدولي للوحدات (SI)، وهو أمر غير معتاد. |
| **Source** | <https://byjus.com/chemistry/chemical-formula-questions/> |

### Science: Math (General Domain)

#### Description

General. Relates to mathematics and calculations.

Math is a field of study that deals with the properties, relationships, and operations of numbers, quantities, shapes, and patterns. It provides a structured and logical framework for understanding and solving problems using precise mathematical language and notation.

#### Possible subtopics

- **Solving equations.**
- **حل المعادلات.**
- **Solving problems.**
- **حل المشاكل.**
- **Conversions (e.g., units)**
- **التحويلات (مثل الوحدات)**
- **Mathematical Logic**
  - How do you reason with logical statements and identify valid arguments?
  - How do you study the foundations and consistency of mathematical systems?
- **المنطق الرياضي**
  - كيف يمكنك التفكير باستخدام العبارات المنطقية وتحديد الحجج الصحيحة؟
  - كيف يمكنك دراسة أسس واتساق النظم الرياضية؟
- **Probability**
  - How do you calculate the likelihood of events in uncertain situations?
- **احتمالات**
  - كيف تحسب احتمالية الأحداث في المواقف غير المؤكدة؟
- **Geometry**
  - What are the properties and relationships of different geometric shapes and figures?
  - How do you calculate areas, volumes, and angles?
  - How do you use geometric theorems and postulates to prove statements about shapes?
- **Algebra**
  - How do you solve equations and inequalities?
  - What are the properties and operations of variables and expressions?
  - How do you graph and analyze linear and quadratic functions?
- **Arithmetic**
  - How do you add, subtract, multiply, and divide numbers?
  - What are the properties of different number systems, such as whole numbers, fractions, and decimals?
  - How do you solve basic word problems involving quantities and operations?
- **Computational**: These questions/instructions involve performing calculations or applying specific formulas or algorithms.
  - **Example:** What is the value of 3 multiplied by 7?
- **الحسابية:** تتضمن هذه الأسئلة/التعليمات إجراء عمليات حسابية أو تطبيق صيغ أو خوارزميات محددة.
  - **مثال:** ما قيمة 3 مضروبة في 7؟
- **Word** **Problems**: Word problems present real-life scenarios that require mathematical reasoning and problem-solving skills to find a solution.
  - **Example:** If John has five apples and gives 2 to his friend, how many apples does John have left?
- **مشاكل الكلمات:** تقدم مشاكل الكلمات سيناريوهات من الحياة الواقعية تتطلب تفكيرًا رياضيًا ومهارات حل المشكلات لإيجاد حل.
  - **مثال:** إذا كان لدى جون خمس تفاحات وأعطى اثنتين لصديقه، فكم عدد التفاحات المتبقية لدى جون؟
- **Conceptual**: These questions/instructions assess understanding of mathematical concepts, principles, and relationships.
  - **Example:** What is the difference between a square and a rectangle?
- المفاهيمي: تقوم هذه الأسئلة/التعليمات بتقييم فهم المفاهيم والمبادئ والعلاقات الرياضية.
  - **مثال:** ما الفرق بين المربع والمستطيل؟
- **Procedural**: Procedural questions/instructions test knowledge and application of specific mathematical procedures or algorithms.
  - **Example:** Simplify the expression 2(x + 3) - 5x.
- **إجرائي:** أسئلة/تعليمات إجرائية تختبر المعرفة وتطبيق إجراءات أو خوارزميات رياضية محددة.
  - **مثال:** بسّط التعبير
- **Proof** **or** **Theoretical**: These questions/instructions require logical reasoning and evidence to prove or disprove a mathematical statement or theorem.
  - **Example:** Prove that the sum of two even numbers is always even.
- **إثبات أو نظري:** تتطلب هذه الأسئلة/التعليمات تفكيرًا منطقيًا وأدلة لإثبات أو دحض عبارة أو نظرية رياضية.
  - **مثال:** أثبت أن مجموع رقمين زوجيين هو دائمًا زوجي.
- **Problem-Solving**: Problem-solving questions/instructions involve analyzing a complex situation and devising a strategy to find a solution.
  - **Example:** A train travels at 60 km/h for 2 hours, then increases its speed to 80 km/h for the next 3 hours. What is the total distance traveled by the train?
- **حل المشكلات:** تتضمن أسئلة/تعليمات حل المشكلات تحليل موقف معقد ووضع استراتيجية لإيجاد حل.
  - **مثال:** يسافر قطار بسرعة 60 كم/ساعة لمدة ساعتين، ثم يزيد سرعته إلى 80 كم/ساعة خلال الثلاث ساعات التالية. ما هي المسافة الإجمالية التي قطعها القطار؟
- **Application**: Application questions/instructions involve using mathematical concepts and techniques to solve problems in real-world contexts.
  - **Example:** A store offers a 20% discount on all items. If an item originally costs $50, what is the sale price after the discount?
- **التطبيق:** تتضمن أسئلة/تعليمات التطبيق استخدام المفاهيم والتقنيات الرياضية لحل المشكلات في سياقات العالم الحقيقي.
  - مثال: يقدم أحد المتاجر خصمًا بنسبة 20% على جميع العناصر. إذا كانت تكلفة السلعة في الأصل 50 دولارًا، فما هو سعر البيع بعد الخصم؟

#### Instruction could be, but not limited to

- **Define** ….
- **عرِّف** ….
- **Give steps to** solve this math equation…….
- **اعطي خطوات** حل هذه المعادلة الرياضية......
- **Calculate** ……….
- **احسب** ……….
- **Convert the following** … from g to kg
- **حوًل ما يلي**... من g إلى كجم
- **Find the area of** a rectangle with length …. meters and width …. Meters.
- **أوجد مساحة** المستطيل بطول .... متر وعرض .... متر.
- **Simplify the expression:** …………..
- **Evaluate the expression:**..................
- **Find the volume of a** …………………..
- **أوجد حجم** ...............
- **Solve the system of equations:** ………………..
- **حل نظام المعادلات**: ………………..
- **Select correct answer**
  - What is the value of 6 + 3?
    - a) 4
    - b) 7
    - c) 9
    - d) 10
  - ما قيمة 6 + 3؟
    - أ) 4
    - ب) 7
    - ج) 9
    - د) 10

- You go to the market and buy material for three dresses. If each dress requires 2/3 m of fabric, use multiplication and calculate the length of the cloth purchased. Write your answer below.
- تذهب إلى السوق وتشتري مواد لـ 3 فساتين. إذا كان كل فستان يتطلب 2/3 م القماش، استخدم الضرب واحسب طول القماش الذي اشتريته. اكتب إجابتك أدناه.
- **Write a formula for the given measure**. The perimeter of a rectangle is …. inches, with a length and width of 'x' and 'y' inches.
- **اكتب صيغة للقياس المعطى**. محيط المستطيل هو .... بوصة، بطول وعرض "x" و"y" بوصة.
- **Create a step-by-step guide on** solving …….. Include examples and explanations of different methods, such as the balance method or using inverse operations, to help readers understand the process.
- **إنشاء دليل خطوة بخطوة** لحل …….. يتضمن أمثلة وشروحات لطرق مختلفة، مثل طريقة التوازن أو استخدام العمليات العكسية، لمساعدة القراء على فهم العملية.
- **Write an article on** ………………..
- **أكتب مقالاً عن** ...............
- **Create a set of** practice problems and solutions on ………………
- **قم بإنشاء** مجموعة من المشكلات التدريبية والحلول حول ...............

#### Examples

**Example 1**

| **Instruction** | نقطة المنتصف للقطعة المستقيمة التي تصل بين النقطتين A(2,4) و B(-2,-4) هي |
| --- | --- |
| **Input** | (أ) (-2، 4)<br><br>(ب) (2، -4)<br><br>(ج) (0، 0)<br><br>(د) (-2، -4) |
| **Output** | الجواب: (ج) (0، 0)<br><br>شرح: حسب صيغة نقطة المنتصف، نحن نعلم؛<br><br>إحداثي x لنقطة المنتصف = \[2 + (-2)\]/2 = 0/2 = 0<br><br>إحداثي y لنقطة المنتصف = \[4 + (-4)\]/2=0/2=0<br><br>ومن ثم، (0، 0) هي نقطة منتصف AB. |
| **Source** | <https://byjus.com/maths/class-10-maths-mcqs-chapter-7-coordinate-geometry/> |

####

**Example 2**

| **Instruction** | أشرح الدوال المثلثية |
| --- | --- |
| **Input** |     |
| **Output** | تُعرف الدوال المثلثية أيضًا باسم الدوال الدائرية ويمكن تعريفها ببساطة على أنها دوال زاوية المثلث. وهذا يعني أن العلاقة بين زوايا المثلث وأضلاعه تعطى من خلال هذه الدوال المثلثية. الوظائف المثلثية الأساسية هي جيب التمام، وجيب التمام، والظل، وظل التمام، والقاطع، وقاطع التمام.<br><br>هناك عدد من الصيغ والمتطابقات المثلثية التي تشير إلى العلاقة بين الوظائف وتساعد في العثور على زوايا المثلث. تم شرح كل هذه الدوال المثلثية مع صيغتها هنا بشكل مفصل، لجعلها مفهومة للقراء.<br><br>كما ستصادف الجدول الذي تم فيه ذكر قيمة هذه النسب لبعض الدرجات المحددة. وبناءً على هذا الجدول ستتمكن من حل العديد من الأمثلة والمسائل المثلثية.<br><br>ست وظائف المثلثية<br><br>زوايا الجيب وجيب التمام والظل هي التصنيف الأساسي لوظائف علم المثلثات. ويمكن استخلاص الوظائف الثلاث، وهي ظل التمام والقاطع وقاطع التمام، من الوظائف الأساسية. في الأساس، غالبًا ما يتم استخدام الدوال الثلاث الأخرى مقارنةً بالدوال المثلثية الأساسية. خذ بعين الاعتبار الرسم البياني التالي كمرجع لشرح هذه الوظائف الأساسية الثلاث. يمكن الإشارة إلى هذا المخطط باسم مثلث sin-cos-tan. عادةً ما نحدد علم المثلثات بمساعدة المثلث القائم الزاوية.<br><br>وظيفة جيبية<br><br>دالة الجيب للزاوية هي النسبة بين طول الضلع المقابل وطول الوتر. من الرسم البياني أعلاه، قيمة الخطيئة ستكون:<br><br>Sin a = الوتر/الوتر = CB/CA<br><br>وظيفة كوس<br><br>جيب تمام الزاوية هو نسبة طول الضلع المجاور إلى طول الوتر. من الرسم البياني أعلاه، سيتم اشتقاق وظيفة cos على النحو التالي.<br><br>كوس أ = المجاور/الوتر = AB/CA<br><br>وظيفة تان<br><br>دالة الظل هي نسبة طول الضلع المقابل إلى طول الضلع المجاور. تجدر الإشارة إلى أنه يمكن أيضًا تمثيل tan بدلالة الجيب وcos كنسبة لهما. من الرسم البياني أعلاه، ستكون وظيفة tan على النحو التالي.<br><br>Tan a = المقابل/المجاور = CB/BA<br><br>أيضًا، من حيث الجيب وcos، يمكن تمثيل tan على النحو التالي:<br><br>Tan a = sin a/cos a<br><br>وظائف القاطع وقاطع التمام وظل التمام<br><br>القاطع وقاطع التمام (csc) وظل التمام هي الوظائف الإضافية الثلاثة المشتقة من الوظائف الأساسية للجيب وcos وtan. مقلوب الجيب وcos وtan هو قاطع التمام (csc) والقاطع (sec) وظل التمام (cot) على التوالي. يتم إعطاء صيغة كل من هذه الوظائف على النحو التالي:<br><br>ثانية أ = 1/(كوس أ) = الوتر/المجاور = CA/AB<br><br>Cosec a = 1/(sin a) = الوتر/المعاكس = CA/CB<br><br>سرير أ = 1/(ظا أ) = مجاور/مقابل = BA/CB<br><br>ملحوظة: تستخدم الدوال المثلثية العكسية للحصول على زاوية من أي من النسب المثلثية للزاوية. في الأساس، يتم تمثيل معكوس وظائف الجيب، وجيب التمام، والظل، وظل التمام، والقاطع، وقاطع التمام على شكل قوس جيب التمام، وأركوسين، وظل قوسي، وظل التمام القوسي، وقاطع القوس، وقاطع التمام القوسي.<br><br>المتطابقات<br><br>فيما يلي الهويات المتعلقة بوظائف المثلثات.<br><br>الوظائف الزوجية والفردية<br><br>الدوال cos وsec هي دوال زوجية؛ بقية الوظائف الأخرى هي وظائف غريبة.<br><br>الخطيئة (-x) = -الخطيئة س<br><br>كوس(-س) = كوس س<br><br>ظا(-س) = – ظا س<br><br>المهد(-س) = -المهد س<br><br>csc(-x) = -csc x<br><br>ثانية(-x) = ثانية س<br><br>الوظائف الدورية<br><br>الدوال المثلثية هي الدوال الدورية. أصغر دورة دورية هي 2π ولكن بالنسبة للظل وظل التمام فهي π.<br><br>الخطيئة(س+2نπ) = الخطيئة س<br><br>cos(x+2nπ) = cos x<br><br>ظا(x+nπ) = ظا x<br><br>سرير الأطفال(x+nπ) = سرير الأطفال x<br><br>csc(x+2nπ) = csc x<br><br>ثانية(x+2nπ) = ثانية س<br><br>حيث n هو أي عدد صحيح.<br><br>هويات فيثاغورس<br><br>عندما يتم التعبير عن نظرية فيثاغورس في شكل دوال علم المثلثات، يقال إنها هوية فيثاغورس. هناك ثلاث هويات رئيسية:<br><br>sin2 x + cos2 x = 1 \[مهم جدًا\]<br><br>1+tan2x = ثانية2x<br><br>cosec2 x = 1 + cot2 x<br><br>ولهذه المتطابقات الثلاث أهمية كبيرة في الرياضيات، حيث يتم إعداد معظم أسئلة علم المثلثات في الامتحانات بناءً عليها. ولذلك، يجب على الطلاب حفظ هذه الهويات لحل مثل هذه المشاكل بسهولة.<br><br>هويات المجموع والفرق<br><br>الخطيئة(x+y) = الخطيئة(x).cos(y)+cos(x).sin(y)<br><br>الخطيئة (x – y) = الخطيئة (x).cos (y) –cos (x).sin (y)<br><br>cos(x+y) = cosx.cosy–sinx.siny<br><br>cos(x–y) = cosx.cosy+sinx.siny<br><br>tan(x+y) = \[tan(x)+tan(y)\]/\[1-tan(x)tan(y)\]<br><br>tan(x-y) = \[tan(x)-tan(y)\]/\[1+tan(x)tan(y)\] |
| **Source** | <https://byjus.com/maths/trigonometric-functions/> |

**Example 3**

| **Instruction** | تشتري بعض الخيوط من السوق. يتم بيعها في عبوات 1/2 كجم. تحتاج إلى 4 كجم و1/2<br><br>من الغزل. حدد عدد العبوات التي تحتاجها. |
| --- | --- |
| **Input** |     |
| **Output** | 9 packets |
| **Source** |     |

### Science: Astronomy (General Domain)

The astronomy domain encompasses the scientific study of celestial objects, such as stars, planets, galaxies, and other celestial phenomena, as well as the physical processes that occur in the universe. It involves the observation, measurement, and analysis of astronomical objects and their interactions through various instruments, including telescopes, spectrographs, and space probes.

#### It encompasses various subfields, including but not limited to the following

- G**alaxies, Planets, Different stars**
  - **Earth, Venus, solar system, Milky Way galaxy**
- **المجرات والكواكب و النجوم المختلفه**
  - **الأرض، الزهرة، النظام الشمسي، مجرة ​​درب التبانة**
- **COMETS, ASTEROIDS & METEORS**
- **المذنبات والكويكبات والنيازك**
- **Cosmology**
- **علم الكونيات**
- **Astrophotography**
- **التصوير الفلكي**
- **Equipment: telescopes**
- **المعدات: التلسكوبات**
- **Black holes**
- **الثقوب السوداء**
- **Dark matter**
- **المادة المظلمة**
- **Bing bang theory**
- **نظريه نشاه الكون**
- **Dark energy**
- **الطاقة المظلمة**
- **Observational**: These questions/instructions involve the observation and measurement of celestial objects and phenomena.
  - **Example**: What is the apparent magnitude of a particular star?
- **المراقبة**: تتضمن هذه الأسئلة/التعليمات مراقبة وقياس الأجرام والظواهر السماوية.
  - **مثال**: ما هو القدر الظاهري لنجم معين؟
- **Morphological**: Morphological questions/instructions pertain to the shape, structure, and characteristics of celestial objects.
  - **Example**: What is the shape and structure of a spiral galaxy?
- **المورفولوجية**: الأسئلة/التعليمات المورفولوجية تتعلق بشكل وبنية وخصائص الأجرام السماوية.
  - **مثال**: ما هو شكل وبنية المجرة الحلزونية؟
- **Spectral**: Spectral questions/instructions involve the analysis and interpretation of the electromagnetic spectra emitted or absorbed by celestial objects.
  - **Example**: What are the spectral features and composition of a particular star?
- **الطيفية**: تتضمن الأسئلة/التعليمات الطيفية تحليل وتفسير الأطياف الكهرومغناطيسية المنبعثة أو الممتصة من الأجرام السماوية.
  - **مثال**: ما هي السمات الطيفية وتكوين نجم معين؟
- **Cosmological**: Cosmological questions/instructions explore the nature, origin, and evolution of the universe as a whole.
  - **Example**: What is the age of the universe, and how has it evolved over time?
- **الكونية**: تستكشف الأسئلة/التعليمات الكونية طبيعة الكون وأصله وتطوره ككل.
  - **مثال**: ما هو عمر الكون، وكيف تطور مع مرور الوقت؟
- **Planetary**: Planetary questions/instructions focus on studying planets, their orbits, atmospheres, geological features, and potential for life.
  - **Example**: What is the composition and structure of the atmosphere of a specific planet?
- **الكواكب**: تركز الأسئلة/التعليمات المتعلقة بالكواكب على دراسة الكواكب ومداراتها وأغلفتها الجوية وخصائصها الجيولوجية وإمكانات الحياة.
  - **مثال**: ما هو تكوين وبنية الغلاف الجوي لكوكب معين؟
- **Stellar**: Stellar questions/instructions involve the study of stars, their properties, life cycles, and interactions.
  - **Example**: How does the mass of a star affect its life span and eventual fate?
- **النجمية** : تتضمن الأسئلة/التعليمات النجمية دراسة النجوم وخصائصها ودورات حياتها وتفاعلاتها.
  - **مثال**: كيف تؤثر كتلة النجم على مدة حياته ومصيره النهائي؟
- **Galactic**: Galactic questions/instructions for studying galaxies, their formation, structure, and dynamics.
  - **Example**: How do galaxies form and evolve over time?
- **المجرة**: أسئلة/تعليمات عن المجرة تتعلق بدراسة المجرات وتكوينها وبنيتها وديناميكيتها.
  - **مثال**: كيف تتشكل المجرات وتتطور مع مرور الوقت؟
- **Exoplanet**: Exoplanet questions/instructions explore the detection, characterization, and habitability of planets outside our solar system.
  - **Example**: What are the properties and potential habitability of an exoplanet?
- **الكواكب الخارجية** : أسئلة/تعليمات الكواكب الخارجية اكتشاف الكواكب خارج نظامنا الشمسي وتوصيفها وصلاحيتها للسكن.
  - **مثال**: ما هي الخصائص وإمكانية السكن لكوكب خارج المجموعة الشمسية؟
- **Gravitational**: Gravitational questions/instructions involve the understanding and application of gravitational forces and their effects on celestial objects.
  - **Example**: How does gravitational lensing occur, and what can it tell us about distant objects?
- **الجاذبية**: تتضمن أسئلة/تعليمات الجاذبية فهم وتطبيق قوى الجاذبية وتأثيراتها على الأجرام السماوية.
  - **مثال**: كيف تحدث عدسة الجاذبية، وماذا يمكن أن تخبرنا عن الأجسام البعيدة؟
- **Astronomical Instrumentation and Techniques:** Astronomical instrumentation and techniques questions/instructions focus on the development and use of telescopes, detectors, and data analysis methods in observational astronomy.
  - **Example**: How do astronomers use adaptive optics to correct for atmospheric distortions and obtain sharper images of celestial objects?
- **الأجهزة والتقنيات الفلكية:** تركز أسئلة/تعليمات الأجهزة والتقنيات الفلكية على تطوير واستخدام التلسكوبات وأجهزة الكشف وطرق تحليل البيانات في علم الفلك الرصدي.
  - **مثال**: كيف يستخدم علماء الفلك البصريات التكيفية لتصحيح التشوهات الجوية والحصول على صور أكثر وضوحًا للأجرام السماوية؟
- **Astrobiology and the Search for Extraterrestrial Life:** Astrobiology questions/instructions explore the conditions necessary for life to exist, the potential habitability of other planets and moons, and the search for signs of life beyond Earth.
  - **Example**: What criteria are used to determine if a planet or moon is potentially habitable, and how do scientists search for biosignatures in exoplanet atmospheres?
- **علم الأحياء الفلكي والبحث عن حياة خارج كوكب الأرض:** تستكشف أسئلة/تعليمات علم الأحياء الفلكي الظروف اللازمة لوجود الحياة، وقابلية السكن المحتملة للكواكب والأقمار الأخرى، والبحث عن علامات الحياة خارج الأرض.
  - **مثال**: ما هي المعايير المستخدمة لتحديد ما إذا كان الكوكب أو القمر صالحًا للسكن، وكيف يبحث العلماء عن البصمات الحيوية في أجواء الكواكب الخارجية؟
- **Galactic Structure and Dynamics:** Galactic structure and dynamics questions/instructions examine the structure, motion, and interactions of galaxies, including their spiral arms, central black holes, and interactions with other galaxies.
  - **Example**: How do astronomers study the rotation curves of galaxies to infer the presence of dark matter?
- **بنية المجرة وديناميكياتها:** أسئلة/تعليمات تتعلق ببنية المجرة وديناميكياتها تدرس بنية المجرات وحركتها وتفاعلاتها، بما في ذلك أذرعها الحلزونية والثقوب السوداء المركزية والتفاعلات مع المجرات الأخرى.
  - **مثال**: كيف يدرس علماء الفلك منحنيات دوران المجرات لاستنتاج وجود المادة المظلمة؟
- **High-Energy Astrophysics:** High-energy astrophysics questions /instructions explore phenomena involving high-energy particles and radiation, such as supernovae, gamma-ray bursts, and active galactic nuclei.
  - **Example**: What are the mechanisms responsible for the emission of gamma-ray bursts, and what can they tell us about the most energetic events in the universe?
- **الفيزياء الفلكية عالية الطاقة:** تستكشف أسئلة/تعليمات الفيزياء الفلكية عالية الطاقة الظواهر التي تتضمن جسيمات وإشعاعات عالية الطاقة، مثل المستعرات الأعظم وانفجارات أشعة جاما ونواة المجرة النشطة.
  - **مثال**: ما هي الآليات المسؤولة عن انبعاث انفجارات أشعة غاما، وماذا يمكن أن تخبرنا عن الأحداث الأكثر نشاطا في الكون؟
- **Dark Matter and Dark Energy:** Dark matter and dark energy questions/instructions investigate the nature and properties of these mysterious components that make up a significant portion of the universe yet remain largely unknown.
  - **Example**: What observational evidence supports the existence of dark matter and dark energy, and what are their implications for the structure and expansion of the universe?
- **المادة المظلمة والطاقة المظلمة:** أسئلة/تعليمات حول المادة المظلمة والطاقة المظلمة تبحث في طبيعة وخصائص هذه المكونات الغامضة التي تشكل جزءًا كبيرًا من الكون ولكنها تظل غير معروفة إلى حد كبير.
  - **مثال**: ما هي الأدلة الرصدية التي تدعم وجود المادة المظلمة والطاقة المظلمة، وما آثارها على بنية الكون وتوسعه؟

####

#### Instructions could be, but not limited to

- **Describe**………
- **صف** مجرة ​​درب التبانة
- **List** planets in ……….. galaxy
- **اعطني قائمة ل** الكواكب في مجرة ​​ويرلبول
- Could we travel to ……… in ……….. years
- **هل** يمكننا السفر إلى ………… في ……. سنوات
- **Whats is** xxx telescope
- **ما هو** التلسكوب …………
- **True or false about statement**
- **هل يمكن** للنجم أن يتحول إلى كوكب؟
- **Recommend** a book/ article about ……….
- **اقترح** كتاب / مقال حول …………..
- **Discuss** the drawbacks of space exploration
- **ناقش** عيوب استكشاف الفضاء
- **Define** …………..
- **Summarize the following article**
- **Classify the following** as galaxies or planets or moon or stars.
  - Input: earth, nebula, Red dwarf
- **صنف ما يلي إلى** مجرات أو كواكب أو قمر أو نجوم.
  - الأرض، السديم، القزم الأحمر
- **Compare between** ………. and …………….
- **قارن بين** النيازك والكويكبات

#### Examples

**Example 1**

| **Instruction** | هل سنسافر يوما ما إلى النجوم؟ |
| --- | --- |
| **Input** |     |
| **Output** | السفر إلى النجوم أمر صعب للغاية لأنها بعيدة جدًا. أقرب نجم يبعد عنا 25,300,000,000,000 ميل (حوالي 39,900,000,000,000 كيلومتر). سوف يستغرق الأمر أسرع الصواريخ التي لدينا آلاف السنين للوصول إليها. من الممكن دائمًا أن يجد الناس في وقت ما في المستقبل طريقة للسفر إلى النجوم، لكن في الوقت الحالي لا نملك التكنولوجيا. |
| **Source** | <https://coolcosmos.ipac.caltech.edu/asks> |

**Example 2**

| **Instruction** | اعطيني اسماء اقمار كوكب زحل |
| --- | --- |
| **Input** |     |
| **Output** | هناك 82 قمراً معروفاً يدور حول زُحل تسعة منها أقطارها أكبر من (200 كيلومتر) وتلك الأقمار الرئيسية هي ميماس، إنسيلادوس، تيثيس، ديون، ريا، تيتان، هايبريون، إيبتوس، وفيبي وقد تم اكتشاف كل منهم قبل القرن العشرين وتم اكتشاف بقية الأقمار في أواخر القرن العشرين أو أوائل القرن الحادي والعشرين. ويطلق على أقمار زُحل الداخلية اسم منتظم لأنها تدور في مسارات دائرية تقريبًا في مستوى مدار زُحل أو بالقرب منه وتشمل الأقمار الداخلية جميع أقمار زُحل الرئيسية باستثناء فيبي بالإضافة إلى عشرات الأقمار الأخرى أما الأقمار الخارجية للكوكب فهي غير منتظمة ولها مدارات شديدة الاستطالة، ويعد قمر تيتان من أكبر أقمار كوكب زُحل ويتميز بغلافه الجوي الثخين وهو القمر الوحيد في النظام الشمسي المعروف بوجود غلاف جوي كثيف وسحب. |
| **Source** | <https://www.twinkl.com.eg/teaching-wiki/zhl#:~:text=%D8%A3%D9%82%D9%85%D8%A7%D8%B1%20%D9%83%D9%88%D9%83%D8%A8%20%D8%B2%D9%8F%D8%AD%D9%84,%D8%A3%D9%88%20%D8%A3%D9%88%D8%A7%D8%A6%D9%84%20%D8%A7%D9%84%D9%82%D8%B1%D9%86%20%D8%A7%D9%84%D8%AD%D8%A7%D8%AF%D9%8A%20%D9%88%D8%A7%D9%84%D8%B9%D8%B4%D8%B1%D9%8A%D9%86>. |

### Technology (General Domain)

The technology domain refers to the broad field of knowledge, practices, and applications related to using scientific and engineering principles to create, develop, and implement various tools, systems, and processes to solve problems, improve efficiency, and enhance human experiences. It encompasses a wide range of subtopics, including but not limited to

#### Possible subtopics could be but are not limited to

- **Mechanics**
- **علم الميكانيكا**
- **Electronics**
- **إلكترونيات**
- **AI**
- **Robotics**
- **الروبوتات**
- **CPUs, GPUs, Mobile phones**
- **وحدات المعالجة المركزية ووحدات معالجة الرسومات والهواتف المحمولة**
- **Companies**
- **الشركات التكنولوجية**
- **Technological news**
- **الأخبار التكنولوجية**
- **Virtual Reality (VR), Augmented Reality (AR)**
- **الواقع الافتراضي (VR)، الواقع المعزز (AR)**
- **Nanotechnology**
- **Design**: Design questions/instructions focus on creating and improving technological solutions, products, or systems.
  - **Example**: How can we design a more efficient and user-friendly interface for a mobile application?
- **التصميم**: تركز أسئلة/تعليمات التصميم على إنشاء وتحسين الحلول أو المنتجات أو الأنظمة التكنولوجية.
  - **مثال**: كيف يمكننا تصميم واجهة أكثر كفاءة وسهلة الاستخدام لتطبيق الهاتف المحمول؟
- **Technical Troubleshooting:** Troubleshooting questions/instructions involve identifying and resolving technical issues or problems in hardware, software, or systems.
  - **Example**: How can we diagnose and fix a network connectivity problem in a computer network?
- **استكشاف الأخطاء وإصلاحها الفنية:** تتضمن أسئلة/تعليمات استكشاف الأخطاء وإصلاحها تحديد وحل المشكلات أو المشكلات الفنية في الأجهزة أو البرامج أو الأنظمة.
  - **مثال**: كيف يمكننا تشخيص مشكلة الاتصال بالشبكة في شبكة الكمبيوتر وإصلاحها؟
- **Technological News and Current Events:** Technological news and current events questions/instructions involve staying updated on the latest developments, product launches, acquisitions, and notable events in the world of technology.
  - **Example**: What are the recent advancements in renewable energy technologies and their implications for addressing climate change?
- **الأخبار التكنولوجية والأحداث الجارية**: تتضمن أسئلة/تعليمات الأخبار التكنولوجية والأحداث الجارية البقاء على اطلاع بآخر التطورات، وإطلاق المنتجات، وعمليات الاستحواذ، والأحداث البارزة في عالم التكنولوجيا.
  - **مثال**: ما هي التطورات الحديثة في تقنيات الطاقة المتجددة وآثارها على معالجة تغير المناخ؟
- **Security**: Security questions/instructions revolve around protecting data, networks, and systems from unauthorized access, breaches, or vulnerabilities.
  - **Example**: How can we enhance the security of an e-commerce website to protect customer information?
- **الأمان**: تدور أسئلة/تعليمات الأمان حول حماية البيانات والشبكات والأنظمة من الوصول غير المصرح به أو الانتهاكات أو نقاط الضعف.
  - **مثال**: كيف يمكننا تعزيز أمان موقع التجارة الإلكترونية لحماية معلومات العملاء؟
- **Emerging Technologies:** Emerging technologies questions/instructions examine new and emerging fields, such as blockchain, virtual reality, augmented reality, Internet of Things (IoT), and their potential impact on various industries.
  - **Example**: What are the potential applications of blockchain technology beyond cryptocurrencies?
- **التقنيات الناشئة**: تدرس أسئلة/تعليمات التقنيات الناشئة المجالات الجديدة والناشئة، مثل blockchain، والواقع الافتراضي، والواقع المعزز، وإنترنت الأشياء (IoT)، وتأثيرها المحتمل على مختلف الصناعات.
  - **مثال**: ما هي التطبيقات المحتملة لتقنية blockchain خارج نطاق العملات المشفرة؟
- **Ethical and Social Implications of Technology:** Ethical and social implications of technology questions/instructions delve into the ethical dilemmas and societal impacts of technological advancements, considering issues like privacy, security, bias, and job displacement.
  - **Example**: How can we ensure the ethical use of facial recognition technology while addressing concerns related to privacy and potential bias?
- **الآثار الأخلاقية والاجتماعية للتكنولوجيا:** تتعمق الآثار الأخلاقية والاجتماعية لأسئلة/تعليمات التكنولوجيا في المعضلات الأخلاقية والآثار المجتمعية للتقدم التكنولوجي، مع الأخذ في الاعتبار قضايا مثل الخصوصية والأمن والتحيز وإزاحة الوظائف.
  - **مثال**: كيف يمكننا ضمان الاستخدام الأخلاقي لتقنية التعرف على الوجه مع معالجة المخاوف المتعلقة بالخصوصية والتحيز المحتمل؟
- **Technological Impact on Industries:** Technological impact on industries questions/instructions address how technology is transforming various sectors, such as healthcare, finance, transportation, manufacturing, and entertainment.
  - **Example**: How is the adoption of 3D printing revolutionizing the manufacturing industry and supply chains?
- **التأثير التكنولوجي على الصناعات**: تتناول أسئلة/تعليمات التأثير التكنولوجي على الصناعات كيفية تحويل التكنولوجيا لمختلف القطاعات، مثل الرعاية الصحية والتمويل والنقل والتصنيع والترفيه.
  - **مثال**: كيف يؤدي اعتماد الطباعة ثلاثية الأبعاد إلى إحداث ثورة في الصناعة التحويلية وسلاسل التوريد؟
- **Technological Skills and Workforce**: Technological skills and workforce questions/instructions examine the skills and competencies needed in the digital age, workforce implications, and the future of work in the context of automation and artificial intelligence.
  - **Example**: What are the essential skills and training programs required to prepare the workforce for jobs in the field of data analytics?
- **المهارات التكنولوجية والقوى العاملة**: تدرس أسئلة/تعليمات المهارات التكنولوجية والقوى العاملة المهارات والكفاءات اللازمة في العصر الرقمي، وتأثيرات القوى العاملة، ومستقبل العمل في سياق الأتمتة والذكاء الاصطناعي.
  - **مثال**: ما هي المهارات الأساسية وبرامج التدريب اللازمة لإعداد القوى العاملة للوظائف في مجال تحليل البيانات؟

#### Instruction could be, but not limited to

- **What can** Sophia Robot do?
- **ما هي** امكانيات الروبوت صوفيا ؟
- **Yes no question/ Is the following statement correct:**
  - Are Tesla Cars safe:
  - هل سيارات تسلا آمنة؟
- **What are** the new capabilities of iPhone 15 pro?
- **ما هي** الإمكانيات لهاتف iPhone 15 pro؟
- **Create a tutorial on** ……….
- **قم بإنشاء** برنامج تعليمي حول كيفية تثبيت وتكوين نظام تشغيل جديد على جهاز الكمبيوتر.
- **قم بإنشاء** برنامج تعليمي حول استخدام أدوات الإنتاجية مثل Microsoft Excel أو Google Sheets لتحليل البيانات.
- **Write a step-by-step guide on** ………….
- **اكتب دليلاً خطوة بخطوة** حول إعداد شبكة Wi-Fi منزلية.
- **Write a guide on** ……………
  - Write a guide on setting up new PlayStation
  - اكتب دليلاً حول إعداد جهاز بلاي ستيشن جديد
- **Compare between** ……… and …………
  - Pros and cons between Android mobile phones and iPhones
  - إيجابيات وسلبيات بين الهواتف المحمولة التي تعمل بنظام Android وأجهزة iPhone
- **List** …………
  - List for me current humanoid robots
  - أعطني قائمة بالروبوتات البشرية الحالية
- **Suggest** ………….
  - Recommend a gaming PC given that current budget is ……….
  - اقترح جهاز كمبيوتر مخصص للألعاب نظرًا لأن الميزانية الحالية هي ……….
- **Summarize** …………
- How to configure ………….
- How does ……….. works
  - How does the computer work?
  - كيف يعمل الكمبيوتر؟
- **What is** ………..
  - What is the difference between Ubuntu OS and Windows OS
  - ما هو الفرق بين نظام التشغيل Ubuntu ونظام التشغيل Windows
- **Define** ………..
  - Define: Mechanics
  - **ما هو تعريف** الميكانيكا

#### Examples

Example 1

| Instruction | أعط نصائح حول كيفية تأمين حسابك الشخصي على وسائل التواصل الاجتماعي |
| --- | --- |
| Input |     |
| Output | وسائل التواصل الاجتماعي: كيفية تأمين حساباتك<br><br>تعد حسابات وسائل التواصل الاجتماعي أدوات قوية وطريقة رائعة للبقاء على اتصال مع العائلة والأصدقاء ومواكبة آخر الأخبار. ومع ذلك، من المهم معرفة كيفية إدارة إعدادات الأمان والخصوصية في حساباتك، بحيث تظل معلوماتك الشخصية غير قابلة للوصول لأي شخص غيرك، ولا تقع حساباتك في الأيدي الخطأ.<br><br>مستخدمي وسائل التواصل الاجتماعي<br><br>كيفية تأمين حساباتك<br><br>نوصي بشدة باستخدام النصائح أدناه للمساعدة في تأمين حساباتك جنبًا إلى جنب مع الإرشادات الخاصة بالنظام الأساسي.<br><br>1\. اختر كلمة مرور قوية باستخدام ثلاث كلمات عشوائية.<br><br>2\. استخدم كلمات مرور فريدة لكل شبكة اجتماعية.<br><br>3\. تمكين المصادقة الثنائية.<br><br>4\. قم بتعيين حساباتك إلى خاصة ومراجعة إعدادات الخصوصية الافتراضية حتى تتمكن من التحكم في من يرى ماذا في حساباتك.<br><br>5\. قم دائمًا بقفل جهازك أو تسجيل الخروج لمنع الوصول غير المصرح به إلى حسابات الوسائط الاجتماعية الخاصة بك.<br><br>6\. كن حذرًا بشأن المعلومات الشخصية التي تكشفها عن نفسك عبر الإنترنت. يمكن لمجرمي الإنترنت استخدام هذا في الهندسة الاجتماعية.<br><br>7\. استخدم وظيفة الحظر لحماية نفسك من حسابات البريد العشوائي والمتابعين/التفاعلات غير المرغوب فيها.<br><br>8\. لا تنقر على الروابط الموجودة في المنشورات أو التغريدات أو الرسائل المباشرة إلا إذا كنت متأكدًا بنسبة 100% من أنها حقيقية وحسنة النية - فقد تكون محاولات تصيد احتيالي! |
| Source | <https://www.nicybersecuritycentre.gov.uk/social-media-how-secure-your-accounts> |

Example 2

| Instruction | ما هي الشركة التي طورت أول هاتف محمول متاح تجاريا؟ |
| --- | --- |
| Input | أ) سامسونج<br><br>ب) التفاح<br><br>ج) موتورولا<br><br>د) نوكيا |
| Output | ج) موتورولا |
| Source | <https://en.wikipedia.org/wiki/Mobile_phone#:~:text=The%20Motorola%20DynaTAC%208000X.,2%20kilograms%20(4.4%20lb)>. |

Example 3

| Instruction | ما هي الإمكانيات الجديدة لهاتف iPhone 15 pro؟ |
| --- | --- |
| Input |     |
| Output | طرحت شركة Apple في سبتمبر 2023 هاتفي iPhone 15 Pro وiPhone 15 Pro Max، وهما هواتفها الذكية الرائدة الجديدة والمتطورة التي يتم بيعها جنبًا إلى جنب مع iPhone 15 وiPhone 15 Plus. تتميز طرازات iPhone 15 Pro بمجموعة ميزات موسعة غير متوفرة في أجهزة iPhone 15 القياسية، بما في ذلك تقنية الكاميرا الأكثر تقدمًا، وشاشة أفضل، وشريحة A17 أسرع، والمزيد.<br><br>متوفر بنفس الأحجام 6.1 و 6.7 بوصة مثل طرازات iPhone 14 Pro، وتتميز طرازات iPhone 15 Pro بتصميم مماثل، ولكن هناك بعض التغييرات الملحوظة. بدلاً من الفولاذ المقاوم للصدأ، تستخدم شركة Apple إطارًا مصنوعًا من سبيكة تيتانيوم جديدة تُستخدم أيضًا في المركبات الفضائية، وهناك ألوان جديدة من التيتانيوم بما في ذلك الأبيض والأسود والطبيعي والأزرق. التيتانيوم أخف من الفولاذ المقاوم للصدأ، لذا فإن موديلات iPhone 15 Pro تزن أقل من موديلات iPhone 14 Pro.<br><br>يتمتع التيتانيوم بملمس فرشاة جديد غير لامع ويرافقه إطار داخلي من الألومنيوم يعمل على تحسين التبديد الحراري وقابلية إصلاح الزجاج الخلفي. قامت Apple أيضًا بتعديل التصميم، بحيث يحتوي الإطار على حواف أكثر تحديدًا وإطارات الشاشة أرق بكثير. وتستمر حماية الجزء الأمامي من جهاز iPhone باستخدام مادة Ceramic Shield التي تنتجها شركة Apple، والتي تقول إنها أقوى زجاج يستخدم في الهاتف الذكي.<br><br>تستخدم Apple نفس شاشة Super Retina XDR من العام الماضي مع تقنية العرض Always-On ومعدل تحديث ProMotion يبلغ 120 هرتز. يتميز iPhone 15 Pro Max بدقة تبلغ 2796×1290، بينما تبلغ دقة iPhone 15 Pro 2556×1179. وبصرف النظر عن الحواف النحيفة، لا توجد تغييرات في الشاشة، كما أنها تتميز بنفس الجزيرة الديناميكية في الأعلى.<br><br>بدلاً من منفذ Lightning، تحتوي طرازات iPhone 15 Pro على منفذ USB-C الذي يوفر سرعات نقل USB 3 تصل إلى 10 جيجابت / ثانية. يتم الآن الشحن باستخدام كابل USB-C، بحيث يمكنك استخدام نفس السلك لشحن أجهزة iPhone وiPad وMac. باستخدام منفذ USB-C، يمكن استخدام iPhone لشحن AirPods أو Apple Watch مباشرة. لا يزال شحن MagSafe بقدرة 15 واط متاحًا، وأضافت Apple دعمًا للشحن اللاسلكي Qi2.<br><br>يوجد زر إجراء قابل للتخصيص تم تصميمه على غرار زر الإجراء الموجود في Apple Watch Ultra، وهو يحل محل مفتاح كتم الصوت. يمكن ضبطه على إحدى الوظائف المتعددة، مثل تشغيل الكاميرا أو تشغيل المصباح أو تسجيل مذكرة صوتية أو تنشيط اختصار. يرتبط زر الإجراء بالجزيرة الديناميكية للحصول على تعليقات مرئية مصاحبة للتعليقات اللمسية.<br><br>توفر الكاميرا الرئيسية التي تمت ترقيتها بدقة 48 ميجابكسل أداءً محسنًا في الإضاءة المنخفضة ودقة صورة افتراضية جديدة تبلغ 24 ميجابكسل توفر صورًا عالية الجودة بحجم ملف عملي، وهو تحسن مقارنة بالكاميرا الافتراضية السابقة البالغة 12 ميجابكسل. يمكن تعديل الكاميرا الرئيسية لأطوال بؤرية مختلفة، بما في ذلك 24 مم و28 مم و35 مم، وهناك خيار لالتقاط صور HEIF بدقة 48 ميجابكسل والتي تشغل مساحة أقل من صور RAW.<br><br>يتم الآن التقاط الصور الشخصية تلقائيًا عندما يكون هناك شخص أو حيوان أليف في الإطار أو عندما تنقر للتركيز، حتى تتمكن من ضبط العمق ونقطة التركيز بعد التقاط الصورة حتى لو لم تحدد الوضع الرأسي. تتضمن الصور تفاصيل أكثر وضوحًا وألوانًا أكثر حيوية وأداء أفضل في الإضاءة المنخفضة. أصبح الوضع الليلي أكثر وضوحًا من ذي قبل، ويلتقط Smart HDR 5 الأهداف والخلفيات بألوان بشرة أكثر واقعية وإبرازات أكثر سطوعًا وألوان متوسطة أكثر ثراءً وظلال أعمق عند عرضها في تطبيق الصور.<br><br>هناك كاميرا جديدة فائقة الاتساع تسمح بدخول المزيد من الضوء. يحتوي iPhone 15 Pro على عدسة Telephoto قياسية 3x، لكن iPhone 15 Pro Max مزود بعدسة Telephoto 5x مطورة تستخدم تصميمًا رباعيًا جديدًا. قدمت شركة Apple نظامًا جديدًا لتثبيت الصورة البصرية يتضمن وحدة تحويل مستشعر التركيز التلقائي ثلاثي الأبعاد للحصول على صور أكثر وضوحًا.<br><br>شريحة A17 Pro هي أول شريحة من Apple بتقنية 3 نانومتر، مبنية على عقدة محدثة. تقول Apple إنها تتضمن أكبر إعادة تصميم لوحدة معالجة الرسومات في تاريخ Apple، وأن أداء وحدة معالجة الرسومات أسرع بنسبة تصل إلى 20% من شريحة A16. أداء وحدة المعالجة المركزية أسرع بما يصل إلى 10%. المحرك العصبي الجديد أسرع بما يصل إلى 2x.<br><br>بفضل وحدة معالجة الرسومات سداسية النواة، تمكنت Apple من إضافة تتبع الأشعة المسرع للأجهزة والذي يسمح لجهاز iPhone بتشغيل ألعاب وحدة التحكم مثل Assassin's Creed Mirage و Resident Evil 4 لأول مرة، بالإضافة إلى أنه يعزز تطبيقات الواقع المعزز. يوجد وحدة فك ترميز AV1 مخصصة لدفق الفيديو بشكل أكثر كفاءة. يعمل A17 Pro على تشغيل ميزة تسمح لجهاز iPhone بالاتصال بوحدة تخزين خارجية لتسجيل فيديو ProRes بدقة 4K بمعدل 60 إطارًا في الثانية مباشرة على جهاز التخزين. ولمرافقة هذه الميزة، أضافت Apple خيارًا لتشفير السجل، مما يجعل طرازات iPhone 15 Pro أول الهواتف الذكية التي تدعم نظام تشفير الألوان Academy الذي يستخدمه صانعو الأفلام.<br><br>وفي وقت لاحق من العام، ستتمكن طرازات iPhone 15 Pro من تسجيل فيديو مكاني ثلاثي الأبعاد يمكن مشاهدته على Apple Vision Pro عند إطلاقه العام المقبل.<br><br>ايفون 15 برو رمادي<br><br>أضافت Apple شريحة Ultra Wideband من الجيل الثاني التي تسمح لجهازي iPhone المزودين بالشريحة بالاتصال على نطاق أطول بمقدار 3x. يعمل الاتصال المحسن على تشغيل جهاز Precision Findi الجديد |
| Source | <https://www.macrumors.com/roundup/iphone-15-pro/> |
