// Onway design system — component types (documentation only, not type-checked).

// ---------- brand ----------
export interface LogoProps { variant?: "light" | "dark" | "ink" | "white"; height?: number; }
export function Logo(props: LogoProps): JSX.Element;

export interface AppIconProps { variant?: "customer" | "driver" | "favicon"; size?: number; }
export function AppIcon(props: AppIconProps): JSX.Element;

export interface IconProps { name: string; size?: number; } // Lucide name; this bundle ships a small demo subset
export function Icon(props: IconProps): JSX.Element;

// ---------- core ----------
export type ButtonVariant = "primary" | "secondary" | "outline" | "ghost" | "destructive";
export type ButtonSize = "sm" | "md" | "lg" | "xl";
export type ButtonState = "default" | "hover" | "pressed" | "loading" | "disabled";
export interface ButtonProps { variant?: ButtonVariant; size?: ButtonSize; state?: ButtonState; children?: string; }
export function Button(props: ButtonProps): JSX.Element;

export interface IconButtonProps { label: string; glyph?: string; variant?: "toolbar" | "row"; }
export function IconButton(props: IconButtonProps): JSX.Element;

export interface AvatarProps { size?: number; initials?: string; src?: string; name?: string; }
export function Avatar(props: AvatarProps): JSX.Element;

export interface CardProps { children?: JSX.Element | JSX.Element[] | string; }
export function Card(props: CardProps): JSX.Element;

export interface BadgeProps { count: number; }
export function Badge(props: BadgeProps): JSX.Element;

export interface TagProps { selected?: boolean; children?: string; }
export function Tag(props: TagProps): JSX.Element;

// ---------- navigation ----------
export interface TopBarProps { title?: string; }
export function TopBar(props: TopBarProps): JSX.Element;

export interface TabBarItem { label: string; icon: string; active?: boolean; badge?: number; }
export interface TabBarProps { items?: TabBarItem[]; }
export function TabBar(props: TabBarProps): JSX.Element;

export interface TabsProps { items?: string[]; active?: number; }
export function Tabs(props: TabsProps): JSX.Element;

export interface SidebarNavItem { label: string; active?: boolean; badge?: number; }
export interface SidebarNavProps { items?: SidebarNavItem[]; }
export function SidebarNav(props: SidebarNavProps): JSX.Element;

export interface ListRowProps { title?: string; subtitle?: string; trailing?: JSX.Element; }
export function ListRow(props: ListRowProps): JSX.Element;

// ---------- form ----------
export interface InputProps { id?: string; label: string; placeholder?: string; value?: string; state?: "default" | "focus" | "error" | "disabled"; helper?: string; }
export function Input(props: InputProps): JSX.Element;

export interface SelectProps { label: string; options?: string[]; }
export function Select(props: SelectProps): JSX.Element;

export interface CheckboxProps { checked?: boolean; children?: string; }
export function Checkbox(props: CheckboxProps): JSX.Element;

export interface RadioProps { label?: string; options?: string[]; }
export function Radio(props: RadioProps): JSX.Element;

export interface SwitchProps { checked?: boolean; children?: string; }
export function Switch(props: SwitchProps): JSX.Element;

export interface SegmentedControlProps { items?: string[]; active?: number; }
export function SegmentedControl(props: SegmentedControlProps): JSX.Element;

// ---------- feedback / overlay ----------
export interface SkeletonProps { variant?: "line" | "block"; }
export function Skeleton(props: SkeletonProps): JSX.Element;

export interface ToastProps { tone?: "success" | "danger"; children?: string; action?: string; }
export function Toast(props: ToastProps): JSX.Element;

export interface BannerProps { tone?: "info" | "success" | "warning" | "danger" | "offline" | "locked"; children?: string; action?: string; }
export function Banner(props: BannerProps): JSX.Element;

export interface DialogProps { title?: string; children?: string; critical?: boolean; }
export function Dialog(props: DialogProps): JSX.Element;

export interface SheetProps { children?: JSX.Element; }
export function Sheet(props: SheetProps): JSX.Element;

