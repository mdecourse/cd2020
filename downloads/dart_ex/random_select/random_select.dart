import 'dart:html';
import 'dart:convert';

SelectElement studListUrl = querySelector("#RstudListUrl");
String grpList;
InputElement numOfStud = querySelector("#RnumOfStud");
int num;
// 將 Label 改為 Textarea, 避免產生過程結果嵌入所在頁面
TextAreaElement output = querySelector("#Routput");

main() {
  querySelector("#Rsubmit").onClick.listen((e) => randomSelect());
}

randomSelect() {
  output.innerHtml = "";

  if (studListUrl.value != "") {
    grpList = studListUrl.value;
  } else {
    grpList = 'https://mde.tw/cd2020/downloads/2a_group_list.txt';
  }

  if (numOfStud.value != "") {
    num = int.parse(numOfStud.value);
  } else {
    num = 2;
  }

  HttpRequest.getString(grpList).then((String resp) {
    final replaced = resp.replaceAll("'", '');
    List studList = jsonDecode(replaced);
    for (int i = 0; i < studList.length; i++) {
      // shuffle studList element
      studList[i].shuffle();
      // draw num of member from each group
      output.text += "-" * 20 + "\n";
      for (int j = 0; j < num; j++) {
        output.text += "group ${i + 1}:" + studList[i][j].toString() + "\n";
      }
    }
  });
}
