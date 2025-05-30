SCHEMA = {
  "typeName" : "AWS::Connect::PhoneNumber",
  "description" : "Resource Type definition for AWS::Connect::PhoneNumber",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-connect",
  "definitions" : {
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. ",
          "pattern" : "^(?!aws:)[a-zA-Z+-=._:/]+$",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for the tag. You can specify a value that is 1 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. ",
          "maxLength" : 256
        }
      },
      "required" : [ "Key", "Value" ]
    }
  },
  "properties" : {
    "TargetArn" : {
      "description" : "The ARN of the target the phone number is claimed to.",
      "type" : "string",
      "pattern" : "^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:(instance|traffic-distribution-group)/[-a-zA-Z0-9]*$"
    },
    "PhoneNumberArn" : {
      "description" : "The phone number ARN",
      "type" : "string",
      "pattern" : "^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:phone-number/[-a-zA-Z0-9]*$"
    },
    "Description" : {
      "description" : "The description of the phone number.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 500
    },
    "Type" : {
      "description" : "The phone number type",
      "type" : "string",
      "pattern" : "TOLL_FREE|DID|UIFN|SHARED|THIRD_PARTY_DID|THIRD_PARTY_TF|SHORT_CODE"
    },
    "CountryCode" : {
      "description" : "The phone number country code.",
      "type" : "string",
      "pattern" : "^[A-Z]{2}"
    },
    "Prefix" : {
      "description" : "The phone number prefix.",
      "type" : "string",
      "pattern" : "^\\+[0-9]{1,15}"
    },
    "Address" : {
      "description" : "The phone number e164 address.",
      "type" : "string",
      "pattern" : "^\\+[0-9]{2,15}"
    },
    "Tags" : {
      "type" : "array",
      "maxItems" : 50,
      "uniqueItems" : True,
      "insertionOrder" : False,
      "description" : "One or more tags.",
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "SourcePhoneNumberArn" : {
      "description" : "The source phone number arn.",
      "type" : "string"
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "connect:UntagResource", "connect:TagResource" ]
  },
  "required" : [ "TargetArn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "connect:ClaimPhoneNumber", "connect:SearchAvailablePhoneNumbers", "connect:DescribePhoneNumber", "connect:TagResource", "connect:ImportPhoneNumber", "sms-voice:DescribePhoneNumbers", "social-messaging:GetLinkedWhatsAppBusinessAccountPhoneNumber", "social-messaging:TagResource" ]
    },
    "read" : {
      "permissions" : [ "connect:DescribePhoneNumber" ]
    },
    "delete" : {
      "permissions" : [ "connect:ReleasePhoneNumber", "connect:UntagResource" ]
    },
    "update" : {
      "permissions" : [ "connect:UpdatePhoneNumber", "connect:UpdatePhoneNumberMetadata", "connect:DescribePhoneNumber", "connect:TagResource", "connect:UntagResource" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "TargetArn" : {
            "$ref" : "resource-schema.json#/properties/TargetArn"
          }
        },
        "required" : [ "TargetArn" ]
      },
      "permissions" : [ "connect:ListPhoneNumbersV2" ]
    }
  },
  "additionalProperties" : False,
  "primaryIdentifier" : [ "/properties/PhoneNumberArn" ],
  "readOnlyProperties" : [ "/properties/PhoneNumberArn", "/properties/Address" ],
  "writeOnlyProperties" : [ "/properties/Prefix" ],
  "createOnlyProperties" : [ "/properties/Type", "/properties/CountryCode", "/properties/Prefix", "/properties/SourcePhoneNumberArn" ]
}