SCHEMA = {
  "typeName" : "AWS::Lex::BotVersion",
  "description" : "A version is a numbered snapshot of your work that you can publish for use in different parts of your workflow, such as development, beta deployment, and production.",
  "sourceUrl" : "https://docs.aws.amazon.com/lexv2/latest/dg/API_CreateBotVersion.html",
  "definitions" : {
    "Id" : {
      "description" : "Unique ID of resource",
      "type" : "string",
      "minLength" : 10,
      "maxLength" : 10,
      "pattern" : "^[0-9a-zA-Z]+$"
    },
    "Description" : {
      "description" : "A description of the version. Use the description to help identify the version in lists.",
      "type" : "string",
      "maxLength" : 200
    },
    "LocaleId" : {
      "description" : "The identifier of the language and locale that the bot will be used in.",
      "type" : "string"
    },
    "BotVersion" : {
      "description" : "The version of a bot.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 5,
      "pattern" : "^(DRAFT|[0-9]+)$"
    },
    "BotVersionLocaleDetails" : {
      "description" : "The version of a bot used for a bot locale.",
      "type" : "object",
      "properties" : {
        "SourceBotVersion" : {
          "$ref" : "#/definitions/BotVersion"
        }
      },
      "required" : [ "SourceBotVersion" ],
      "additionalProperties" : False
    },
    "BotVersionLocaleSpecification" : {
      "type" : "object",
      "properties" : {
        "LocaleId" : {
          "$ref" : "#/definitions/LocaleId"
        },
        "BotVersionLocaleDetails" : {
          "$ref" : "#/definitions/BotVersionLocaleDetails"
        }
      },
      "required" : [ "LocaleId", "BotVersionLocaleDetails" ],
      "additionalProperties" : False
    },
    "BotVersionLocaleSpecificationList" : {
      "description" : "Specifies the locales that Amazon Lex adds to this version. You can choose the Draft version or any other previously published version for each locale.",
      "type" : "array",
      "insertionOrder" : False,
      "minItems" : 1,
      "items" : {
        "$ref" : "#/definitions/BotVersionLocaleSpecification"
      }
    }
  },
  "properties" : {
    "BotId" : {
      "$ref" : "#/definitions/Id"
    },
    "BotVersion" : {
      "$ref" : "#/definitions/BotVersion"
    },
    "Description" : {
      "$ref" : "#/definitions/Description"
    },
    "BotVersionLocaleSpecification" : {
      "$ref" : "#/definitions/BotVersionLocaleSpecificationList"
    }
  },
  "taggable" : False,
  "additionalProperties" : False,
  "required" : [ "BotId", "BotVersionLocaleSpecification" ],
  "readOnlyProperties" : [ "/properties/BotVersion" ],
  "createOnlyProperties" : [ "/properties/BotId" ],
  "writeOnlyProperties" : [ "/properties/BotVersionLocaleSpecification" ],
  "primaryIdentifier" : [ "/properties/BotId", "/properties/BotVersion" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "lex:CreateBotVersion", "lex:DescribeBotVersion", "lex:DescribeBot", "lex:DescribeBotLocale", "lex:BuildBotLocale" ]
    },
    "read" : {
      "permissions" : [ "lex:DescribeBotVersion" ]
    },
    "delete" : {
      "permissions" : [ "lex:DeleteBotVersion", "lex:DescribeBotVersion" ]
    },
    "list" : {
      "permissions" : [ "lex:ListBotVersions" ]
    }
  }
}