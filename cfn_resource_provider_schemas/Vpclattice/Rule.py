SCHEMA = {
  "typeName" : "AWS::VpcLattice::Rule",
  "description" : "Creates a listener rule. Each listener has a default rule for checking connection requests, but you can define additional rules. Each rule consists of a priority, one or more actions, and one or more conditions.",
  "additionalProperties" : False,
  "definitions" : {
    "Forward" : {
      "type" : "object",
      "properties" : {
        "TargetGroups" : {
          "type" : "array",
          "items" : {
            "$ref" : "#/definitions/WeightedTargetGroup"
          },
          "maxItems" : 10,
          "minItems" : 1,
          "insertionOrder" : False
        }
      },
      "required" : [ "TargetGroups" ],
      "additionalProperties" : False
    },
    "FixedResponse" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "StatusCode" : {
          "type" : "integer",
          "maximum" : 599,
          "minimum" : 100
        }
      },
      "required" : [ "StatusCode" ]
    },
    "HeaderMatch" : {
      "type" : "object",
      "properties" : {
        "Name" : {
          "type" : "string",
          "maxLength" : 40,
          "minLength" : 1
        },
        "Match" : {
          "$ref" : "#/definitions/HeaderMatchType"
        },
        "CaseSensitive" : {
          "type" : "boolean",
          "default" : False
        }
      },
      "required" : [ "Match", "Name" ],
      "additionalProperties" : False
    },
    "HeaderMatchType" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Exact" : {
          "type" : "string",
          "maxLength" : 128,
          "minLength" : 1
        },
        "Prefix" : {
          "type" : "string",
          "maxLength" : 128,
          "minLength" : 1
        },
        "Contains" : {
          "type" : "string",
          "maxLength" : 128,
          "minLength" : 1
        }
      }
    },
    "HttpMatch" : {
      "type" : "object",
      "properties" : {
        "Method" : {
          "type" : "string",
          "enum" : [ "CONNECT", "DELETE", "GET", "HEAD", "OPTIONS", "POST", "PUT", "TRACE" ]
        },
        "PathMatch" : {
          "$ref" : "#/definitions/PathMatch"
        },
        "HeaderMatches" : {
          "type" : "array",
          "maxItems" : 5,
          "items" : {
            "$ref" : "#/definitions/HeaderMatch"
          },
          "insertionOrder" : False
        }
      },
      "additionalProperties" : False
    },
    "PathMatch" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Match" : {
          "$ref" : "#/definitions/PathMatchType"
        },
        "CaseSensitive" : {
          "type" : "boolean",
          "default" : False
        }
      },
      "required" : [ "Match" ]
    },
    "PathMatchType" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Exact" : {
          "type" : "string",
          "maxLength" : 128,
          "minLength" : 1,
          "pattern" : "^\\/[a-zA-Z0-9@:%_+.~#?&\\/=-]*$"
        },
        "Prefix" : {
          "type" : "string",
          "maxLength" : 128,
          "minLength" : 1,
          "pattern" : "^\\/[a-zA-Z0-9@:%_+.~#?&\\/=-]*$"
        }
      }
    },
    "Action" : {
      "type" : "object",
      "title" : "Forward",
      "properties" : {
        "Forward" : {
          "$ref" : "#/definitions/Forward"
        },
        "FixedResponse" : {
          "$ref" : "#/definitions/FixedResponse"
        }
      },
      "required" : [ ],
      "additionalProperties" : False
    },
    "Match" : {
      "type" : "object",
      "title" : "HttpMatch",
      "properties" : {
        "HttpMatch" : {
          "$ref" : "#/definitions/HttpMatch"
        }
      },
      "required" : [ "HttpMatch" ],
      "additionalProperties" : False
    },
    "WeightedTargetGroup" : {
      "type" : "object",
      "properties" : {
        "TargetGroupIdentifier" : {
          "type" : "string",
          "maxLength" : 2048,
          "minLength" : 20,
          "pattern" : "^((tg-[0-9a-z]{17})|(arn:[a-z0-9\\-]+:vpc-lattice:[a-zA-Z0-9\\-]+:\\d{12}:targetgroup/tg-[0-9a-z]{17}))$"
        },
        "Weight" : {
          "type" : "integer",
          "maximum" : 999,
          "minimum" : 1
        }
      },
      "required" : [ "TargetGroupIdentifier" ],
      "additionalProperties" : False
    },
    "Tag" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Key" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 256
        }
      },
      "required" : [ "Key", "Value" ]
    }
  },
  "properties" : {
    "Action" : {
      "$ref" : "#/definitions/Action"
    },
    "Arn" : {
      "type" : "string",
      "maxLength" : 2048,
      "minLength" : 20,
      "pattern" : "^arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:service/svc-[0-9a-z]{17}/listener/listener-[0-9a-z]{17}/rule/((rule-[0-9a-z]{17})|(default))$"
    },
    "Id" : {
      "type" : "string",
      "maxLength" : 22,
      "minLength" : 7,
      "pattern" : "^((rule-[0-9a-z]{17})|(default))$"
    },
    "ListenerIdentifier" : {
      "type" : "string",
      "maxLength" : 2048,
      "minLength" : 20,
      "pattern" : "^((listener-[0-9a-z]{17})|(arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:service/svc-[0-9a-z]{17}/listener/listener-[0-9a-z]{17}))$"
    },
    "Match" : {
      "$ref" : "#/definitions/Match"
    },
    "Name" : {
      "type" : "string",
      "maxLength" : 63,
      "minLength" : 3,
      "pattern" : "^(?!rule-)(?![-])(?!.*[-]$)(?!.*[-]{2})[a-z0-9-]+$"
    },
    "Priority" : {
      "type" : "integer",
      "maximum" : 100,
      "minimum" : 1
    },
    "ServiceIdentifier" : {
      "type" : "string",
      "maxLength" : 2048,
      "minLength" : 20,
      "pattern" : "^((svc-[0-9a-z]{17})|(arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:service/svc-[0-9a-z]{17}))$"
    },
    "Tags" : {
      "type" : "array",
      "insertionOrder" : False,
      "uniqueItems" : True,
      "minItems" : 0,
      "maxItems" : 50,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "propertyTransform" : {
    "/properties/Action/Forward/TargetGroups/*/TargetGroupIdentifier" : "$split(TargetGroupIdentifier, \"/\")[-1]"
  },
  "required" : [ "Action", "Match", "Priority" ],
  "readOnlyProperties" : [ "/properties/Arn", "/properties/Id" ],
  "createOnlyProperties" : [ "/properties/ListenerIdentifier", "/properties/ServiceIdentifier", "/properties/Name" ],
  "writeOnlyProperties" : [ "/properties/ListenerIdentifier", "/properties/ServiceIdentifier" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "additionalIdentifiers" : [ [ "/properties/ServiceIdentifier", "/properties/ListenerIdentifier", "/properties/Name" ] ],
  "handlers" : {
    "create" : {
      "permissions" : [ "vpc-lattice:CreateRule", "vpc-lattice:GetRule", "vpc-lattice:ListTagsForResource", "vpc-lattice:TagResource" ]
    },
    "read" : {
      "permissions" : [ "vpc-lattice:GetRule", "vpc-lattice:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "vpc-lattice:UpdateRule", "vpc-lattice:GetRule", "vpc-lattice:TagResource", "vpc-lattice:UntagResource", "vpc-lattice:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "vpc-lattice:DeleteRule", "vpc-lattice:UntagResource" ]
    },
    "list" : {
      "permissions" : [ "vpc-lattice:ListRules" ],
      "handlerSchema" : {
        "properties" : {
          "ServiceIdentifier" : {
            "type" : "string",
            "maxLength" : 2048,
            "minLength" : 20,
            "pattern" : "^((svc-[0-9a-z]{17})|(arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:service/svc-[0-9a-z]{17}))$"
          },
          "ListenerIdentifier" : {
            "type" : "string",
            "maxLength" : 2048,
            "minLength" : 20,
            "pattern" : "^((listener-[0-9a-z]{17})|(arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:service/svc-[0-9a-z]{17}/listener/listener-[0-9a-z]{17}))$"
          }
        },
        "required" : [ "ServiceIdentifier", "ListenerIdentifier" ]
      }
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "vpc-lattice:UntagResource", "vpc-lattice:TagResource", "vpc-lattice:ListTagsForResource" ]
  }
}