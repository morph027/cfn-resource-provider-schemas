SCHEMA = {
  "typeName" : "AWS::CustomerProfiles::Domain",
  "description" : "A domain defined for 3rd party data source in Profile Service",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-customer-profiles.git",
  "definitions" : {
    "Tag" : {
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "pattern" : "^(?!aws:)[a-zA-Z+-=._:/]+$",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "additionalProperties" : False,
      "required" : [ "Key", "Value" ]
    },
    "DomainStats" : {
      "type" : "object",
      "description" : "Usage-specific statistics about the domain.",
      "properties" : {
        "MeteringProfileCount" : {
          "description" : "The number of profiles that you are currently paying for in the domain. If you have more than 100 objects associated with a single profile, that profile counts as two profiles. If you have more than 200 objects, that profile counts as three, and so on.",
          "type" : "number"
        },
        "ObjectCount" : {
          "description" : "The total number of objects in domain.",
          "type" : "number"
        },
        "ProfileCount" : {
          "description" : "The total number of profiles currently in the domain.",
          "type" : "number"
        },
        "TotalSize" : {
          "description" : "The total size, in bytes, of all objects in the domain.",
          "type" : "number"
        }
      },
      "additionalProperties" : False
    },
    "S3ExportingConfig" : {
      "type" : "object",
      "description" : "The S3 location where Identity Resolution Jobs write result files.",
      "properties" : {
        "S3BucketName" : {
          "description" : "The name of the S3 bucket where Identity Resolution Jobs write result files.",
          "type" : "string",
          "minLength" : 3,
          "maxLength" : 63,
          "pattern" : "^[a-z0-9.-]+$"
        },
        "S3KeyName" : {
          "description" : "The S3 key name of the location where Identity Resolution Jobs write result files.",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 800,
          "pattern" : ".*"
        }
      },
      "required" : [ "S3BucketName" ],
      "additionalProperties" : False
    },
    "ExportingConfig" : {
      "type" : "object",
      "description" : "Configuration information for exporting Identity Resolution results, for example, to an S3 bucket.",
      "properties" : {
        "S3Exporting" : {
          "$ref" : "#/definitions/S3ExportingConfig"
        }
      },
      "additionalProperties" : False
    },
    "JobSchedule" : {
      "type" : "object",
      "description" : "The day and time when do you want to start the Identity Resolution Job every week.",
      "properties" : {
        "DayOfTheWeek" : {
          "description" : "The day when the Identity Resolution Job should run every week.",
          "type" : "string",
          "enum" : [ "SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY" ]
        },
        "Time" : {
          "description" : "The time when the Identity Resolution Job should run every week.",
          "type" : "string",
          "minLength" : 3,
          "maxLength" : 5,
          "pattern" : "^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$"
        }
      },
      "required" : [ "DayOfTheWeek", "Time" ],
      "additionalProperties" : False
    },
    "ConflictResolution" : {
      "type" : "object",
      "description" : "How the auto-merging process should resolve conflicts between different profiles. For example, if Profile A and Profile B have the same FirstName and LastName (and that is the matching criteria), which EmailAddress should be used? ",
      "properties" : {
        "ConflictResolvingModel" : {
          "description" : "How the auto-merging process should resolve conflicts between different profiles.",
          "type" : "string",
          "enum" : [ "RECENCY", "SOURCE" ]
        },
        "SourceName" : {
          "description" : "The ObjectType name that is used to resolve profile merging conflicts when choosing SOURCE as the ConflictResolvingModel.",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 255
        }
      },
      "required" : [ "ConflictResolvingModel" ],
      "additionalProperties" : False
    },
    "MatchingAttributes" : {
      "type" : "array",
      "minItems" : 1,
      "maxItems" : 20,
      "items" : {
        "type" : "string",
        "minLength" : 1,
        "maxLength" : 255
      }
    },
    "Consolidation" : {
      "description" : "A list of matching attributes that represent matching criteria. If two profiles meet at least one of the requirements in the matching attributes list, they will be merged.",
      "type" : "object",
      "properties" : {
        "MatchingAttributesList" : {
          "description" : "A list of matching criteria.",
          "type" : "array",
          "minItems" : 1,
          "maxItems" : 10,
          "items" : {
            "$ref" : "#/definitions/MatchingAttributes"
          }
        }
      },
      "required" : [ "MatchingAttributesList" ],
      "additionalProperties" : False
    },
    "AutoMerging" : {
      "type" : "object",
      "description" : "Configuration information about the auto-merging process.",
      "properties" : {
        "Enabled" : {
          "description" : "The flag that enables the auto-merging of duplicate profiles.",
          "type" : "boolean"
        },
        "ConflictResolution" : {
          "$ref" : "#/definitions/ConflictResolution"
        },
        "Consolidation" : {
          "$ref" : "#/definitions/Consolidation"
        },
        "MinAllowedConfidenceScoreForMerging" : {
          "description" : "A number between 0 and 1 that represents the minimum confidence score required for profiles within a matching group to be merged during the auto-merge process. A higher score means higher similarity required to merge profiles.",
          "type" : "number",
          "minimum" : 0.0,
          "maximum" : 1.0
        }
      },
      "required" : [ "Enabled" ],
      "additionalProperties" : False
    },
    "MatchingRuleAttributeList" : {
      "description" : "A single rule level of the MatchRules. Configures how the rule-based matching process should match profiles.",
      "type" : "array",
      "minItems" : 1,
      "maxItems" : 15,
      "items" : {
        "type" : "string",
        "minLength" : 1,
        "maxLength" : 255
      }
    },
    "MatchingRule" : {
      "description" : "Specifies how does the rule-based matching process should match profiles.",
      "type" : "object",
      "properties" : {
        "Rule" : {
          "$ref" : "#/definitions/MatchingRuleAttributeList"
        }
      },
      "required" : [ "Rule" ],
      "additionalProperties" : False
    },
    "AttributeTypesSelector" : {
      "description" : "Configures information about the AttributeTypesSelector where the rule-based identity resolution uses to match profiles.",
      "type" : "object",
      "properties" : {
        "AttributeMatchingModel" : {
          "description" : "Configures the AttributeMatchingModel, you can either choose ONE_TO_ONE or MANY_TO_MANY.",
          "type" : "string",
          "enum" : [ "ONE_TO_ONE", "MANY_TO_MANY" ]
        },
        "Address" : {
          "description" : "The Address type. You can choose from Address, BusinessAddress, MaillingAddress, and ShippingAddress. You only can use the Address type in the MatchingRule. For example, if you want to match profile based on BusinessAddress.City or MaillingAddress.City, you need to choose the BusinessAddress and the MaillingAddress to represent the Address type and specify the Address.City on the matching rule.",
          "type" : "array",
          "minItems" : 1,
          "maxItems" : 4,
          "items" : {
            "type" : "string",
            "minLength" : 1,
            "maxLength" : 255
          }
        },
        "EmailAddress" : {
          "description" : "The Email type. You can choose from EmailAddress, BusinessEmailAddress and PersonalEmailAddress. You only can use the EmailAddress type in the MatchingRule. For example, if you want to match profile based on PersonalEmailAddress or BusinessEmailAddress, you need to choose the PersonalEmailAddress and the BusinessEmailAddress to represent the EmailAddress type and only specify the EmailAddress on the matching rule.",
          "type" : "array",
          "minItems" : 1,
          "maxItems" : 3,
          "items" : {
            "type" : "string",
            "minLength" : 1,
            "maxLength" : 255
          }
        },
        "PhoneNumber" : {
          "description" : "The PhoneNumber type. You can choose from PhoneNumber, HomePhoneNumber, and MobilePhoneNumber. You only can use the PhoneNumber type in the MatchingRule. For example, if you want to match a profile based on Phone or HomePhone, you need to choose the Phone and the HomePhone to represent the PhoneNumber type and only specify the PhoneNumber on the matching rule.",
          "type" : "array",
          "minItems" : 1,
          "maxItems" : 4,
          "items" : {
            "type" : "string",
            "minLength" : 1,
            "maxLength" : 255
          }
        }
      },
      "required" : [ "AttributeMatchingModel" ],
      "additionalProperties" : False
    },
    "Matching" : {
      "description" : "The process of matching duplicate profiles. If Matching = True, Amazon Connect Customer Profiles starts a weekly batch process called Identity Resolution Job. If you do not specify a date and time for Identity Resolution Job to run, by default it runs every Saturday at 12AM UTC to detect duplicate profiles in your domains. After the Identity Resolution Job completes, use the GetMatches API to return and review the results. Or, if you have configured ExportingConfig in the MatchingRequest, you can download the results from S3.",
      "type" : "object",
      "properties" : {
        "Enabled" : {
          "description" : "The flag that enables the matching process of duplicate profiles.",
          "type" : "boolean"
        },
        "AutoMerging" : {
          "$ref" : "#/definitions/AutoMerging"
        },
        "ExportingConfig" : {
          "$ref" : "#/definitions/ExportingConfig"
        },
        "JobSchedule" : {
          "$ref" : "#/definitions/JobSchedule"
        }
      },
      "required" : [ "Enabled" ],
      "additionalProperties" : False
    },
    "RuleBasedMatching" : {
      "description" : "The process of matching duplicate profiles using the Rule-Based matching. If RuleBasedMatching = True, Amazon Connect Customer Profiles will start to match and merge your profiles according to your configuration in the RuleBasedMatchingRequest. You can use the ListRuleBasedMatches and GetSimilarProfiles API to return and review the results. Also, if you have configured ExportingConfig in the RuleBasedMatchingRequest, you can download the results from S3.",
      "type" : "object",
      "properties" : {
        "Enabled" : {
          "description" : "The flag that enables the rule-based matching process of duplicate profiles.",
          "type" : "boolean"
        },
        "AttributeTypesSelector" : {
          "$ref" : "#/definitions/AttributeTypesSelector"
        },
        "ConflictResolution" : {
          "$ref" : "#/definitions/ConflictResolution"
        },
        "ExportingConfig" : {
          "$ref" : "#/definitions/ExportingConfig"
        },
        "MatchingRules" : {
          "description" : "Configures how the rule-based matching process should match profiles. You can have up to 15 MatchingRule in the MatchingRules.",
          "type" : "array",
          "minItems" : 1,
          "maxItems" : 15,
          "items" : {
            "$ref" : "#/definitions/MatchingRule"
          }
        },
        "MaxAllowedRuleLevelForMatching" : {
          "description" : "Indicates the maximum allowed rule level for matching.",
          "type" : "integer",
          "minimum" : 1,
          "maximum" : 15
        },
        "MaxAllowedRuleLevelForMerging" : {
          "description" : "Indicates the maximum allowed rule level for merging.",
          "type" : "integer",
          "minimum" : 1,
          "maximum" : 15
        },
        "Status" : {
          "type" : "string",
          "enum" : [ "PENDING", "IN_PROGRESS", "ACTIVE" ]
        }
      },
      "required" : [ "Enabled" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "DomainName" : {
      "description" : "The unique name of the domain.",
      "type" : "string",
      "pattern" : "^[a-zA-Z0-9_-]+$",
      "minLength" : 1,
      "maxLength" : 64
    },
    "DeadLetterQueueUrl" : {
      "description" : "The URL of the SQS dead letter queue",
      "type" : "string",
      "minLength" : 0,
      "maxLength" : 255
    },
    "DefaultEncryptionKey" : {
      "description" : "The default encryption key",
      "type" : "string",
      "minLength" : 0,
      "maxLength" : 255
    },
    "DefaultExpirationDays" : {
      "description" : "The default number of days until the data within the domain expires.",
      "type" : "integer",
      "minimum" : 1,
      "maximum" : 1098
    },
    "Matching" : {
      "$ref" : "#/definitions/Matching"
    },
    "RuleBasedMatching" : {
      "$ref" : "#/definitions/RuleBasedMatching"
    },
    "Stats" : {
      "$ref" : "#/definitions/DomainStats"
    },
    "Tags" : {
      "description" : "The tags (keys and values) associated with the domain",
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Tag"
      },
      "minItems" : 0,
      "maxItems" : 50
    },
    "CreatedAt" : {
      "description" : "The time of this integration got created",
      "type" : "string"
    },
    "LastUpdatedAt" : {
      "description" : "The time of this integration got last updated at",
      "type" : "string"
    }
  },
  "additionalProperties" : False,
  "required" : [ "DomainName", "DefaultExpirationDays" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "profile:TagResource", "profile:UntagResource", "profile:ListTagsForResource" ]
  },
  "readOnlyProperties" : [ "/properties/LastUpdatedAt", "/properties/CreatedAt", "/properties/RuleBasedMatching/Status", "/properties/Stats" ],
  "createOnlyProperties" : [ "/properties/DomainName" ],
  "primaryIdentifier" : [ "/properties/DomainName" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "profile:CreateDomain", "profile:TagResource" ]
    },
    "read" : {
      "permissions" : [ "profile:GetDomain" ]
    },
    "update" : {
      "permissions" : [ "profile:GetDomain", "profile:UpdateDomain", "profile:UntagResource", "profile:TagResource" ]
    },
    "delete" : {
      "permissions" : [ "profile:DeleteDomain" ]
    },
    "list" : {
      "permissions" : [ "profile:ListDomains" ]
    }
  }
}