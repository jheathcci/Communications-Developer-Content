/*
 * SaasPro
 * APIs to interface with communications tax engine.<br />The API requires Basic authentication.<br />Users with access to multiple clients must also set request header parameter for <code>client_id</code>.<br />Set <code>client_profile_id</code> to specify profile to be used for taxation.
 *
 * The version of the OpenAPI document: v2
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import org.openapitools.client.model.Location;
import org.openapitools.client.model.TaxBracket;

/**
 * Tax rate override information.
 */
@ApiModel(description = "Tax rate override information.")
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2020-02-14T16:02:52.336-05:00[America/New_York]")
public class TaxOverride {
  public static final String SERIALIZED_NAME_LOC = "loc";
  @SerializedName(SERIALIZED_NAME_LOC)
  private Location loc = null;

  public static final String SERIALIZED_NAME_SCP = "scp";
  @SerializedName(SERIALIZED_NAME_SCP)
  private Integer scp;

  public static final String SERIALIZED_NAME_TID = "tid";
  @SerializedName(SERIALIZED_NAME_TID)
  private Integer tid;

  public static final String SERIALIZED_NAME_LVL = "lvl";
  @SerializedName(SERIALIZED_NAME_LVL)
  private Integer lvl;

  public static final String SERIALIZED_NAME_LVL_EXM = "lvlExm";
  @SerializedName(SERIALIZED_NAME_LVL_EXM)
  private Boolean lvlExm;

  public static final String SERIALIZED_NAME_BRKT = "brkt";
  @SerializedName(SERIALIZED_NAME_BRKT)
  private List<TaxBracket> brkt = null;


  public TaxOverride loc(Location loc) {
    
    this.loc = loc;
    return this;
  }

   /**
   * Get loc
   * @return loc
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Location getLoc() {
    return loc;
  }


  public void setLoc(Location loc) {
    this.loc = loc;
  }


  public TaxOverride scp(Integer scp) {
    
    this.scp = scp;
    return this;
  }

   /**
   * Get scp
   * @return scp
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Integer getScp() {
    return scp;
  }


  public void setScp(Integer scp) {
    this.scp = scp;
  }


  public TaxOverride tid(Integer tid) {
    
    this.tid = tid;
    return this;
  }

   /**
   * Get tid
   * @return tid
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Integer getTid() {
    return tid;
  }


  public void setTid(Integer tid) {
    this.tid = tid;
  }


  public TaxOverride lvl(Integer lvl) {
    
    this.lvl = lvl;
    return this;
  }

   /**
   * Get lvl
   * @return lvl
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Integer getLvl() {
    return lvl;
  }


  public void setLvl(Integer lvl) {
    this.lvl = lvl;
  }


  public TaxOverride lvlExm(Boolean lvlExm) {
    
    this.lvlExm = lvlExm;
    return this;
  }

   /**
   * Get lvlExm
   * @return lvlExm
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Boolean getLvlExm() {
    return lvlExm;
  }


  public void setLvlExm(Boolean lvlExm) {
    this.lvlExm = lvlExm;
  }


  public TaxOverride brkt(List<TaxBracket> brkt) {
    
    this.brkt = brkt;
    return this;
  }

  public TaxOverride addBrktItem(TaxBracket brktItem) {
    if (this.brkt == null) {
      this.brkt = new ArrayList<TaxBracket>();
    }
    this.brkt.add(brktItem);
    return this;
  }

   /**
   * Get brkt
   * @return brkt
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public List<TaxBracket> getBrkt() {
    return brkt;
  }


  public void setBrkt(List<TaxBracket> brkt) {
    this.brkt = brkt;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TaxOverride taxOverride = (TaxOverride) o;
    return Objects.equals(this.loc, taxOverride.loc) &&
        Objects.equals(this.scp, taxOverride.scp) &&
        Objects.equals(this.tid, taxOverride.tid) &&
        Objects.equals(this.lvl, taxOverride.lvl) &&
        Objects.equals(this.lvlExm, taxOverride.lvlExm) &&
        Objects.equals(this.brkt, taxOverride.brkt);
  }

  @Override
  public int hashCode() {
    return Objects.hash(loc, scp, tid, lvl, lvlExm, brkt);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TaxOverride {\n");
    sb.append("    loc: ").append(toIndentedString(loc)).append("\n");
    sb.append("    scp: ").append(toIndentedString(scp)).append("\n");
    sb.append("    tid: ").append(toIndentedString(tid)).append("\n");
    sb.append("    lvl: ").append(toIndentedString(lvl)).append("\n");
    sb.append("    lvlExm: ").append(toIndentedString(lvlExm)).append("\n");
    sb.append("    brkt: ").append(toIndentedString(brkt)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}