export interface TooltipProps { label: string; children?: string; }
export function Tooltip(props: TooltipProps): JSX.Element;

export interface EmptyStateProps { icon?: string; title?: string; description?: string; }
export function EmptyState(props: EmptyStateProps): JSX.Element;

export interface ProgressBarProps { value?: number; steps?: string[]; currentStep?: number; }
export function ProgressBar(props: ProgressBarProps): JSX.Element;

// ---------- status ----------
export type StatusKey =
  | "requested" | "searching" | "matching" | "accepted" | "confirmed"
  | "arriving" | "arrived" | "preparing" | "atOutlet" | "pickup" | "proofPending" | "changeRequested" | "pendingReview" | "unpaid" | "paused"
  | "inProgress" | "delivering" | "appeal"
  | "completed" | "proofVerified" | "online" | "approved" | "active" | "published"
  | "proofRejected" | "disputed" | "issue" | "rejected" | "locked"
  | "cancelled" | "offline" | "expired" | "draft" | "finalized";
export interface StatusPillProps { status: StatusKey; size?: "sm" | "md"; label?: string; pulse?: boolean; }
export function StatusPill(props: StatusPillProps): JSX.Element;

// ---------- map ----------
export interface MapSurfaceProps { variant?: "route" | "region"; }
export function MapSurface(props: MapSurfaceProps): JSX.Element;

export interface AddressPickerProps {}
export function AddressPicker(props: AddressPickerProps): JSX.Element;

export interface RegionEditorToolbarProps {}
export function RegionEditorToolbar(props: RegionEditorToolbarProps): JSX.Element;

// ---------- booking ----------
export interface JobStatusHeaderProps { status?: StatusKey; headline?: string; meta?: string; step?: number; }
export function JobStatusHeader(props: JobStatusHeaderProps): JSX.Element;

export interface TimelineItem { label: string; time?: string; actor?: string; state: "done" | "current" | "pending" | "failed"; }
export interface TimelineProps { items?: TimelineItem[]; } // pass `actor` per item for the Audit variant (CMP-052)
export function Timeline(props: TimelineProps): JSX.Element;

export interface PriceRowProps { rows?: { label: string; value: string }[]; }
export function PriceRow(props: PriceRowProps): JSX.Element;

export interface QuantityStepperProps { value?: number; }
export function QuantityStepper(props: QuantityStepperProps): JSX.Element;

export interface RatingStarsProps { value?: number; }
export function RatingStars(props: RatingStarsProps): JSX.Element;

export interface StatCardProps { label?: string; value?: string; delta?: string; }
export function StatCard(props: StatCardProps): JSX.Element;

export interface JobCardProps { status?: StatusKey; id?: string; customer?: string; distance?: string; }
export function JobCard(props: JobCardProps): JSX.Element;

export interface ProofUploadProps { state?: "empty" | "uploading" | "failed" | "submitted" | "verified" | "rejected"; filename?: string; amount?: string; reason?: string; }
export function ProofUpload(props: ProofUploadProps): JSX.Element;

// ---------- communication ----------
export interface ChatMessage { from: "me" | "them"; text: string; expired?: boolean; }
export interface ChatRoomProps { messages?: ChatMessage[]; }
export function ChatRoom(props: ChatRoomProps): JSX.Element;

export interface ComplaintFormProps {}
export function ComplaintForm(props: ComplaintFormProps): JSX.Element;

// ---------- admin ----------
export interface DataTableRow { id: string; name: string; status: StatusKey; }
export interface DataTableProps { rows?: DataTableRow[]; }
export function DataTable(props: DataTableProps): JSX.Element;

export interface AdminDrawerProps { title?: string; children?: JSX.Element; }
export function AdminDrawer(props: AdminDrawerProps): JSX.Element;

export interface CatalogEditorProps {}
export function CatalogEditor(props: CatalogEditorProps): JSX.Element;

export interface PolicyConfigFormProps {}
export function PolicyConfigForm(props: PolicyConfigFormProps): JSX.Element;

export interface FilterBarProps {}
export function FilterBar(props: FilterBarProps): JSX.Element;
