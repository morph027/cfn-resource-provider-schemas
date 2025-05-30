SCHEMA = {
  "typeName" : "AWS::Location::APIKey",
  "description" : "Definition of AWS::Location::APIKey Resource Type",
  "definitions" : {
    "ApiKeyRestrictions" : {
      "type" : "object",
      "properties" : {
        "AllowActions" : {
          "type" : "array",
          "items" : {
            "type" : "string",
            "maxLength" : 200,
            "minLength" : 5,
            "pattern" : "^(geo|geo-routes|geo-places|geo-maps):\\w*\\*?$"
          },
          "maxItems" : 24,
          "minItems" : 1,
          "insertionOrder" : False
        },
        "AllowResources" : {
          "type" : "array",
          "items" : {
            "type" : "string",
            "maxLength" : 1600,
            "pattern" : "(^arn(:[a-z0-9]+([.-][a-z0-9]+)*):geo(:([a-z0-9]+([.-][a-z0-9]+)*))(:[0-9]+):((\\*)|([-a-z]+[/][*-._\\w]+))$)|(^arn(:[a-z0-9]+([.-][a-z0-9]+)*):(geo-routes|geo-places|geo-maps)(:((\\*)|([a-z0-9]+([.-][a-z0-9]+)*)))::((provider[\\/][*-._\\w]+))$)"
          },
          "maxItems" : 8,
          "minItems" : 1,
          "insertionOrder" : False
        },
        "AllowReferers" : {
          "type" : "array",
          "items" : {
            "type" : "string",
            "maxLength" : 253,
            "pattern" : "^([$\\-._+!*\\x{60}(),;/?:@=&\\w]|%([0-9a-fA-F?]{2}|[0-9a-fA-F?]?[*]))+$"
          },
          "maxItems" : 5,
          "minItems" : 1,
          "insertionOrder" : False
        }
      },
      "required" : [ "AllowActions", "AllowResources" ],
      "additionalProperties" : False
    },
    "TagMap" : {
      "type" : "object",
      "maxProperties" : 50,
      "patternProperties" : {
        "^([\\p{L}\\p{Z}\\p{N}_.,:/=+\\-@]*)$" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0,
          "pattern" : "^([\\p{L}\\p{Z}\\p{N}_.,:/=+\\-@]*)$"
        }
      },
      "additionalProperties" : False
    },
    "Unit" : {
      "type" : "object",
      "additionalProperties" : False
    },
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "minLength" : 1,
          "maxLength" : 128,
          "pattern" : "^[a-zA-Z+-=._:/]+$"
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "minLength" : 0,
          "maxLength" : 256,
          "pattern" : "^[A-Za-z0-9 _=@:.+-/]*$"
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    },
    "iso8601UTC" : {
      "description" : "The datetime value in ISO 8601 format. The timezone is always UTC. (YYYY-MM-DDThh:mm:ss.sssZ)",
      "type" : "string",
      "pattern" : "^([0-2]\\d{3})-(0[0-9]|1[0-2])-([0-2]\\d|3[01])T([01]\\d|2[0-4]):([0-5]\\d):([0-6]\\d)((\\.\\d{3})?)Z$"
    }
  },
  "properties" : {
    "CreateTime" : {
      "$ref" : "#/definitions/iso8601UTC"
    },
    "Description" : {
      "type" : "string",
      "maxLength" : 1000,
      "minLength" : 0
    },
    "ExpireTime" : {
      "$ref" : "#/definitions/iso8601UTC"
    },
    "ForceUpdate" : {
      "type" : "boolean"
    },
    "KeyArn" : {
      "type" : "string",
      "maxLength" : 1600,
      "pattern" : "^arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:([^/].*)?$"
    },
    "KeyName" : {
      "type" : "string",
      "maxLength" : 100,
      "minLength" : 1,
      "pattern" : "^[-._\\w]+$"
    },
    "NoExpiry" : {
      "type" : "boolean"
    },
    "Restrictions" : {
      "$ref" : "#/definitions/ApiKeyRestrictions"
    },
    "Tags" : {
      "description" : "An array of key-value pairs to apply to this resource.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "minItems" : 0,
      "maxItems" : 200,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "UpdateTime" : {
      "$ref" : "#/definitions/iso8601UTC"
    },
    "ForceDelete" : {
      "type" : "boolean"
    },
    "Arn" : {
      "type" : "string",
      "maxLength" : 1600,
      "pattern" : "^arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:([^/].*)?$"
    }
  },
  "required" : [ "KeyName", "Restrictions" ],
  "readOnlyProperties" : [ "/properties/CreateTime", "/properties/Arn", "/properties/KeyArn", "/properties/UpdateTime" ],
  "writeOnlyProperties" : [ "/properties/ForceUpdate", "/properties/ForceDelete", "/properties/NoExpiry" ],
  "createOnlyProperties" : [ "/properties/KeyName" ],
  "primaryIdentifier" : [ "/properties/KeyName" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "geo:CreateKey", "geo:DescribeKey", "geo:TagResource", "geo:UntagResource", "geo:GetMapTile", "geo:GetMapStyleDescriptor", "geo:GetMapSprites", "geo:GetMapGlyphs", "geo:SearchPlaceIndexForText", "geo:SearchPlaceIndexForPosition", "geo:SearchPlaceIndexForSuggestions", "geo:GetPlace", "geo:CalculateRoute", "geo:CalculateRouteMatrix", "geo-maps:GetTile", "geo-maps:GetStaticMap", "geo-places:Autocomplete", "geo-places:Geocode", "geo-places:GetPlace", "geo-places:ReverseGeocode", "geo-places:SearchNearby", "geo-places:SearchText", "geo-places:Suggest", "geo-routes:CalculateIsolines", "geo-routes:CalculateRouteMatrix", "geo-routes:CalculateRoutes", "geo-routes:OptimizeWaypoints", "geo-routes:SnapToRoads" ]
    },
    "read" : {
      "permissions" : [ "geo:DescribeKey" ]
    },
    "update" : {
      "permissions" : [ "geo:CreateKey", "geo:DescribeKey", "geo:TagResource", "geo:UntagResource", "geo:GetMapTile", "geo:GetMapStyleDescriptor", "geo:GetMapSprites", "geo:GetMapGlyphs", "geo:SearchPlaceIndexForText", "geo:SearchPlaceIndexForPosition", "geo:SearchPlaceIndexForSuggestions", "geo:GetPlace", "geo:CalculateRoute", "geo:CalculateRouteMatrix", "geo-maps:GetTile", "geo-maps:GetStaticMap", "geo-places:Autocomplete", "geo-places:Geocode", "geo-places:GetPlace", "geo-places:ReverseGeocode", "geo-places:SearchNearby", "geo-places:SearchText", "geo-places:Suggest", "geo-routes:CalculateIsolines", "geo-routes:CalculateRouteMatrix", "geo-routes:CalculateRoutes", "geo-routes:OptimizeWaypoints", "geo-routes:SnapToRoads", "geo:UpdateKey" ]
    },
    "delete" : {
      "permissions" : [ "geo:DeleteKey", "geo:DescribeKey" ]
    },
    "list" : {
      "permissions" : [ "geo:ListKeys" ]
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "geo:TagResource", "geo:UntagResource" ]
  },
  "additionalProperties" : False
}