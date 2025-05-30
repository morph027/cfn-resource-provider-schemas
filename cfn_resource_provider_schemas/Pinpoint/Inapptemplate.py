SCHEMA = {
  "additionalProperties" : False,
  "createOnlyProperties" : [ "/properties/TemplateName" ],
  "definitions" : {
    "Alignment" : {
      "enum" : [ "LEFT", "CENTER", "RIGHT" ],
      "type" : "string"
    },
    "BodyConfig" : {
      "additionalProperties" : False,
      "properties" : {
        "Alignment" : {
          "$ref" : "#/definitions/Alignment"
        },
        "Body" : {
          "type" : "string"
        },
        "TextColor" : {
          "type" : "string"
        }
      },
      "type" : "object"
    },
    "ButtonAction" : {
      "enum" : [ "LINK", "DEEP_LINK", "CLOSE" ],
      "type" : "string"
    },
    "ButtonConfig" : {
      "additionalProperties" : False,
      "properties" : {
        "Android" : {
          "$ref" : "#/definitions/OverrideButtonConfiguration"
        },
        "DefaultConfig" : {
          "$ref" : "#/definitions/DefaultButtonConfiguration"
        },
        "IOS" : {
          "$ref" : "#/definitions/OverrideButtonConfiguration"
        },
        "Web" : {
          "$ref" : "#/definitions/OverrideButtonConfiguration"
        }
      },
      "type" : "object"
    },
    "DefaultButtonConfiguration" : {
      "additionalProperties" : False,
      "properties" : {
        "BackgroundColor" : {
          "type" : "string"
        },
        "BorderRadius" : {
          "type" : "integer"
        },
        "ButtonAction" : {
          "$ref" : "#/definitions/ButtonAction"
        },
        "Link" : {
          "type" : "string"
        },
        "Text" : {
          "type" : "string"
        },
        "TextColor" : {
          "type" : "string"
        }
      },
      "type" : "object"
    },
    "HeaderConfig" : {
      "additionalProperties" : False,
      "properties" : {
        "Alignment" : {
          "$ref" : "#/definitions/Alignment"
        },
        "Header" : {
          "type" : "string"
        },
        "TextColor" : {
          "type" : "string"
        }
      },
      "type" : "object"
    },
    "InAppMessageContent" : {
      "additionalProperties" : False,
      "properties" : {
        "BackgroundColor" : {
          "type" : "string"
        },
        "BodyConfig" : {
          "$ref" : "#/definitions/BodyConfig"
        },
        "HeaderConfig" : {
          "$ref" : "#/definitions/HeaderConfig"
        },
        "ImageUrl" : {
          "type" : "string"
        },
        "PrimaryBtn" : {
          "$ref" : "#/definitions/ButtonConfig"
        },
        "SecondaryBtn" : {
          "$ref" : "#/definitions/ButtonConfig"
        }
      },
      "type" : "object"
    },
    "OverrideButtonConfiguration" : {
      "additionalProperties" : False,
      "properties" : {
        "ButtonAction" : {
          "$ref" : "#/definitions/ButtonAction"
        },
        "Link" : {
          "type" : "string"
        }
      },
      "type" : "object"
    }
  },
  "description" : "Resource Type definition for AWS::Pinpoint::InAppTemplate",
  "handlers" : {
    "create" : {
      "permissions" : [ "mobiletargeting:CreateInAppTemplate", "mobiletargeting:GetInAppTemplate", "mobiletargeting:TagResource" ]
    },
    "delete" : {
      "permissions" : [ "mobiletargeting:DeleteInAppTemplate", "mobiletargeting:GetInAppTemplate" ]
    },
    "list" : {
      "permissions" : [ "mobiletargeting:GetInAppTemplate", "mobiletargeting:ListTemplates" ]
    },
    "read" : {
      "permissions" : [ "mobiletargeting:GetInAppTemplate", "mobiletargeting:ListTemplates" ]
    },
    "update" : {
      "permissions" : [ "mobiletargeting:UpdateInAppTemplate", "mobiletargeting:GetInAppTemplate", "mobiletargeting:TagResource", "mobiletargeting:UntagResource" ]
    }
  },
  "primaryIdentifier" : [ "/properties/TemplateName" ],
  "properties" : {
    "Arn" : {
      "type" : "string"
    },
    "Content" : {
      "insertionOrder" : True,
      "items" : {
        "$ref" : "#/definitions/InAppMessageContent"
      },
      "type" : "array"
    },
    "CustomConfig" : {
      "type" : "object"
    },
    "Layout" : {
      "enum" : [ "BOTTOM_BANNER", "TOP_BANNER", "OVERLAYS", "MOBILE_FEED", "MIDDLE_BANNER", "CAROUSEL" ],
      "type" : "string"
    },
    "Tags" : {
      "type" : "object"
    },
    "TemplateDescription" : {
      "type" : "string"
    },
    "TemplateName" : {
      "type" : "string"
    }
  },
  "readOnlyProperties" : [ "/properties/Arn" ],
  "required" : [ "TemplateName" ],
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "mobiletargeting:TagResource", "mobiletargeting:UntagResource" ]
  },
  "typeName" : "AWS::Pinpoint::InAppTemplate"
}