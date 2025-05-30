SCHEMA = {
  "typeName" : "AWS::Pinpoint::PushTemplate",
  "description" : "Resource Type definition for AWS::Pinpoint::PushTemplate",
  "additionalProperties" : False,
  "properties" : {
    "GCM" : {
      "$ref" : "#/definitions/AndroidPushNotificationTemplate"
    },
    "Baidu" : {
      "$ref" : "#/definitions/AndroidPushNotificationTemplate"
    },
    "TemplateName" : {
      "type" : "string"
    },
    "ADM" : {
      "$ref" : "#/definitions/AndroidPushNotificationTemplate"
    },
    "APNS" : {
      "$ref" : "#/definitions/APNSPushNotificationTemplate"
    },
    "TemplateDescription" : {
      "type" : "string"
    },
    "DefaultSubstitutions" : {
      "type" : "string"
    },
    "Id" : {
      "type" : "string"
    },
    "Arn" : {
      "type" : "string"
    },
    "Default" : {
      "$ref" : "#/definitions/DefaultPushNotificationTemplate"
    },
    "Tags" : {
      "type" : "object"
    }
  },
  "definitions" : {
    "AndroidPushNotificationTemplate" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Action" : {
          "type" : "string"
        },
        "ImageUrl" : {
          "type" : "string"
        },
        "SmallImageIconUrl" : {
          "type" : "string"
        },
        "Title" : {
          "type" : "string"
        },
        "ImageIconUrl" : {
          "type" : "string"
        },
        "Sound" : {
          "type" : "string"
        },
        "Body" : {
          "type" : "string"
        },
        "Url" : {
          "type" : "string"
        }
      }
    },
    "APNSPushNotificationTemplate" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Action" : {
          "type" : "string"
        },
        "MediaUrl" : {
          "type" : "string"
        },
        "Title" : {
          "type" : "string"
        },
        "Sound" : {
          "type" : "string"
        },
        "Body" : {
          "type" : "string"
        },
        "Url" : {
          "type" : "string"
        }
      }
    },
    "DefaultPushNotificationTemplate" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Title" : {
          "type" : "string"
        },
        "Action" : {
          "type" : "string"
        },
        "Sound" : {
          "type" : "string"
        },
        "Body" : {
          "type" : "string"
        },
        "Url" : {
          "type" : "string"
        }
      }
    }
  },
  "required" : [ "TemplateName" ],
  "createOnlyProperties" : [ "/properties/TemplateName" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id", "/properties/Arn" ]
}